# Amazon-Web-Scraper
A Web Scraper to find products on amazon.com that stores the description, price, rating, review count and url of each product in .csv and .xlsx files.

## How to use it?
You must install selenium and webdriver for your browser. Learn more in <a href="https://selenium-python.readthedocs.io/installation.html">selenium docs</a>.

### Libraries to install with pip
```python
pip install seleinum # To use webdriver
````
```python
pip install pandas # To convert the results to a pandas dataframe and then convert to .csv and .xlsx files
````
```python
pip install bs4 # To use BeautifulSoup (library for pulling data out of HTML and XML files)
````

### Usage

<img src="https://github.com/mateusvictor/Amazon-Web-Scraper/blob/main/screenshot.jpg" width="600" height="400">

The results are saved in the same folder as the script in excel and csv formats. Result example in csv format: <a href="https://github.com/mateusvictor/Amazon-Web-Scraper/blob/main/results_csv.csv">results_csv</a>.
