# Binary Search

This module allows the function of binary searching in strings, lists or tuples
<p>&nbsp;</p> 
<p>&nbsp;</p> 


## Installation

Run the following to install:
```python
pip install bisearch
```
<p>&nbsp;</p> 



## Usage
```python
import bisearch 

# Check if target exists within search range
bisearch.exist(target,field)

# Check where target is located within search range
bisearch.location(target,field)
```
<p>&nbsp;</p> 



## Types of target inputs 
*Target input refers to the first input argument when the function is called*  
<p>&nbsp;</p>  

**Int** - accepts int value --- *Note - int inputs are not compatible with string fields*


**Float** - accepts float value --- *Note - float inputs are not compatible with string fields*


**Single character string** - accepts single character string --- *Note - single character string inputs are only compatible with one word strings*


**Word string** - accepts string of single word --- *Note - word strings are only compatible with multiple word strings*
<p>&nbsp;</p> 
<p>&nbsp;</p> 


## Types of field inputs
*Field input refers to the second argument when the function is called*
<p>&nbsp;</p>   

**2D Array** - accepts any length 2D array


**Tuple** - accepts any length tuple --- *Note - tuples are converted into lists*


**One Word Strings** - accepts strings without any spaces --- *Note - string is split into list of characters*


**Multiple Word Strings** - accepts strings that are seperated by *one* white space --- *Note - string is split into list of words*
<p>&nbsp;</p> 
<p>&nbsp;</p> 




### Notes
*when using location if the target does not exist within the field the function will return None.*


