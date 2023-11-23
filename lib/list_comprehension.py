#!/usr/bin/env python3

# def return_evens(num_list):
    
#     return [num for num in num_list if num & 1 == 0]

# def make_exclamation(sentence_list):
   
#     return [sentence + "!" for sentence in sentence_list]

def return_evens(num_list):
    pass
    evens = [num for num in num_list if num % 2 == 0]
    return evens
# Example usage
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Output: [0, 8]

def make_exclamation(sentence_list):
    pass
    if not sentence_list:
        return []
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    return exclamation_list
# Example usage
result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)  # Output: ["Hello!", "I'm doing great!", "Python is fun!"]