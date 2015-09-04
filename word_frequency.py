
#represent all text in sample.txt
import re

#convert text to all lower case
file = open('sample2.txt', 'r')
words = file.read().lower()
file.close()
#get rid of sentence structure and convert text file to a list
words = re.sub('[^a-z\ \']+', " ", words)
text = list(words.split())

#print(text)

#sort words into a list with no duplicates
unique_words = []
number = []
unique_words = sorted(set(text))
print(unique_words)
#make a list of how many times words pop up using .count
for number in unique_words:
    print(text.count(number), number)
