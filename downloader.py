from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import click

#FILES_PER_DOWNLOAD=25
#OLD_URL_FILE='old-tmp.txt'

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-n', '--num-per-download', default=25, help='The number of files to download at once.')
@click.option('-o', '--output-path', default='downloads', help='The name of the folder to store the downloaded files.')
def main(input_file, num_per_download, output_path):
	#print('Input File:', input_file)
	#print('# Per Download:', num_per_download)
	#print('Output Path:', output_path)
	old_file = open(input_file, 'r')
	urls = old_file.readlines()
	old_file.close()
	url_file_name = input_file+'.tmp'
	url_file = open(url_file_name, 'w')

	chrome_options = Options()
	chrome_options.add_argument("--headless")
	#chrome_driver = os.getcwd() +"/chromedriver"
	chrome_driver = "/usr/lib/chromium-browser/chromedriver"
	#driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
	driver = webdriver.Chrome(options=chrome_options)

	i = 0
	for url in urls:
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		link = soup.find(id="dlbutton")
		if link is None:
			print("Error! Most likely file expired.")
			break
		print(urljoin(url, link.get('href')))
		url_file.write(urljoin(url, link.get('href')) + "\n")
		if i == num_per_download:
			url_file.close()
			os.system('aria2c -d "'+output_path+'" -i '+url_file_name)
			i = 0
			url_file = open(url_file_name, 'w')
		else:
			i += 1

	driver.close()
	driver.quit()
	url_file.close()
	os.system('aria2c -d "'+output_path+'" -i '+url_file_name)
	os.remove(url_file_name)

if __name__ == '__main__':
	main()
