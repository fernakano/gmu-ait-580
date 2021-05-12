This repository will have the code for the AIT-580 final project.

to install the current code, you need Python 3, to install dependencies you can run  
`pip install -r /path/to/requirements.txt`

There are 3 main files

`pipeline.py` - where the main logic is currently running

`stocks.py` - helper to find stocks in sentence 
            and to get stock performance history from YAHOO

`nlp_filters` - currently doing basic sentiment analysis, we may want to 
add the filter for positive and negative '

/datainputs contain all data we used
/dataoutput contain all data that we had as a result of our analisys
/datawork contain all intermediate data used for processing
/notebook contain our notebooks used for BERT analysis.
pipeline.py uses the datainput to tag the stocks and output result to datawork

after that with the tagged data we processed the BERT code on top of this data for sentiment analisys.
