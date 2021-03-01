## Finding Files

This is using recusion to go down in each directory and subdirectories to return the files found which then the path of those files get added to the list. Which will go down infinitely since there is no limit of depth of the amount of subdirectories in existance.

The Time Complexity of this operation is O(m * n) which will loop through all of the subdirectories (m) and the number of files in said directories (n)

Space complexity is also O(m * n) since m represents the number of subdirectories to search and n represents the number of files to hold.