# write a func that takes 2 lists and provides the product of coressponding elements as a new list and
def multiply_two_lists(a, b):
    length = len(a)
    result = []
    for i in range(length):
        result.append(a[i]*b[i])
    return result


l1 = list(map(int, input().rstrip().split()))
l2 = list(map(int, input().rstrip().split()))
print(multiply_two_lists(l1, l2))
# call the new list as c, get square root of elemnsts in C and then multiply those 3 square rrots and then find the 8th  power of that product
# write a function that takes in list and another eleemnt and check how many eleelmnts in the list are > than this element
# write a function that takes a list as an input , now create another list that is formed out of the min and max of the list
# remove those min and max out of the 1st list and create another list such that the elements= len of 1st, len of 2nd ,max of 1st and max of 2nd list
# take a function that takes tuples and sets and list as inputs and create 3 diff lists which contain min element , max and avg elements of the list, sets and tuples
# give the inverse of the above list and combining  into a new list
# create a list of lists where the inner list should be 1,2,3, and the other 4,5,6 and the other 7,8,9
# get the len of bigger and smaller list
# call the bigger list as biglist, smaller list as small list l1, l2 and l3
# using indexes get the second element of the second list
# reverse the second small list
#  get the sum of the maps of each sub list
