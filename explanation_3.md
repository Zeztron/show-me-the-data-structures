## Huffman Coding

I used dictionaries to store data since it allows for O(1) runtime.
I calculate the instances of each char in the string.. the one with the highest occurence is encoded (1) then next character is 01 then 001

Time complexity for the ``huffman_encoding`` method is O(n log n) since the ``sorted`` method is being used.
Space complexity is O(logn)