import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import collections
import re
import matplotlib
import matplotlib.pyplot as plt

def word_sorter(df_to_use):
    
    '''
    Input: 
        df_to_use: df of top clicked on tags in this case
    Output:
        sorted list of tuples representing key value pairs of word freq.
        
    Task:
        Goes through all tags and separates them into words.
        After, it will note their frequencies in descending order.
    '''
    
    # regular expression tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    # regex to get rid of non alphanumeric characters
    regex = re.compile('[^a-zA-Z]')
    
    # remove | delimiters as well as non-alphanumeric characters
    # combine words into one string
    words = []
    for word in df_to_use['tag']:
        word = regex.sub(' ', word)
        words.append(word.lower()) # lowercase as to avoid any case issues
    
    # join all words into one string
    words = ' '.join(words)
    
    # find all unique words 
    tokens = tokenizer.tokenize(words)
    print(str(len(tokens)) + " unique words")
    
    # remove stop words
    stop_words = set(stopwords.words('english'))
    
    # create al ist that does not contain stop words or numbers
    filtered_tag_tokens = []
    for word in tokens:
        if word not in stop_words:
            filtered_tag_tokens.append(word)
    print(str(len(filtered_tag_tokens)) + " unique non stopwords")
    
    # remove all words not in filtered tokens and remove all digits as well
    dic={}
    for word in words.split(" "):
        if word in filtered_tag_tokens and not word.isdigit():
            if word in dic:
                dic[word]=dic[word]+1
            else:
                dic[word]=1
                
    # sort words by number of occurences or frequency
    sorted_tag_words = sorted(dic.items(), key=lambda kv: (kv[1],kv[0]), reverse=True)
    return sorted_tag_words

#Bar Chart 
def word_frequency_graph(df_to_use, title, number_words):
    
    '''
    Input:
        df_to_use: the df we want to get our tags from to plot
        title: title name of plot
        number_words: number of most freq. words to plot
        
    '''
    
    # get first number_words from word_sorter
    words = word_sorter(df_to_use)[:number_words]
    count_words = []
    actual_word = []
    
    # make two lists of words representing the words and counts for plotting
    for word, count in words:
        count_words.append(count)
        actual_word.append(word)
    
    # plot code
    plt.figure(figsize=(number_words - 2, number_words - 2)) # figsize dynamically resizes with number_words
    plt.bar(actual_word, count_words, align='center', alpha=0.5)
    plt.ylabel('Frequency')
    plt.title(str(title) + ' Word Frequency')
    plt.tick_params(axis='x', which='major', pad=15)
    plt.xticks(rotation=45) # rotate tick labels to avoid overlapping
    
    plt.show()

# read dataset into pandas dataframe
df_items = pd.read_csv('items-Copy1.csv')

# print out top 5 rows
#print(df_items.head())

# df_clicks -> all items sorted in descending order by clicks
# most clicked on items are at the top
df_clicks = df_items.sort_values(by='clicks', ascending=False)

# let's see the top 10 clicked on tags
#print(df_clicks[['tag','clicks']].head(10))

# let's get the top 50 clicked on tags
top50_tags = df_clicks[['tag']].head(50)
#print(top50_tags)
    
dic = word_sorter(top50_tags)

#print(dic)

word_frequency_graph(top50_tags, 'Tags', 20)