#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 
        'language': "C", 
        'Number': 89, 
        'track': "Low level", 
        'ids': [1, 2, 3] ,
        'friends': [
            {'name':"Biden", 'age':25, 'occupation':"Banker" },
            {'name':"Kendra", 'age':20, 'occupation':"Dancer" },
            {'name':"Mcgutter", 'age':35, 'occupation':"Civil Engineer" }]
        }
print_sorted_dictionary(a_dictionary)
