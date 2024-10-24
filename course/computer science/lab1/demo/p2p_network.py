import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Save public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(key.publickey().export_key())

# Load private key from a file
with open('private_key.pem', 'wb') as f:
    f.write(key.export_key())

# Encrypt data using recipient's public key
def encrypt_data(data, recipient_public_key):
    cipher_rsa = PKCS1_OAEP.new(recipient_public_key)
    encrypted_data = cipher_rsa.encrypt(data.encode())
    return encrypted_data

# Decrypt data using own private key
def decrypt_data(encrypted_data):
    cipher_rsa = PKCS1_OAEP.new(key)
    decrypted_data = cipher_rsa.decrypt(encrypted_data).decode()
    return decrypted_data

# Start P2P server
def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Server started. Waiting for incoming connections...')

    while True:
        client_socket, addr = server_socket.accept()
        print('Connected with', addr)

        # Receive encrypted data from client
        encrypted_data = client_socket.recv(1024)

        # Decrypt the received data
        decrypted_data = decrypt_data(encrypted_data)

        print('Received data:', decrypted_data)

        # Send encrypted response back to client
        response = encrypt_data('Response from server', client_public_key)
        client_socket.send(response)

        client_socket.close()

# Connect to P2P server
def connect_to_server():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send encrypted data to server
    data = encrypt_data('Data from client', server_public_key)
    client_socket.send(data)

    # Receive encrypted response from server
    encrypted_response = client_socket.recv(1024)

    # Decrypt the received response
    decrypted_response = decrypt_data(encrypted_response)

    print('Received response:', decrypted_response)

    client_socket.close()

# Load public keys for server and client
with open('public_key.pem', 'rb') as f:
    server_public_key = RSA.import_key(f.read())

with open('client_public_key.pem', 'rb') as f:
    client_public_key = RSA.import_key(f.read())

# Start P2P server in a separate thread
import threading
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Connect to P2P server
connect_to_server()
