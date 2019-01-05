# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci_list(n):
    list = [0,1]
    while len(list) < n:
        list.append(list[len(list) - 1] + list[len(list) - 2])
    return list

# print(fibonacci_list(10))

# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def isprime(number):
    for i in range(2, number//2):
        if number % i == 0:
            return False
    return True

def prime_list(list):
    returnList = []
    for element in list:
        if isprime(element):
            returnList.append(element)
    return returnList

# print(prime_list([12,13,14,15,16,17]))


# 3. Let a tuple (x, y) represent a point in a Cartesian system. Write a function that receives as a parameter a list of points and returns a list of unique tuples (a, b, c) representing the unique lines determined by those              points ((a, b, c) corresponds to the right ax + by +c  = 0).

def line_from_points(point1, point2):
    return (point2[1] - point1[1], point1[0] - point2[0], point1[0] * (point1[1] - point2[1]) + point1[1] * (point2[0] - point1[0]))

# print(line_from_points((1,3), (3,1)))

# 4. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def return_set_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return (set1.intersection(set2), set1.union(set2), set1.difference(set2), set2.difference(set1))

# print(return_set_operations([1,2,3,4], [2,4,5,6]))

# 5. Write a function that receives as a parameter an x ​​list, and a number k. Return a list of tuples that represent combinations of len (x) taken by k from list x. Example: for the list x = [1,2,3,4] and k = 3, return [(1,2,3),          (1,2,4), (1,3,4) 3, 4)].

def partial_solution(vector, x):
    for i in range(len(vector)):
        elem = vector[i]
        if vector.count(elem) > 1:
            return False
        if vector.index(elem) > 0:
            if x.index(elem) < x.index(vector[i-1]):
                return False
    return True

def build_combinations_list(x, k, solution, pos):
    if pos == k:
        print(solution)
    elif pos < k:
        pos+=1
        solution.append(0)
        for i in range(len(x)):
            solution[pos-1] = x[i]
            if (partial_solution(solution, x)):
                build_combinations_list(x, k, list(solution), pos)

def combinations(x, k):
    return build_combinations_list(x, k, [], 0)    

# combinations([1,2,3,4,5], 3)


# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],              [4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 , 4] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2, 4 is in lists 2 and 3.

def apparitions_in_lists(*lists, x: int):
    return_set = set()

    bigList = []
    for list in lists:
        for elem in list:
            bigList.append(elem)
    for elem in bigList:
        if bigList.count(elem) == x:
            return_set.add(elem)
    return return_set

# print(apparitions_in_lists([1,2,3], [2,3,4], [4,5,6], [4, 1, "test"], x = 2))

# 7. Write a function that receives as default a default x number equal to 1, a variable number of strings, and a boolean flag set to True. For each character string, generate a list containing the characters that have the           ASCII divisible by x if the flag is set to True, otherwise it should contain characters that have the non-xvid ASCII code. Example: x = 2, "test", "hello", "lab002", flag = False will return (["e", "s"], ["e" . Note: The                   function must return a variable number of lists that corresponds to the number of character strings received as an input.

def function(x = 1, *strings, flag = True):
    condition = lambda x: x
    if flag == True:
        condition = lambda y,x: y % x == 0
    else: 
        condition = lambda y,x : y % x != 0
    
    new_strings = []
    for string in strings:
        new_string = []
        for char in string:
            if condition(ord(char), x):
                new_string.append(char)
        new_strings.append(new_string)
    return new_strings

# print(function(2, "test", "hello", "lab002", flag = False))

# 8. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists,               etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1.5, a " , 6, "b"), (3,7, "c")]. Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len           (x) for x in input_lists]) tuples.

def transform_lists(*lists):
    return_list = []
    for _ in range(len(lists)):
        return_list.append([])

    max_size = max([len(list) for list in lists])
    for list in lists:
        while len(list) < max_size:
            list.append(None)

        for elem in list:
            return_list[list.index(elem)].append(elem)

    for i in range(len(return_list)):
        return_list[i] = tuple(return_list[i])

    return return_list

# print(transform_lists([1,2,3], [5,6,7], ["a", "b", "c"]))


# 9. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order_by_3rd_char_in_2nd_elem(list):
    list.sort(key = lambda tuple: tuple[1][2])
    return list

print(order_by_3rd_char_in_2nd_elem([('abc', 'bcd'), ('abc', 'zza')]))