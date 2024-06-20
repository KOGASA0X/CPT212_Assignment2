# CPT212_Assignment2

## Project Structure

```
The Assignment2.ipynb in the repository is our main file. This file integrates and implements the complete functionality.  
All related references are annotated in the file.  

These are the files related to the bad character heuristic:  
bad_character_heuristic_test.py  
bad_character_heuristic.py  
Where bad_character_heuristic_test.py is the test file,  
and bad_character_heuristic.py is the implementation file.  

The following two are files related to the good suffix heuristic:  
good_suffix_shift.py  
good_suffix_shift2.py  

The file good_suffix_shift.py is an implementation I wrote after studying various sources.  
The file good_suffix_shift2.py is an implementation I found online. All related references are annotated in the file.  

```

## Functionality Description

In Assignment2.ipynb, we implemented two heuristic algorithms.  
You can understand the functionality of the functions inside based on comments or documentation, for example:  

Comments  
![alt text](readme/image.png)  

Documentation  
![alt text](readme/image-0.png)  

Or you can use the debugging feature and the built-in logging feature (only in methods related to the good suffix heuristic)  
![alt text](readme/image-1.png)  
It is False by default, pass in True to enable.  

Of course, there is also an option to turn it on in the main function.  
![alt text](readme/image-2.png)  
When enabled, it will display  
![alt text](readme/image-3.png)  
If it is closed, it will only display  
![alt text](readme/image-4.png)  

## Function Descriptions (Specific to Assignment2.ipynb)

def bad_character_heuristic(pattern, text)  
This function implements the bad character heuristic, returning the positions to move.

def good_suffix_shift(pattern, enable_print=False)  
This function implements the good suffix heuristic, returning the array of moves, i.e., the goodSuffix array.

def good_suffix_heuristic(pattern, text, enable_print=False)  
This function is an integrated implementation of the good suffix heuristic, calling good_suffix_shift so that the return value can be like bad_character_heuristic, returning the positions to move.

def boyer_moore(pattern, text, enable_print=False, enable_suffix_print=False)  
This function integrates the two heuristic algorithms, returning a list of matched positions.

def compute_lps(pattern)  
This function implements the calculation of the lps array, returning the lps array.

def kmp_search(text, pattern)  
This function implements the KMP algorithm, returning a list of matched positions.

