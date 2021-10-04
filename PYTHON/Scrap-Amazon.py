import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os



def get_url(search_term):

	template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'

	search_term = search_term.replace(' ', '+')
	
	url = template.format(search_term)
	
	url += '&page{}'
	
	return url



def extract_record(item):

	try:
		atag = item.h2.a
	except AttributeError:
		return

	try:
		description = atag.text.strip()
	except AttributeError:
		return

	url = 'https://www.amazon.com' + atag.get('href')

	try:
		price_parent = item.find('span', 'a-price')
		price = price_parent.find('span', 'a-offscreen').text
	except AttributeError:
		return

	try:
		rating = item.i.text
		review_count = item.find('span', {'class': 'a-size-base'}).text
	except AttributeError:
		rating = ''
		review_count = ''

	result = (description, price, rating, review_count, url)

	return result



def main():

	search_term = input("Enter the product name to search for - ")

	driver = webdriver.Chrome(ChromeDriverManager().install())

	url = get_url(search_term)

	records = []


	for page in range(1, 21):

		driver.get(url.format(page))
		
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		
		results = soup.find_all('div', {'class', 's-result-item'})
		
		for item in results:
			
			record = extract_record(item)
			
			if record:
				records.append(record)


	driver.close()

	with open('Scrap-Amazon.csv', 'w', newline='', encoding='utf-8') as f:
		
		writer = csv.writer(f)
		
		writer.writerow(['Description', 'Price', 'Rating', 'Review Count', 'URL'])
		
		writer.writerows(records)


	os.startfile('Scrap-Amazon.csv')



main()
