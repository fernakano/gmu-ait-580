import pandas as pd
import stocks
import nlp_filters as nlp
import time


def read_wsb():
    return pd.read_csv('datainputs/reddit_wsb.csv')
    # return pd.read_csv('datawork/reddit_wsb.csv')


def get_vader_wsb_training():
    return {
        'yolo': 100,
        'dd': 25,
        'double down': 25,
        'moon': 25,
        'dh': 20,
        'diamond hands': 20,
        'hold': 20,
        # Need to understand better the following ones
        'retarded': 20,  # in this case its a good thing looks like.
        'bullish': 10,
        'BTFD': 5,
        'FD': 5,
        'paper hands': -5,
        'bagholder': -5,
        'bearish': -10
    }


def main():
    df_wsb = read_wsb()

    # test of npl_filters
    # stock_dict_list = stocks.get_stock_dict()
    # vader = nlp.init(get_vader_wsb_training())
    # vader = nlp.setup_wsb_vader_lexicon()
    # scores = nlp.get_vader_polarity_scores(df_wsb, 'title')
    # scores_df = nlp.get_df_from_scores(scores)
    # scored_news = pd.concat([df_wsb['timestamp'], df_wsb['title'], df_wsb['body'], scores_df], axis=1)
    #
    # print("Vader Sentiment Analysis Complete!, finding stocks.....")
    #
    # wsb_post_stock = []
    # start = time.time()
    # NUMBER_POSTS=100
    # # scored_news = scored_news.head(NUMBER_POSTS)
    # # for index, row in scored_news.iterrows():
    # # for index, row in df_wsb.iterrows():
    #     print(index)
    #     wsb_post_stock.append(','.join(stocks.search_stock_on_sentence(row['title'])))
    # end = time.time()
    # print("Time Elapsed for stock search", end-start)
    # # scored_news['stock'] = wsb_post_stock
    # df_wsb['stock'] = wsb_post_stock
    # print(df_wsb)
    # # ten_scores = scored_news.head(NUMBER_POSTS)
    # # ten_scores['stock'] = wsb_post_stock
    # # print(ten_scores)

    # print("Vader Sentiment Analysis Complete!, finding stocks.....")

    wsb_post_stock = []
    start = time.time()
    # NUMBER_POSTS=100
    # scored_news = df_wsb.head(NUMBER_POSTS)
    scored_news = df_wsb
    for index, row in scored_news.iterrows():
        if index % 100 == 0:
            print(index)
            current = time.time()
            print("Current Time Elapsed for stock search", current - start)
        wsb_post_stock.append(','.join(stocks.search_stock_on_sentence(row['title'])))
    end = time.time()
    print("Time Elapsed for stock search", end - start)
    scored_news['stock'] = wsb_post_stock
    print(scored_news)
    scored_news.to_csv('datawork/reddit_wsb.csv')


if __name__ == "__main__":
    main()
