from bs4 import BeautifulSoup
import requests
import csv

url = 'http://www2.copasa.com.br/servicos/qualidadeagua/pesqtel.asp?letra=D&cidade=443&periodoInicial=01%2F2019&periodoFinal=04%2F2020'
html = requests.get(url)
soup = BeautifulSoup(html.text)
tables = soup.select("#mesames table")

for table in tables:
    headers = [th.text.encode("utf-8") for th in table.select("tr th")]
    with open("out.csv", "a") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(
            [
                [td.text.encode("utf-8") for td in row.find_all("td")]
                for row in table.select("tr + tr")
            ]
        )
