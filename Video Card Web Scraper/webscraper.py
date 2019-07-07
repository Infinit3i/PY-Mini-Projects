import base64
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

pageSoup = soup(page_html, "html.parser")

videoCardContainers = pageSoup.findAll("div",{"class":"item-container"})

filename = "videoCardProducts.csv"
f = open(filename, "w")
headers = "brand, product_name, Shipping\n"
f.write(headers)

for videoCard in videoCardContainers:
    
    titleContainer = videoCard.findAll("a", {"class":"item-title"})
    productName = titleContainer[0].text

    brand = productName.split(" ")[0]

    shippingContainer = videoCard.findAll("li",{"class":"price-ship"})
    shipping = shippingContainer[0].text.strip()

    print("brand: " + brand)
    print("productName: " + productName)
    print("shipping: " + shipping)

    f.write(brand + "," + productName.replace(",", "|") + "," + shipping + "\n")

f.close()