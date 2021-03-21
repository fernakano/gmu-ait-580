import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()


# Instantiate the sentiment intensity analyzer with the existing lexicon
def setup_wsb_vader_lexicon(words={}):
    # Update the lexicon
    # New words and values
    new_words = {
        # usual journalist stock jargon
        'crushes': 10,
        'beats': 5,
        'misses': -5,
        'trouble': -10,
        'falls': -100,
    }

    new_words.update(words)
    vader.lexicon.update(new_words)
    return vader


def get_vader_polarity_scores(input_dataframe, column):
    return input_dataframe[column].apply(vader.polarity_scores)


def get_df_from_scores(vader_scores):
    return pd.DataFrame.from_records(vader_scores)


def init(vader_words={}):
    setup_wsb_vader_lexicon(vader_words)
    return vader


def main():
    print('nlp_filters')


if __name__ == "__main__":
    main()
