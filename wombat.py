#Wombat search
#Assignment 4
#Part C

#Imports 
import time
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from requests.api import get

#Empty list to store Image URLs
imgURL = []

#Time for benchmarking
startTime = time.perf_counter()

#URL where wombat photos are located
searchURL = "https://unsplash.com/s/photos/wombat"

#Scraping images by using bs4 and adding them to the imageURL list
page = requests.get(searchURL)
soup = BeautifulSoup(page.content, 'html.parser')
for image in soup.find_all('img', class_='YVj9w'):
    imgURL.append(image.get('src').strip())

imgURL = imgURL[:10]

#Method of writing the image file to PC. 
#Method can be passed into a map to use multiple threads 
def downloadImageToPC(image):
    imgName = image.split('/')[3]
    imgName = imgName.split('-')[2]
    imgName = f"{imgName}.jpg"
    imgContent = requests.get(image).content
    #context manager for downloading image
    with open(imgName, 'wb') as img:
        img.write(imgContent)
        print(f"{imgName} downloaded")

#Context Manager for Thread pool which executes the method and iterates over a list of URLs
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(downloadImageToPC, imgURL)

endTime = time.perf_counter()

#Printing out results
print("\n")
print(f"Total time taken = {round(endTime-startTime, 3)} seconds")

    


