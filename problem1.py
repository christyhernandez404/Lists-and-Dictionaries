#Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. 
# #Analyze the time and space complexity of this operation

def solution(n):
    newlist = [num**2 for num in range(1, n)] #
    return newlist


print(solution(8)) #time and space complexity is linear

#Implement a function to merge two pre-sorted lists into a single sorted list. 
# Analyze the time complexity of this operation.

def solution_2():
    a = [1 , 5, 7, 9, 25]
    b = [1, 8, 26, 99]
    for item in a:
        b.append(item)
        b.sort()
    return b

print(solution_2()) #time and space complexity is linear logrithmic




