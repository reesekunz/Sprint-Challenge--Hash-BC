

# * Think about what we can store in the hash table in order to help us to solve this problem more efficiently.
# * What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key?
# * If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!


# Example:
# ```
# input: weights = [4, 6, 10, 15, 16], length = 5, limit = 21
# output: [3, 1]
# since these are the indices of weights 15 and 6 whose sum equals 21

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )
# Your function will return an instance of an `Answer` tuple that has the following form:
# ```
# (zero, one)
# ```
# where each element represents the item weights of the two packages. _**The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index.**_ If such a pair doesn’t exist for the given inputs, your function should return `None`.


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # PLANNING:
    # Insert weight values into hashtable
    # Loop through hashtable and retrieve values.
    # Check to see if theres any paired values (sum of values equals limit)
    # If any paired values, compare the values to each other. Higher valued index goes first, lower valued index goes second.
    # If no paired values that equal limit, return None.

    # insert weight values into hashtable
    # insert is looking for (hash_table, key, value)
    for x in range(length):
        hash_table_insert(ht, weights[x], x)
    # grab values from hashtable
    # retrieve  is looking for (hash_table, key)
    for x in range(length):
        matching_value = hash_table_retrieve(ht, (limit-weights[x]))
        # if pair exists (values of 2 indexs equal limit)
        if matching_value:
            print("matching_value", matching_value)
            print("x", x)
            # if matching value is higher valued index, return that one first.
            if matching_value > x:
                print("matching_value, x = ", [matching_value, x])
                return [matching_value, x]
            # if matching value is lower valued index, return that one second.
            else:
                print("x, matching_value = ", [x, matching_value])
                return [x, matching_value]
        # else:
        #     return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
