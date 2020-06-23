from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/')

soup=BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.write(csv_file)
csv_writer.writerow(['headline', 'summary', 'video-link'])

for article in soup.find_all('article')

	headline = article.h2.a.text
	print(headline)
	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	try:
		vid_src = artivle.find('iframe', class_='youtube-player')['src']

		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'

	except Exception as e:
		yt_link = None

	csv_write.writerow([headline,summary,yt_link])

csv_file.close()