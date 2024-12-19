'''Program to implement a Hash Map using a Dictionary'''

class HashMap:
    def __init__(self):
        self.map = {}  # Dictionary to represent the hash map

    def put(self, key, value):
        self.map[key] = value  # Insert key-value pair into the hash map

    def get(self, key):
        return self.map.get(key, "Key not found")  # Retrieve value for the given key

    def remove(self, key):
        if key in self.map:
            del self.map[key]  # Remove key-value pair from the hash map
        else:
            print(f"Key {key} not found.")

    def display(self):
        print(self.map)  # Display the entire hash map

# Example usage
hm = HashMap()
hm.put("name", "Alice")
hm.put("age", 30)
hm.display()  # Output: {'name': 'Alice', 'age': 30}

print(hm.get("name"))  # Output: Alice
hm.remove("age")
hm.display()  # Output: {'name': 'Alice'}
