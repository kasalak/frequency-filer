
#represent all text in sample.txt
import re

#convert text to all lower case
def word_frequency(text):
    words = {}
    for unique in text.split():
        words = re.sub('[^a-z\ \']+', " ", text).lower
        if unique in words:
            words[unique] += 1
        else:
            words[unique] = 1
    return word_frequency(text)

def file_text():
    file_name = input("Enter filename here. ")
    file_text = open(file_name, 'r')
    text = read(file_name)
    close(file_name)
    return file_text()


#get rid of sentence structure and convert text file to a list
#text = re.sub('[^a-z\ \']+', " ", text).lower
#text = list(text.split())
#print(text)

#create dictionary
#print(text)

#sort words into a list with no duplicates

#make a list of how many times words pop up using .count


#sort and print top 20 results
#pass tests
