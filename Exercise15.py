def get_input():
    return input("Enter something: ")

def str_to_list(sentence):
    word_list = sentence.split()
    return word_list

def rev_str(sentence):
    i = len(sentence)-1
    rev_str = sentence
    sentence = ''
    while i>=0:
        sentence += rev_str[i] + ' '
        i-=1
    return sentence

sentence = get_input()
sentence = str_to_list(sentence)
sentence = rev_str(sentence)
print(sentence)