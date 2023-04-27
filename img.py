from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup


import requests
import io
from PIL import Image
import os

category = input("Enter image category: ")
url = 'https://unsplash.com/s/photos/'+ category
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
page_src = driver.page_source

soup = BeautifulSoup(page_src,'lxml')

element_card = soup.find_all('img', class_='tB6UZ a5VGX')
image_links = []
for item in element_card:
    image_links.append(item['src'])

def download_img(download_folder,image_links):
    file_name = 1
    for url in image_links:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)

        image_name = category+str(file_name)+(".jpg")
        file_name+=1
        file_path = download_folder+image_name
        

        
        with open(file_path,'wb') as f:
            image.save(f, "JPEG")
        


if not os.path.exists("./"+category):
    print("creating folder")
    os.mkdir("./"+category)
    path = category+"/"
else:
    print("folder already exist")
    path = category+"/"

download_img(path,image_links)