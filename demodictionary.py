import requests
from bs4 import BeautifulSoup
n=input("Enter the word\n")
link="https://en.wikipedia.org/wiki"+"/"+str(n)
r=requests.get(link)
c=r.content
soup=BeautifulSoup(c,'html.parser')
for i in range(30):
    try:
     all=soup.find_all("p")[i].text
     print(all)
    except:
        print("")
