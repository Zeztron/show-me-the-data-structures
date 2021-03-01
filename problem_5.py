import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Block(timestamp, data, temp)
            self.tail.previous_hash = temp

def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

block_zero = Block(get_timestamp(), "abc123", 0)
block_one = Block(get_timestamp(), "xyz", block_zero)
block_two = Block(get_timestamp(), "hello world", block_one)

linked_list = LinkedList()
linked_list.append(get_timestamp(), "Hello")
linked_list.append(get_timestamp(), "World")

print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Linked list tail data : ", linked_list.tail.data)
print("Linked list tail previous hash data : ", linked_list.tail.previous_hash.data)