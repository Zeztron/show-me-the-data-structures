import sys
import heapq

'''
    Encoding:
    Step 1. Build frequency dictionary
    Step 2. Build priority queue (used MinHeap)
    Step 3. Build Huffman Tree by selecing 2 min nodes and merging them
    Step 4. Assign codes to characters (by traversing the tree from root)
    Step 5. Encode the input text (by replacing character with its code)
    Step 6. If overall length of bit streams is not multiple of 8, add some padding to the text

    Decoding:
    Step 1: Read in the bits
    Step 2: Read padding. Remove padded bits.
    Step 3: Decode the bits - read the bits and replace the valid Huffman Code bits with the character values

    Notes: 
    - Need to store Huffman Codes mapping while encoding
'''

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        
        def __lt__(self, other):
            return self.freq < other.freq
        
        def __eq__(self, other):
            if (other == None) :
                return False
            
            if (not isinstance(other, HeapNode)):
                return False
       
            return self.freq == other.freq

    def make_frequency_dict(self, text):
        # Need to calculate frequency and return 
        frequency = {}
        for char in text:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1
        
        return frequency

    def make_heap(self, frequency):
        # Create priority queue
        for key in frequency:
            node = self.HeapNode(key, frequency[key])

           
            heapq.heappush(self.heap, node)
    

    def merge_codes(self):
        # Build huffman tree and save root node in heap
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, node, current_code):
        if (node == None):
            return 
        
        if (node.char != None):
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char

        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")
        
    def make_codes(self):
        # Make code for characters and save
        root_node = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root_node, current_code)

    def get_encoded_text(self, data):
        # Returns the encoded text
        encoded_text = ""
        for char in data:
            encoded_text += self.codes[char]
        
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        # pad encoded text and return
        extra_padding = 8 - len(encoded_text) % 8

        for i in range(extra_padding):
            encoded_text += "0"
        
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def remove_padding(self, text):
        # Remove padding and return
        padded_info = text[:8]
        extra_padding = int(padded_info, 2)

        text = text[8:]
        encoded_text = text[:-1*extra_padding]

        return encoded_text
    
    def decode_text(self, encoded_text):
        # Decode and return 
        current_code = ""
        decoded_text = ""

        for text in encoded_text:
            current_code += text
            if (current_code in self.reverse_mapping):
                char = self.reverse_mapping[current_code]
                decoded_text += char
                current_code = ""

        return decoded_text


    def huffman_encoding(self, data):

        frequency = self.make_frequency_dict(data)
    
        self.make_heap(frequency)
    
        self.merge_codes()
        self.make_codes()

        encoded_text = self.get_encoded_text(data)
        padded_encoded_text = self.pad_encoded_text(encoded_text)
        

        return padded_encoded_text, self.codes
    

    def huffman_decoding(self, data, tree):

        encoded_text = self.remove_padding(data)
        decoded_text = self.decode_text(encoded_text)

        return decoded_text


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffmanCoding = HuffmanCoding()

    encoded_data, tree = huffmanCoding.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffmanCoding.huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
