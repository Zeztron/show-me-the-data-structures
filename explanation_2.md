## Finding Files

This is using recusion to go down in each directory and subdirectories to return the files found which then the path of those files get added to the list. Which will go down infinitely since there is no limit of depth of the amount of subdirectories in existance.

This implementation is a depth-first search recursive tree traversal algorithm. 
The traversal of the folders is recursive, i visit each node once so the time complexity is linear conbined with the number of files and folders in my input data. which is O(N)

The space complexity is O(D) as well where the D is the depth of the tree which in this case is the depth of the folder structure 