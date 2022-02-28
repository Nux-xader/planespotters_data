import time, os

temp = "tempp.txt"
open(temp, "w").write("")
success, filed = 0, 0

# for n, file in enumerate([i for i in open("temp.txt", "r").read().split("\n") if len(i) > 4]):
for n, file in enumerate(os.listdir("res_multi_page")):
    time.sleep(0.15)
    print(f" [{n+1}] Converting {file}")
    path = "res_multi_page/"+file
    try:
        data = str(open(path, "r", encoding="utf-8").read())
        result = ""
        for x in data.split("\n"):
            if len(x) < 3: continue
            while "  " in x or "\n" in x:
                x = x.replace("\n", "").replace("  ", " ")
            result+=f"{x};\n"

        open("multi/"+file, "w", encoding="utf-8").write(result)
        success+=1
    except Exception as e:
        print(e)
        print(f" [!] [{n+1}] Filed Converting {file}")
        open(temp, "a").write(file+"\n")
        filed+=1

print(f" Total success converting : {success}")
print(f" Total filed converting : {filed}")