from bs4 import BeautifulSoup
import requests
hamropatro_url='https://www.hamropatro.com/rashifal'

get_data=requests.get(url=hamropatro_url)
print(get_data)

data_rashifal=BeautifulSoup(get_data.content)
print(data_rashifal.prettify)

rashifals=data_rashifal.find_all("div",attrs={"class":"item"})
print(rashifals)

for rashifal in rashifals:
    print(f"Rashi:{rashifal.h3.text}")
    print(f"Rashifal:{rashifal.p.text}")
    
rashi_dictionary={}
for rashifal in rashifals:
    rashi_dictionary[rashifal.h3.text]=rashifal.p.text
    print(rashi_dictionary)
    
mine_rashi = [
    {
        "name": "Isu Sharma",
        "rashi": "धनु"
    },
    {
        "name": "Aaditya Kafle",
        "rashi": "बृश्चिक"
    }
]

print(mine_rashi)

for me in mine_rashi:
    zodiac=me["rashi"]
    today_rashi=rashi_dictionary[zodiac]
    body=f"Dear {me["name"]}....your todays rashi is:{today_rashi}"
    print(body)
    

    