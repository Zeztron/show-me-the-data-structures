## Huffman Coding

I used dictionaries to store data since it allows for O(1) runtime.

The time complexity for encoding the characters based on its frequence is O(nlog n)
Getting the minimum frequency from the priority queue i used takes 2 * (n-1) times which the time complexity of that is O (log n)

The overall complexity is O (nlog n)