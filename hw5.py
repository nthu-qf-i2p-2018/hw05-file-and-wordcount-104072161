
# coding: utf-8

# In[13]:


import csv
import json
import pickle
import string

def main(i_have_a_dream):
    lines =open('i_have_a_dream.txt').readlines()
    all_words = []
    for line in lines:
        words=line.split() 
        for word in words:
            word=word.strip(string.punctuation)
            if word!=(" "):
                all_words.append(word) 
    
    from collections import Counter
    word_counter=Counter(all_words)
    
    csv_file=open("word_count.csv","w")
    with open("word_count.csv","w")as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['word','count'])
        writer.writerows(word_counter.most_common())
       
    with open("wordcount.json","w")as json_file:
        json.dump(word_counter,json_file)
        
    with open("wordcount.pkl","wb")as pkl_file:
        pickle.dump(word_counter,pkl_file)
        
if __name__ == '__main_':
    main("i_have_a_dream.txt")


# In[12]:


main("i_have_a_dream.txt")

