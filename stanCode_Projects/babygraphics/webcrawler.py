"""
File: webcrawler.py
Name: Alice Chiu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #
        # Male amount
        male = 0
        female = 0
        male_numbers = ""
        female_numbers = ""
        tags = soup.find_all('table', {'class': 't-stripe'})
        for tag in tags:
            tbodys = tag.find_all('tbody')
            for tbody in tbodys:
                trs = tbody.find_all('tr')
                for tr in trs:
                    tds = tr.find_all('td')
                    if len(tds) > 4:
                        male += string_manipulate(tds[2])
                        female += string_manipulate(tds[4])

        print('Male Number: ' + str(male))
        print('Female Number: ' + str(female))


def string_manipulate(td):
    ans = ""
    for ch in td:
        for i in range(len(ch)):
            if ch[i].isdigit():
                ans += ch[i]
    return int(ans)


if __name__ == '__main__':
    main()
