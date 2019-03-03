import os

def clearAll():
    os.system("rm -rf ./title.txt ./body.txt ./author.txt")

def writeTitle(data: str):
    with open("./title.txt", "w") as f:
        f.write(data)
        f.close()