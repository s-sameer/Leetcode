'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
'''
class ListNode:
    def __init__(self, key=-1, val=-1, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap(object):

    def __init__(self):
        # Inititalize array with dummy nodes
        self.map = [ListNode() for i in range(1000)]
    
    # helper func that maps a key to a index
    def hash(self, key):
        return key % len(self.map)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        cur = self.map[self.hash(key)] 
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        cur = self.map[self.hash(key)] 
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
