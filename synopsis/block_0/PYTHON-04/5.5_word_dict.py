sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm'
sentence = sentence.lower()
sentence = sentence.replace(",", "")
word_list = list(sentence.split())
word_dict = {}
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


"""
Вывод программы:
{'a': 3, 'robot': 1, 'may': 1, 'not': 1, 'injure': 1, 'human': 2,
 'being': 2, 'or': 1, 'through': 1, 'inaction': 1, 'allow': 1, 'to': 2, 'come': 1, 'harm': 1}
"""