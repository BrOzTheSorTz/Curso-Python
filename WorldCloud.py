#pip install wordcloud
#pip install fileupload
#pip install ipywidgets


import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display




with open("TextProyect.txt") as f:
    lines= f.readlines()
text = "".join(lines)

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    def create_dictionary(punctuations,uninteresting_words):
        #We allow to the user to change the punctuations and unisteresting words along the time
        
       
        
        words = file_contents.lower().split()
        
        words_copy = words.copy()
        
        #First of al we need to eliminate the punctuations from the words
        index =0
        for word in words:
            for punctuation in punctuations:
                if punctuation in word:
                    #We need to delete this punctuation
                    #We use replace(letter, x) we replace letter with x 
                    words_copy[index] = words_copy[index].replace(punctuation,'')
                    
            index +=1
            
        words = words_copy
        #Secondly, we eliminate the uninteresting words
        index =0
        for wrong_word in uninteresting_words:
            for word in words:
                if wrong_word == word:
                    words_copy.remove(word)
       
        words = words_copy
        
        #Thirdly we count the words
        frequency={}
        for word in words:
            if word not in frequency:
                #We start with one because there is a word since we just found it
                frequency[word]=1
            frequency[word] +=1
            
        return frequency
                            
    #wordcloud
    dict = create_dictionary(punctuations,uninteresting_words)
    
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict)#Entre los paréntiesis va el diccionario
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(text)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()