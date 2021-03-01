import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt') #tokenizer

lemmatizer = WordNetLemmatizer()

df_nasdaq_list = pd.read_csv('nasdaqlisted.txt', delimiter='|')
# df_other_list = pd.read_csv('otherlisted.txt', delimiter='|')
# df_wsb = pd.read_csv('reddit_wsb.csv')
#
#
# df_nasdaq_list.describe()
# df_other_list.describe()
# df_wsb.describe()

y = df_nasdaq_list['Security Name'].iloc[0]
print(nltk.word_tokenize(y))
# x = lemmatizer.lemmatize(y)




# df_stocks = pd.concat(df_nasdaq_list, df_other_list)

# print(df_wsb)
# print(df_nasdaq_list)
# print(df_other_list)
# nltk.download([
#     "names",
#     "stopwords",
#     "state_union",
#     "twitter_samples",
#     "movie_reviews",
#     "averaged_perceptron_tagger",
#     "vader_lexicon",
#     "punkt",
# ])



# N = 10
# with open("reddit_wsb.csv") as f_wsb:
#     head = [next(f_wsb) for x in range(N)]
#     # for line in f_wsb:
#     #     print(line)
# print(head)
