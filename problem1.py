def max_occur_chance(arr, lookup):
    dic_count = {}

    for key in lookup:
        count = 0
        for num in arr:
            if num in lookup[key]:
                count += 1
        dic_count[key] = count

    max_key = None
    max_count = -1
    for key in dic_count:
        if dic_count[key] > max_count:
            max_count = dic_count[key]
            max_key = key

    return max_key

""" explanation 

create max_occur_chance function give 2 arguments (arr,lookup). fist assign one variable called dic_count (dictionary (key-value))
# iterate each dictionary key, initialize count  = 0, iterate each number in an arry
if num is associated with lookup[key] and increase the count value (number of occurences)

"""


        #  Test case 1
arr1 = [4, 13, 98, 54, 88, 16, 33]
lookup1 = {
    13: [],
    65: [89, 98, 33, 65, 878],
    24: [98, 54, 123, 234, 67],
    33: [43, 76, 9],
    41: [4, 13, 23, 56, 89, 00, 87, 654, 789, 54],
    54: [46, 32, 54, 66, 87, 88, 943, 16, 89, 33, 6],
    88: [13, 33],
    98: [88, 76, 77, 55, 32]
}

print("Test Case 1: key & occurrences :", max_occur_chance( arr1, lookup1))


# Test Case 2
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lookup2 = {
    11: [2, 4, 6, 8, 10],
    12: [1, 3, 5, 7, 9],
    13: [1, 2, 3, 4, 5],
    14: [6, 7, 8, 9, 10],
    15: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    16: [5, 6, 7, 8, 9, 10],
    17: [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

print("Test Case 2: key & occurrences :", max_occur_chance( arr2, lookup2))

# Test Case 3
arr3 = [3, 7, 15, 8, 20, 3, 10, 15, 7, 8]
lookup3 = {
    101: [3, 7, 15],
    102: [8, 20, 3],
    103: [10, 15, 7, 8],
    104: [3, 7, 8],
    105: [15, 20],
    106: [10, 7, 8],
    107: [3, 10, 15]
}

print("Test Case 3: key & occurrences :", max_occur_chance( arr3, lookup3))

arr4 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lookup4 = {
    201: [2, 4, 6, 8, 10],
    202: [12, 14, 16, 18, 20],
    203: [2, 8, 10, 12, 20],
    204: [4, 6, 14, 16, 18],
    205: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    206: [6, 8, 10, 12, 14, 16],
    207: [2, 4, 12, 16, 18, 20]
}

print("Test Case 4: key & occurrences :", max_occur_chance( arr4, lookup4))

# Test Case 5
arr5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
lookup5 = {
    301: [5, 10, 15, 20],
    302: [25, 30, 35, 40],
    303: [10, 15, 20, 25, 30],
    304: [15, 25, 35, 45, 50],
    305: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    306: [20, 30, 40, 50],
    307: [5, 10, 20, 25, 30, 35, 40, 45, 50]
}

print("Test Case 5: key & occurrences :", max_occur_chance( arr5, lookup5))

