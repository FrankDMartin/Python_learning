import os
import requests
from bs4 import BeautifulSoup

# 读取用户输入的主题
topic = input("Input the topic of pictures:")
url = "https://www.pexels.com/search/" + topic + "/"

# 向相关网址发起请求，将所有图片的原图网址存入一个列表中
url_code = requests.get(url)
soup = BeautifulSoup(url_code.content, "html.parser")
img_original_list = []
for img_url in soup.find_all(attrs={"class": "js-photo-link"}):
    if img_url["class"] == ['js-photo-link']:
        img_original_list.append("https://www.pexels.com" + img_url["href"])

# 向图片原图所在网址发送请求，并将网址存入列表
img_list = []
for img_url in img_original_list:
    code = requests.get(img_url)
    soup = BeautifulSoup(code.content, "html.parser")
    img_list.append(soup.find(attrs={"class": "btn btn-primary custom-size__submit"})["data-url"])

# 建立以主题命名的文件夹，并将图片存入其中
address = "D:\\" + topic
os.mkdir(address)
for img in img_list:
    img_name = img[img.rfind('/') + 1:]
    img_file = open(address + "\\" + img_name, 'wb')
    img_code = requests.get(img)
    img_file.write(img_code.content)
    img_file.close()
