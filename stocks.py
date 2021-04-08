from os import path
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz

# Get Stock History from Yahoo Finance
import yfinance as yf


def stock_file_create():
    if not path.exists('datawork/stocks.csv'):
        df_nasdaq_list = pd.read_csv('datainputs/nasdaqlisted.txt', delimiter='|')
        df_other_list = pd.read_csv('datainputs/otherlisted.txt', delimiter='|')
        df_other_list.rename(columns={'ACT Symbol': 'Symbol'}, inplace=True)
        stocks = pd.concat([df_nasdaq_list[['Symbol', 'Security Name']],
                            df_other_list[['Symbol', 'Security Name']]])
        stocks['Security Name'] = stocks['Security Name'].str.upper()
        stocks.to_csv('datawork/stocks.csv', index=False, sep='|', quotechar='"')
    else:
        stocks = pd.read_csv('datawork/stocks.csv', delimiter='|')
    return stocks


def fuzzy_search(list_of_dicts, query, threshold):
    query = query.upper()
    scores = []
    for index, item in enumerate(list_of_dicts):
        values = list(list_of_dicts[item].split(' '))
        ratios = [fuzz.ratio(str(query), str(value)) for value in values]  # ensure both are in string
        # ratios = [fuzz.ratio(str(query), str(value)) for index, value in values]  # ensure both are in string
        scores.append({"index": index, "score": max(ratios)})

    filtered_scores = [item for item in scores if item['score'] >= threshold]
    sorted_filtered_scores = sorted(filtered_scores, key=lambda k: k['score'], reverse=True)
    filtered_list_of_dicts = [list_of_dicts[item["index"]] for item in sorted_filtered_scores]
    return filtered_list_of_dicts


def return_results_partial(list_of_dicts, query, threshold):
    query = query.upper()
    scores = []
    for index, item in enumerate(list_of_dicts):
        values = list(item.values())
        ratios = [fuzz.partial_ratio(str(query), str(value)) for value in values]  # ensure both are in string
        scores.append({"index": index, "score": max(ratios)})

    filtered_scores = [item for item in scores if item['score'] >= threshold]
    sorted_filtered_scores = sorted(filtered_scores, key=lambda k: k['score'], reverse=True)
    filtered_list_of_dicts = [list_of_dicts[item["index"]] for item in sorted_filtered_scores]
    return filtered_list_of_dicts


def search_stock(mydict, word):
    word_striped = word.upper().replace(" ", "")
    val = mydict.get(word_striped, None)
    if val is not None:
        return [word_striped]
    if not val:
        val = list(
            filter(lambda item: f' {word_striped.upper()} ' in f' {str(mydict[item]).upper()} ', mydict))
    # if not val:
    #     val = fuzzy_search(mydict, word, 80)
    return val


def search_stock_on_sentence(sentence):
    list_stock = []
    sentence = sentence.lower()
    sentence = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,']", "", sentence)
    stop_words = set(stopwords.words('english'))

    for word in nltk.word_tokenize(sentence):
        if word not in stop_words:
            stock = search_stock(get_stock_dict(), word)
            if stock is not None:
                list_stock.extend(stock)
    return list_stock


def get_stock_dict():
    stocks = stock_file_create()
    return dict(zip(stocks['Symbol'], stocks['Security Name']))
    # return stocks.to_dict('records')


def get_stock_hist_data(stock_key):
    msft = yf.Ticker(stock_key)
    # get stock info
    msft.info
    # get historical market data
    return msft.history(period="max")


def main():
    print("Create Full Stock List")
    stock_dict_list = get_stock_dict()
    sentence = 'Not to distract from GME, just thought our AMC and BlackBerry or Microsoft'
    # print('Looking for sentence: ')
    # print('->', sentence)
    # sentence = sentence.lower()
    # sentence = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
    # stop_words = set(stopwords.words('english'))
    #
    # for word in nltk.word_tokenize(sentence):
    #     if word not in stop_words:
    #         stock = search_stock(stock_dict_list, word)
    #         if stock is not None:
    #             print(word, stock)
    #             print(get_stock_hist_data(stock))

    print(search_stock_on_sentence(sentence))


if __name__ == "__main__":
    main()
