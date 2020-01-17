#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    index = 0
    for weight in weights:
        different_weight = limit - weight
        guess = hash_table_retrieve(ht, different_weight)

        if guess is not None:
            if guess < index:
                return(index, guess)
            else: 
                return(index,guess)
        hash_table_insert(ht, weight, index)
        index += 1
            
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
