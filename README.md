# ScrapyTests

## Installation of the environment with conda

For the moment, Scrapy only works with Python2, so create a python2 environment:

    $ conda create -n py2 python=2
    $ source activate py2

For windows, just drop the 'source' before activate.

Install scrapy. -c stands for channel

    $ conda install -c scrapinghub scrapy

For windows, we have to install pywin32 as well:

    $ conda install pywin32

Start a scrapy project:

    $ scrapy startproject Scrapy

This creates the basic directory structure. Then we create a spider in the spiders directory, like the example.py file. To run it:

    $ scrapy crawl tripadv -o out.json

