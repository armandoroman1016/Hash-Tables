# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        hashed = self._hash_mod(key)
        key_val = LinkedPair(key, value)

        # if hashed key is none set the value as a linked pair
        if not self.storage[hashed]:
            self.storage[hashed] = key_val

        # else create new linked pair and set it to the next value of current linked pair
        else:
            
            current = self.storage[hashed]
            prev = None
            # iterating to find next available spot in linked list
            while current:
                
                # update scenario - returns immediateley after update
                if current.key == key:
                    current.value = value
                    return

                # updating previous and current for next iteration
                prev = current
                current = current.next

            # we know after the while loop that current in none so we set the next key value pairs from previous iteration
            prev.next = key_val




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # hash the key
        hashed = self._hash_mod(key)

        # if storage[hashed] is none then return warning

        if not self.storage[hashed]:
            print("No current value for key")
            
 
        # if key is equal to storage[hashed] and there is no other linked pairs at that value, set to none
        elif self.storage[hashed].key == key and not self.storage[hashed].next:
            self.storage[hashed] = None
            
        
        else:
             current = self.storage[hashed]
             prev = None
             nxt = current.next
             while current:
                #  if matching key is found, set the item to none
                # and point the previous' next pointer to the current next
                 if current.key == key:
                     prev.next = current.next
                     current = None
                     break
                
                 prev = current
                 current = current.next



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        hashed = self._hash_mod(key)

        if self.storage[hashed]:

            if self.storage[hashed].key == key:
                return self.storage[hashed].value
            
            else:

                if self.storage[hashed].next:
                    
                    current = self.storage[hashed].next

                    while current:

                        if current.key == key:
                            return current.value
                        
                        current = current.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
