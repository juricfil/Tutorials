from urllib.request import urlopen as uReq # za uzimanje stranice
from bs4 import BeautifulSoup as soup # za parsiranje HTMLa

# URL stranice koju scrapamo
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# otvaranje konekcije sa stranicom , preuzimanje stranice
uClient = uReq(my_url)
page_html=uClient.read()
uClient.close

#html parsiranje
page_soup=soup(page_html, "html.parser")


containers = page_soup.findAll("div",{"class":"item-container"})

# kreiranje csv fajla za pisanje 
filename = "products.csv"
f = open(filename,"w")
headers = "brand, product_name,shipping \n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li",{"li":"price-ship"})
	shipping_container[0].text.strip()

	print('brand' + brand)
	print('product_name' + product_name)
	print('shipping_container' + shipping_container)

	f.write(brand.replace(",","|")+","+product_name.replace(",","|")+","+shipping_container.replace(",","|") + "\n")

f.close()