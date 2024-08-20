#Implement a function to find the intersection of two dictionaries, i.e., keys common to both 
# dictionaries along with their values. Analyze the time complexity of this operation

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

def solution_2(dict_1, dict_2):
    common = dict_1.items() & dict_2.items()
    final_dict = dict(common)
    print(final_dict)


solution_2(dict_1, dict_2) # time and space complexity is linear