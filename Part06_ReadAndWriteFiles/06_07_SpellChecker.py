"""Write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them.
The case of the letters should be irrelevant to the functioning of your program.
The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct."""

if False:
    text = input('Write text: ')
else:
    text = 'We use ptython to make a spell checker'


with open('06_07_wordlist.txt') as words_file:
    word_list = []
    for line in words_file:
        word = line.strip()
        word_list.append(word)

text_list = text.split(' ')
output = []
for item in text_list:
    input_word = item.strip().lower()
    if input_word in word_list:
        output.append(item)
    else:
        output.append(f'*{item}*')

string = ''
for item in output:
    string += (str(item)+' ')
print(string)


# end=""：不换行输出 --更简洁
# for word in sentence.split(' '):
#     if word.lower() in words:
#         print(word + " ", end="")
#     else:
#         print("*" + word + "* ", end="")
