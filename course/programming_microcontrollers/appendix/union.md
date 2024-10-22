
```c++
#include <iostream>
using namespace std;

struct modes {
    unsigned others : 3;  // Permissions for others (3 bits)
    unsigned group  : 3;  // Permissions for group (3 bits)
    unsigned user   : 3;  // Permissions for user (3 bits)
    unsigned type   : 7;   // Type of file (7 bits)
};

union map {
    unsigned short statmode; // 16-bit short for file mode
    modes convert;           // Modes struct to interpret the bits
};

int main() {
    map mapper;              // Declare a map object

    // Correct binary representation
    unsigned short data = 0b0000000001111000; // User: 7, Group: 4, Others: 0, Type: 0
    mapper.statmode = data; // Assign the value to statmode

    // Output individual permission bits
    cout << "User permissions: " << mapper.convert.user << endl;   // Outputs user permissions
    cout << "Group permissions: " << mapper.convert.group << endl; // Outputs group permissions
    cout << "Others permissions: " << mapper.convert.others << endl; // Outputs others permissions
    cout << "File type: " << mapper.convert.type << endl;           // Outputs file type

    return 0;
}

```



```c++
#include <iostream>
using namespace std;

struct modes {
	unsigned others : 3; // Permissions for others (3 bits)
	unsigned group : 3; // Permissions for group (3 bits)
	unsigned user : 3; // Permissions for user (3 bits)
	unsigned type : 7; // Type of file (7 bits)
};

union map {
	unsigned short statmode; // 16-bit short for file mode
	
	modes convert; // Modes struct to interpret the bits
// Function to set permissions safely

	void setPermissions(unsigned u, unsigned g, unsigned o, unsigned t) {
		convert.user = u & 0b111; // Ensure only 3 bits are used
		convert.group = g & 0b111; // Ensure only 3 bits are used
		convert.others = o & 0b111; // Ensure only 3 bits are used
		convert.type = t & 0b1111111; // Ensure only 7 bits are used
	}
	
	  
	
	// Function to get the raw mode as a string for debugging
	
	string getModeAsString() {
		return "Mode: " + to_string(statmode);
	}

};

int main() {
	map mapper; // Declare a map object
	// Setting permissions using the method provided in the union
	mapper.setPermissions(7, 4, 0, 32); // User: 7, Group: 4, Others: 0, Type: 32
	// Output individual permission bits
	cout << "User permissions: " << mapper.convert.user << endl; // Outputs user permissions
	cout << "Group permissions: " << mapper.convert.group << endl; // Outputs group permissions
	cout << "Others permissions: " << mapper.convert.others << endl; // Outputs others permissions
	cout << "File type: " << mapper.convert.type << endl; // Outputs file type
	cout << mapper.getModeAsString() << endl; // Outputs raw mode for debugging
	
	// Bitwise operation example: Toggle the user permissions
	mapper.convert.user ^= 0b111; // Toggle user permissions (flips the bits)
	
	cout << "Toggled User permissions: " << mapper.convert.user << endl; // Outputs modified user permissions
	
	return 0;

}
```