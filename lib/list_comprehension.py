def return_evens(num_list):
    new_list = [item for item in num_list if item % 2 == 0]
    return new_list

def make_exclamation(sentence_list):
    squared_minus_one = [n + "!" for n in sentence_list]
    return squared_minus_one
