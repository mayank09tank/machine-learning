# data-scientist-and-machine-learning
1.#How do lists and tuples differ in terms of mutability and performance? When would you choose one over the other? 

**********************************LIST**********************************           *********************************TUPLE**********************************
Mutability:>>:  Mutable (can be modified: add, remove, update elements)                       Immutable (cannot be changed after creation) 
Performance:>>: Slower due to dynamic resizing and modification                               Faster as it is fixed in size and requires less memory
Memory Usage:>> Uses more memory due to dynamic allocation                                    Uses less memory as it has a fixed size
Functions:>>:>>	More built-in functions for modification (e.g., append(), remove())           Limited functions since it cannot be modified
use Case:>>:>>	When data needs to be changed frequently                                      When data should remain constant
Use lists when you need to modify the data.
Use tuples when you want to ensure data remains constant (e.g., representing coordinates, database records, etc.).

2.#Explain how Python handles type conversion between different data types, such as between integers and floats or between strings and lists.

#Implicit Conversion:>:>: Python converts smaller data types to larger ones to prevent data loss.
#num = 10      # Integer
#result = num + 5.5  # Float (int is converted to float)
#print(result)  
# Output: 15.5

#Explicit Conversion:>:>: Using functions like int(), float(), str(), and list().
num_str = "100"
num_int = int(num_str)  # Converts string to integer
print(num_int + 5) 
# Output: 105

char_list = list("hello")  # Converts string to list
print(char_list)  
# Output: ['h', 'e', 'l', 'l', 'o']


