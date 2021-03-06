class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # checks if HTE has a key
    # if it does, returns the HTE
    # if it does not, returns none
    def find(self, key):
        current = self
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    # returns the last HTE
    def getLast(self):
        current = self
        while current.next is not None:
            current = current.next
        return current

    def delete(self, key):
        current = self
        print(f'key:{current.key}, value:{current.value}, next: {current.next}')
        # Deleting head of the list
        if current.key == key:
            self.key = None
            self.value = None
            self = current.next

        prev = current
        current = current.next

        while current is not None:
            if current.key == key:  # delete it
                prev.next = current.next

            else:
                prev = prev.next
                current = current.next
        return None


        # Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        The load factor is the number of keys divided by the capacity
        Implement this.
        """
        # Your code here
        # count = 0
        # for i in range(self.capacity):
        #     current = self.storage[i]
        #     while current is not None:
        #         count += 1
        #         current = current.next
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        fnv_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis

        for char in key:
            hash += hash * fnv_prime
            hash += hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Needs to be a high prime number
        hash = 7883

        for char in key:
            hash = hash * 33 + ord(char)
        return hash

    # def _hash(self, key):
    #     bytes_rep = key.encode()

    #     sum = 0
    #     for byte in bytes_rep:
    #         sum += byte
    #     return sum % MIN_CAPACITY

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2)

        index = self.hash_index(key)
        # if nothing there create the first HTE
        if not self.storage[index]:
            self.storage[index] = HashTableEntry(key, value)
            self.count += 1
        # check to see if key/value already exists
        node = self.storage[index].find(key)
        if node:
            # replace it if yes
            node.key = key
            node.value = value
        else:
            # add new HTE to linked list
            new_node = HashTableEntry(key, value)
            new_node.next = self.storage[index]
            self.count += 1

# def put(self, key, value): # For no collision test
#     index = self.hash_index(key)
#     self.storage[index] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.get_load_factor() < 0.2 and self.get_num_slots() >= MIN_CAPACITY * 2:
            self.resize(self.get_num_slots() / 2)
        index = self.hash_index(key)
        node = self.storage[index].find(key)
        if node:
            self.storage[index].delete(key)
            self.count -= 1
        else:
            print("ERROR")
    # def delete(self, key): # for no collision test
    #     index = self.hash_index(key)

    #     self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index]:
            node = self.storage[index].find(key)
            if node is not None:
                return node.value
            else:
                return None
        return None

    # def get(self, key): # For no collision test
    #     index = self.hash_index(key)
    #     if self.storage[index]:
    #         return self.storage[index].value
    #     return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_table = HashTable(new_capacity)

        for i in range(self.capacity):
            current = self.storage[i]
            while current is not None:
                new_table.put(current.key, current.value)
                current = current.next
                self.count += 1
        self.capacity = new_capacity
        self.storage = new_table.storage


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
