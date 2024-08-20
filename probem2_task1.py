#Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. #Analyze the time complexity of this operation.

dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

def solution():
    dict_1.update(dict_2)
    print(dict_1)

solution() # time and space complexity is linear








