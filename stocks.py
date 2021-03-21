from os import path

import pandas as pd
from fuzzywuzzy import fuzz


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
        values = list(item.values())
        ratios = [fuzz.ratio(str(query), str(value)) for value in values]  # ensure both are in string
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


def search_in_values(mydict, word):
    word_striped = word.upper().replace(" ", "")
    val = list(filter(lambda item: item['Symbol'] == word, mydict))
    if not val:
        val = list(
            filter(lambda item: word_striped.upper() in str(item['Security Name']).upper().replace(" ", ""), mydict))
    if not val:
        val = fuzzy_search(mydict, word, 40)
    if val:
        return val[0]['Symbol']


def main():
    print("Create Full Stock List")
    stocks = stock_file_create()
    stock_dict_list = stocks.to_dict('records')
    # stock_dict_list_strip = [{key: str(value).rsplit('. ')[0].replace(" ", "") for key, value in e.items()} for e in
    #                          stock_dict_list]

    # print(stock_dict_list)
    results = search_in_values(stock_dict_list, 'Black Berry')
    # print(results2)
    print(results)


if __name__ == "__main__":
    main()
