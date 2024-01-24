from bs4 import BeautifulSoup
import requests
import random


def horoscope_API():
    sign = ""
    luck=""
    signs = {"aries": 1,"taurus": 2,"gemini": 3,"cancer": 4,"leo": 5,"virgo": 6,"libra": 7,"scorpio": 8,"sagittarius": 9,"capricorn": 10,"aquarius": 11,"pisces": 12, }
    #I added this block so el borj ye5ou we7ed random
    #if you want a specific sign ektebha fi "given_sign"
    L=["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
    given_sign = L[random.randint(0, len(L)-1)]
    #the rest of the code madabik 5aliha 3ala rou7ha juste bech yeb3ath request bech ye5ou el text w y7asnou
    URL = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + \
        str(signs[given_sign])
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find("p")
    sign = given_sign +"   "+ container.text.strip()
    return (sign)
print(horoscope_API())