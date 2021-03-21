This repository will have the code for the AIT-580 final project.

to install the current code, you need Python 3, to install dependencies you can run  
`pip install -r /path/to/requirements.txt`

There are 3 main files

`pipeline.py` - where the main logic is currently running

`stocks.py` - helper to find stocks in sentence 
            and to get stock performance history from YAHOO

`nlp_filters` - currently doing basic sentiment analysis, we may want to 
add the filter for positive and negative 