import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_url(search_term):
	""" Generate a url for search term """

	template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
	search_term = search_term.replace(' ', '+')

	url = template.format(search_term)
	url += '&page={}'

	return url

def extract_record(item):
	""" Extract and return data from a single record """

	# Description and url
	atag = item.h2.a
	description = atag.text.strip()
	url_product = 'https://www.amazon.com'+atag.get('href')

	try:
		# Price
		price_parent = item.find('span', 'a-price')
		price = price_parent.find('span', 'a-offscreen').text
	except AttributeError:
		return 	

	try:
		# Rank and rating
		rating = item.i.text
		review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
	except AttributeError:
		rating = ''
		review_count = ''

	result = [description, price, rating, review_count, url_product]

	return result

def main(search_term):
	"""Main program"""

	options = Options()
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver.exe')

	records = []
	url = get_url(search_term)

	for page in range(1, 11):
		driver.get(url.format(page))
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		results = soup.find_all('div', {'data-component-type': 's-search-result'})

		for item in results:
			record = extract_record(item)
			if record:
				records.append(record)

	driver.close()

	print(f"{len(records)} results for '{search_term}'\n")

	dataframe = pd.DataFrame(records, columns=['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
	
	dataframe.to_excel('results_excel.xlsx', index=False)
	print('Results saved in a excel file: results_excel.xlsx')

	dataframe.to_csv('results_csv.csv', index=False)
	print('Results saved in a csv file: results_csv.csv')
	
search_term = str(input('Type the search term: ')).strip()
main(search_term)