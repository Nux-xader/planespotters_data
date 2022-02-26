import time, os
from bs4 import BeautifulSoup

temp = "tempp.txt"
open(temp, "w").write("")
success, filed = 0, 0
for n, file in enumerate([i for i in open("temp.txt", "r").read().split("\n") if len(i) > 4]):
	time.sleep(0.15)
	print(f" [{n+1}] Converting {file}")
	path = "database/"+file
	try:
		data = str(open(path, "r", encoding="utf-8").read())
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

		open("sub_data/"+file.split(".html")[0]+".csv", "w", encoding="utf-8").write(result)
		success+=1
	except Exception as e:
		print(e)
		print(f" [!] [{n+1}] Filed Converting {file}")
		open(temp, "a").write(file+"\n")
		filed+=1

print(f" Total success converting : {success}")
print(f" Total filed converting : {filed}")