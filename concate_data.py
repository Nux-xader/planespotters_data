import time,  os
import pandas as pd


writer = pd.ExcelWriter("master_data.xlsx")
for n, path in enumerate(os.listdir("sub_data")[:4]):
	print(f" [{n+1}] Processing {path}")
	data = open("sub_data/"+path, "r").read()
	while " ; " in data or "; " in data or "; " in data:
		data = data.replace(" ; ", ";")
		data = data.replace("; ", ";")
		data = data.replace(" ;", ";")
	delmt_count = data.split("\n")[0].count(";")
	data_res = ""
	for x in data.split("\n")[1:]:
		if x.count(";") < delmt_count:
			for i in range(delmt_count-x.count(";")):
				x+=";"
		elif x.count(";") > delmt_count:
			x = x[:-int(x.count(";")-delmt_count)]

	open("sub_data/"+path, "w").write(data)
	df = pd.read_csv("sub_data/"+path, on_bad_lines='skip')
	df.to_excel(writer, sheet_name=path.split(".csv")[0], index=False)


writer.save()
