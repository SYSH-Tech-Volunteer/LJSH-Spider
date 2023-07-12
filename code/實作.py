from bs4 import BeautifulSoup
import requests
url = "https://ljjhs.tc.edu.tw/p/403-1080-1244-1.php?Lang=zh-tw"
titles_list = []
links_list = []
dates_list = []
response = requests.get(url).text
soup = BeautifulSoup(response, 'html5lib')
tbody = soup.find('tbody') #6
a_tag_list = tbody.find_all('a')
for a_tag in a_tag_list:
    links_list.append(a_tag.get('href')) 
    titles_list.append(a_tag.get('title')) 
td_tag_list = tbody.find_all('td', attrs={"data-th" : "日期"}) 
for td_tag in td_tag_list:
    div = td_tag.find("div")
    dates_list.append(div.text.strip())
for title in titles_list:
    print (title)
for link in links_list:
    print (link)