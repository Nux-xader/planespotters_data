from bs4 import BeautifulSoup

data = str(open("ex.html", "r").read())
soup = BeautifulSoup(data, 'html.parser')
result = ""
for n, data in enumerate(soup.findAll(class_="dt-tr")):
    scnd_soup = BeautifulSoup(str(data), 'html.parser')
    data = scnd_soup.findAll(class_="dt-th" if n == 0 else "dt-td")
    for x in data:
        x = x.text
        while "  " in x or "\n" in x:
            x = x.replace("\n", "").replace("  ", " ")
        result+=f"{x};"
    result+="\n"

open("ex.csv", "w").write(result)