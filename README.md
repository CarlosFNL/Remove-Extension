# Remove-Extension
Simple Python Script to get the extension of a file,web address etc.
There are two solutions: 
The first one uses a for loop to iterate in the string and find the last ".". Then we return the string from the index where the last dot is until the end of the string.
The second one uses a while loop. In this case we take advantage of the fact that the extension is always in the end, so we start looking from the end of the string until we found a dot and store the value of the index in a variable. Then we return the same as the first case. 
Both methods have also a function to print extensions from a list of strings. It is basically a implementation of one of the functions above through a for loop.
