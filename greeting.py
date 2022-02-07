import inflect

def num_word(number):
    p = inflect.engine()
    return print(p.number_to_words(number))
