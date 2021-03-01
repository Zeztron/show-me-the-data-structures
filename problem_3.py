import sys

def huffman_encoding(data):
    
    huff_dict = {}
    huff_tree = {}
    encoded_str = ''
    temp_str = '1'

    for char in data:
        huff_dict[char] = huff_dict.get(char, 0) + 1
    
    for item in sorted(huff_dict.items(), key=lambda x: x[1]):
        huff_tree[item[0]] = temp_str
        temp_str = '0' + temp_str
    
    for d in data:
        encoded_str += huff_tree[d]
    
    return encoded_str, huff_tree

def huffman_decoding(data,tree):
    
    huff_tree = {}
    decoded_str = ''
    temp_str = ''

    for char in tree:
        huff_tree[tree[char]] = char
    
    for d in data:
        if d == '1':
            decoded_str += huff_tree[temp_str + d]
            temp_str = ''
        else:
            temp_str += d 
    
    return decoded_str
    
    
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))