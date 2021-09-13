#load necessary libraries
import requests
import os
from bs4 import BeautifulSoup

#Request URL from user & fetch URL
URL = input("Enter a URL to scrape")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#Only print text
text = soup.get_text()
print(text)

#Universal save path
#example: C:\Users\Username'
save_path = os.path.join(os.environ['USERPROFILE'], "Desktop")
#Create & write to txt file
file = open("output.txt", "w+")
file.write(text)
#close file
file.close()
