# Node class for doubly linked list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val  # Store both key and value
        self.prev = self.next = None  # Initialize pointers for doubly linked list


class LRUCache(object):

    def __init__(self, capacity):
        """
        Initialize the LRU Cache with a given capacity.
        :type capacity: int
        """
        self.cap = capacity                  # Maximum number of items allowed
        self.cache = {}                      # Hash map to store key -> node for O(1) access

        # Create dummy head (left) and tail (right) nodes to simplify insert/remove logic
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key):
        """
        Retrieve value from cache by key.
        If found, move it to the most recently used (right end).
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])     # Remove node from current position
            self.insert(self.cache[key])     # Insert node at the end (most recently used)
            return self.cache[key].val       # Return the value
        return -1                            # Key not found

    def remove(self, node):
        """
        Remove a node from the doubly linked list.
        :type node: Node
        """
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """
        Insert a node at the end (right before the dummy tail).
        :type node: Node
        """
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def put(self, key, value):
        """
        Add or update a key-value pair in the cache.
        If key already exists, update and move to most recently used.
        If over capacity, remove least recently used node from front.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])     # Remove the old node if key exists
        self.cache[key] = Node(key, value)   # Create and insert new node
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove least recently used node (just after dummy head)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
