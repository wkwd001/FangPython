import requests
from bs4 import BeautifulSoup

class FangData():

    def __init__(self):
        self.url = "http://esf.nanjing.fang.com/house1-j058-k06691/c2150-d2250-j2110-k2200-t21-l3110/"
        self.baseUrl = "http://esf.nanjing.fang.com"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Host': 'esf.nanjing.fang.com'}
        response = requests.get(self.baseUrl, headers=headers)
        response.encoding = 'gbk'
        content = BeautifulSoup(response.text, 'lxml')

        linkblock = content.find('div', class_="houseList")
        self.linklist = linkblock.find_all('dl', class_="list rel")

    def printli(self):
        linklist = self.linklist
        linksum = list()

        for link in linklist:
            linkForTitle = link.find('p', class_="title")
            subUrl = linkForTitle.a.get('href')
            title = linkForTitle.a.get('title')
            infoForHouse = link.find('p', class_="mt12").get_text().replace(' ', '').replace("\r", "").replace("\n", "")
            addressInfo = link.find('p', class_="mt10")
            housingEstate = addressInfo.a.get('title')
            housingAddress = link.find('span', class_="iconAdress ml10 gray9").get_text()
            areaMeasure = link.find('div', class_="area alignR").get_text().replace(' ', '').replace("\r", "").replace( "\n", "")
            price = link.find('div', class_="moreInfo").get_text().replace(' ', '').replace("\r", "").replace("\n", "")
            image = link.img.get('src2')

            linksum.append((image,title, infoForHouse, housingEstate,housingAddress,areaMeasure,price,self.baseUrl + subUrl))
        return linksum