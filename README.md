# Binary Search

This module allows the function of binary searching in strings, lists or tuples


## Installation

Run the following to install:
```python
pip install bisearch
```


## Usage
```python
import bisearch 

# Check if target exists within search range
bisearch.exist(target,field)

# Check where target is located within search range
bisearch.location(target,field)
```

## Notes
```
when using location if the target does not exist within the field the function will return None

when using location if the field is a string it will return the target position within the sorted array of string

when using strings if there are multiple words make sure each word is seperated by one white space