# python 3
# calculate Jaccard between texts

import os
import sys

def Intersection(list1, list2):
    intersection_list = []
    for item in list1:
        if item in list2:
            intersection_list.append(item)
    return len(intersection_list)

def Intersection_list(list1, list2):
    intersection_list = []
    for item in list1:
        if item in list2:
            intersection_list.append(item)
    return intersection_list

def jaccard(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    jac = float(len(set1.intersection(set2))) / len(set1.union(set2))
    return jac    

def tokenize(file):
    f = open(os.path.join(sys.path[0], file), "r", encoding = "utf-8")
    proto_reader = f.read().lower()
    reader = ""
    for character in proto_reader:
        if character.isalpha() or character == " " or character.isnumeric():
            reader = reader + character
        else:
            reader = reader + " "

    tokenized_reader = reader.split()
    return tokenized_reader

def lemmatize(file):
    f = open(os.path.join(sys.path[0], file), "r", encoding = "utf-8")
    proto_reader = f.read().lower()
    reader = ""
    for character in proto_reader:
        if character.isalpha() or character == " " or character.isnumeric():
            reader = reader + character
        else:
            reader = reader + " "

    tokenized_reader = reader.split()

    from nltk.corpus import stopwords
    stopWords = set(stopwords.words('english'))
    filtered_reader = []

    for token in tokenized_reader:
        if token not in stopWords:
            filtered_reader.append(token)


    import nltk
    nltk.download('wordnet')
    from nltk.stem import WordNetLemmatizer

    # Create WordNetLemmatizer object
    wnl = WordNetLemmatizer()
    lemmatized_reader = []

    for token in filtered_reader:
        lemmatized_reader.append(wnl.lemmatize(token))

    return lemmatized_reader

Marlow_texts = ["Youth.txt", "Heart of Darkness.txt", "Lord Jim.txt", "Chance.txt"]

tokenized_texts = []

for text in Marlow_texts:
    tokenized_texts.append(lemmatize(text))

print(Marlow_texts[0], Marlow_texts[1], jaccard(tokenized_texts[0],tokenized_texts[1]), Intersection(tokenized_texts[0],tokenized_texts[1]))
print(Marlow_texts[0], Marlow_texts[2], jaccard(tokenized_texts[0],tokenized_texts[2]), Intersection(tokenized_texts[0],tokenized_texts[2]))
print(Marlow_texts[0], Marlow_texts[3], jaccard(tokenized_texts[0],tokenized_texts[3]), Intersection(tokenized_texts[0],tokenized_texts[3]))
print(Intersection(Intersection_list(tokenized_texts[0],tokenized_texts[2]), Intersection_list(tokenized_texts[0],tokenized_texts[3])))
print(jaccard(Intersection_list(tokenized_texts[0],tokenized_texts[2]), Intersection_list(tokenized_texts[0],tokenized_texts[3])))
print(Marlow_texts[1], Marlow_texts[2], jaccard(tokenized_texts[1],tokenized_texts[2]), Intersection(tokenized_texts[1],tokenized_texts[2]))
print(Marlow_texts[1], Marlow_texts[3], jaccard(tokenized_texts[1],tokenized_texts[3]), Intersection(tokenized_texts[1],tokenized_texts[3]))
print(Intersection(Intersection_list(tokenized_texts[1],tokenized_texts[2]), Intersection_list(tokenized_texts[1],tokenized_texts[3])))
print(jaccard(Intersection_list(tokenized_texts[1],tokenized_texts[2]), Intersection_list(tokenized_texts[1],tokenized_texts[3])))
print(Marlow_texts[2], Marlow_texts[3], jaccard(tokenized_texts[2],tokenized_texts[3]), Intersection(tokenized_texts[2],tokenized_texts[3]))

'''
Youth.txt Heart of Darkness.txt 0.2657182999648753 5271
Youth.txt Lord Jim.txt 0.1962283384301733 5920
Youth.txt Chance.txt 0.19729549988915984 5690
5530
0.8029197080291971
Heart of Darkness.txt Lord Jim.txt 0.34981060606060604 16574
Heart of Darkness.txt Chance.txt 0.34637153830604406 15969
15390
0.7440607396522165
Lord Jim.txt Chance.txt 0.43400016068128866 53715
'''