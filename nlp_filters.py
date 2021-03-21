import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Instantiate the sentiment intensity analyzer with the existing lexicon
vader = SentimentIntensityAnalyzer()

# First import into a Dataframe
df_wsb = pd.read_csv('datainputs/reddit_wsb.csv')

# Update the lexicon
# New words and values
new_words = {
    'yolo': 100,
    'dd': 25,
    'double down': 25,
    'moon': 25,
    'dh': 20,
    'diamond hands': 20,
    'hold': 20,

    # Need to understand better the following ones
    'bullish': 10,
    'BTFD': 5,
    'FD': 5,

    'paper hands': -5,
    'bagholder': -5,
    'bearish': -10,

    # usual journalist stock jargon
    'crushes': 10,
    'beats': 5,
    'misses': -5,
    'trouble': -10,
    'falls': -100,
}
vader.lexicon.update(new_words)

# scores = df_wsb['body'].astype(str).apply(vader.polarity_scores)
scores = df_wsb['title'].apply(vader.polarity_scores)
scores_df = pd.DataFrame.from_records(scores)
scored_news =pd.concat([df_wsb['timestamp'],df_wsb['title'],df_wsb['body'], scores_df], axis=1)
print(scored_news)