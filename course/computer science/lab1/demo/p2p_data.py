import socket
import struct
import threading
import time
import traceback


def btdebug(msg: str):
    """ Prints a message to the screen with the name of the current thread """
    print(f"[{str(threading.currentThread().getName())}] {msg}")


class BTPeer:
    """ Implements the core functionality that might be used by a peer in a P2P network. """

    def __init__(self, maxpeers: int, serverport: int, myid: str = None, serverhost: str = None):
        """ Initializes a peer with the ability to catalog information for up to maxpeers number of peers,
        listening on a given server port, with a given canonical peer name (id) and host address.
        If not supplied, the host address (serverhost) will be determined by attempting to connect to an Internet host like Google.
        """
        self.debug = 0
        self.maxpeers = int(maxpeers)
        self.serverport = int(serverport)
        if serverhost:
            self.serverhost = serverhost
        else:
            self.__initserverhost()

        if myid:
            self.myid = myid
        else:
            self.myid = f"{self.serverhost}:{self.serverport}"

        self.peerlock = threading.Lock()
        self.peers = {}
        self.shutdown = False
        self.handlers = {}
        self.router = None

    def __initserverhost(self):
        """ Attempt to connect to an Internet host in order to determine the local machine's IP address. """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.google.com", 80))
        self.serverhost = s.getsockname()[0]
        s.close()

    def __debug(self, msg: str):
        if self.debug:
            btdebug(msg)

    def __handlepeer(self, clientsock: socket.socket):
        """ Dispatches messages from the socket connection """
        self.__debug(f"New child {str(threading.currentThread().getName())}")
        self.__debug(f"Connected {str(clientsock.getpeername())}")

        host, port = clientsock.getpeername()
        peerconn = BTPeerConnection(None, host, port, clientsock, debug=False)

        try:
            msgtype, msgdata = peerconn.recvdata()
            if msgtype:
                msgtype = msgtype.upper()
            if msgtype not in self.handlers:
                self.__debug(f"Not handled: {msgtype}: {msgdata}")
            else:
                self.__debug(f"Handling peer msg: {msgtype}: {msgdata}")
                self.handlers[msgtype](peerconn, msgdata)
        except KeyboardInterrupt:
            raise
        except:
            if self.debug:
                traceback.print_exc()

        self.__debug(f"Disconnecting {str(clientsock.getpeername())}")
        peerconn.close()

    def __runstabilizer(self, stabilizer, delay):
        while not self.shutdown:
            stabilizer()
            time.sleep(delay)

    def setmyid(self, myid: str):
        self.myid = myid

    def startstabilizer(self, stabilizer, delay):
        """ Registers and starts a stabilizer function with this peer.
        The function will be activated every <delay> seconds.
        """
        t = threading.Thread(target=self.__runstabilizer, args=[stabilizer, delay])
        t.start()

    def addhandler(self, msgtype: str, handler):
        """ Registers the handler for the given message type with this peer """
        assert len(msgtype) == 4
        self.handlers[msgtype] = handler

    def addrouter(self, router):
        """ Registers a routing function with this peer.
        The setup of routing is as follows: This peer maintains a list of other known peers (in self.peers).
        The routing function should take the name of a peer (which may not necessarily be present in self.peers)
        and decide which of the known peers a message should be routed to next in order to (hopefully) reach the desired peer.
        The router function should return a tuple of three values: (next-peer-id, host, port).
        If the message cannot be routed, the next-peer-id should be None.
        """
        self.router = router

    def addpeer(self, peerid: str, host: str, port: int):
        """ Adds a peer name and host:port mapping to the known list of peers. """
        if peerid not in self.peers and (self.maxpeers == 0 or len(self.peers) < self.maxpeers):
            self.peers[peerid] = (host, int(port))
            return True
        else:
            return False

    def getpeer(self, peerid: str):
        """ Returns the (host, port) tuple for the given peer name """
        assert peerid in self.peers
        return self.peers[peerid]

    def removepeer(self, peerid: str):
        """ Removes peer information from the known list of peers. """
        if peerid in self.peers:
            del self.peers[peerid]

    def addpeerat(self, loc, peerid: str, host: str, port: int):
        """ Inserts a peer's information at a specific position in the list of peers.
        The functions addpeerat, getpeerat, and removepeerat should not be used concurrently with addpeer, getpeer, and/or removepeer.
        """
        self.peers[loc] = (peerid, host, int(port))

    def getpeerat(self, loc):
        if loc not in self.peers:
            return None
        return self.peers[loc]

    def removepeerat(self, loc):
        self.removepeer(loc)

    def getpeerids(self):
        """ Return a list of all known peer id's. """
        return list(self.peers.keys())

    def numberofpeers(self):
        """ Return the number of known peers. """
        return len(self.peers)

    def maxpeersreached(self):
        """ Returns whether the maximum limit of names has been added to the list of known peers.
        Always returns True if maxpeers is set to 0.
        """
        assert self.maxpeers == 0 or len(self.peers) <= self.maxpeers
        return self.maxpeers > 0 and len(self.peers) == self.maxpeers

    def makeserversocket(self, port: int, backlog: int = 5):
        """ Constructs and prepares a server socket listening on the given port. """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', port))
        s.listen(backlog)
        return s

    def sendtopeer(self, peerid: str, msgtype: str, msgdata: str, waitreply: bool = True):
        """
        sendtopeer( peer id, message type, message data, wait for a reply )
        -> [ ( reply type, reply data ), ... ]

        Send a message to the identified peer. In order to decide how to send the message,
        the router handler for this peer will be called.
        If no router function has been registered, it will not work.
        The router function should provide the next immediate peer to whom the message should be forwarded.
        The peer's reply, if it is expected, will be returned.

        Returns None if the message could not be routed.
        """
        if self.router:
            nextpid, host, port = self.router(peerid)
        if not self.router or not nextpid:
            self.__debug(f"Unable to route {msgtype} to {peerid}")
            return None
        return self.connectandsend(host, port, msgtype, msgdata, pid=nextpid, waitreply=waitreply)

    def connectandsend(self, host: str, port: int, msgtype: str, msgdata: str, pid=None, waitreply: bool = True):
        """
        connectandsend( host, port, message type, message data, peer id, wait for a reply )
        -> [ ( reply type, reply data ), ... ]

        Connects and sends a message to the specified host:port.
        The host's reply, if expected, will be returned as a list of tuples.
        """
        msgreply = []
        try:
            peerconn = BTPeerConnection(pid, host, port, debug=self.debug)
            peerconn.senddata(msgtype, msgdata)
            self.__debug(f"Sent {pid}: {msgtype}")

            if waitreply:
                onereply = peerconn.recvdata()
                while onereply != (None, None):
                    msgreply.append(onereply)
                    self.__debug(f"Got reply {pid}: {str(msgreply)}")
                    onereply = peerconn.recvdata()
            peerconn.close()
        except KeyboardInterrupt:
            raise
        except:
            if self.debug:
                traceback.print_exc()

        return msgreply

    def checklivepeers(self):
        """ Attempts to ping all currently known peers in order to ensure that they are still active.
        Removes any from the peer list that do not reply.
        This function can be used as a simple stabilizer.
        """
        todelete = []
        for pid in self.peers:
            isconnected = False
            try:
                self.__debug(f"Check live {pid}")
                host, port = self.peers[pid]
                peerconn = BTPeerConnection(pid, host, port, debug=self.debug)
                peerconn.senddata("PING", "")
                isconnected = True
            except:
                todelete.append(pid)
                if isconnected:
                    peerconn.close()

        self.peerlock.acquire()
        try:
            for pid in todelete:
                if pid in self.peers:
                    del self.peers[pid]
        finally:
            self.peerlock.release()

    def mainloop(self):
        s = self.makeserversocket(self.serverport)
        s.settimeout(2)
        self.__debug(f"Server started: {self.myid} ({self.serverhost}:{self.serverport})")

        while not self.shutdown:
            try:
                self.__debug("Listening for connections...")
                clientsock, clientaddr = s.accept()
                clientsock.settimeout(None)

                t = threading.Thread(target=self.__handlepeer, args=[clientsock])
                t.start()
            except KeyboardInterrupt:
                print("KeyboardInterrupt: stopping mainloop")
                self.shutdown = True
                continue
            except:
                if self.debug:
                    traceback.print_exc()
                    continue

        self.__debug("Main loop exiting")
        s.close()


class BTPeerConnection:
    def __init__(self, peerid, host, port, sock=None, debug=False):
        self.id = peerid
        self.debug = debug

        if not sock:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((host, int(port)))
        else:
            self.s = sock

        self.sd = self.s.makefile("rw", 0)

    def __makemsg(self, msgtype, msgdata):
        msglen = len(msgdata)
        msg = struct.pack("!4sL%ds" % msglen, msgtype, msglen, msgdata)
        return msg

    def __debug(self, msg):
        if self.debug:
            btdebug(msg)

    def senddata(self, msgtype, msgdata):
        try:
            msg = self.__makemsg(msgtype, msgdata)
            self.sd.write(msg)
            self.sd.flush()
        except KeyboardInterrupt:
            raise
        except:
            if self.debug:
                traceback.print_exc()
                return False
        return True

