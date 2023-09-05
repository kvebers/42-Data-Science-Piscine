from table import load
import os


def extractTableNames(item):
    return [name[0:-4] for name in item]


def checkCSV(item):
    if (len(item) < 4):
        return False
    if (item[-4:] != ".csv"):
        return False
    return True


def main():
    path = "/goinfre/kvebers/subject/customer/"
    Files = os.listdir(path)
    TablesToAdd = [item for item in Files if checkCSV(item) is True]
    TableNames = extractTableNames(TablesToAdd)
    print(TableNames)
    for index, item in enumerate(TablesToAdd):
        newpath = path + TablesToAdd[index]
        print(newpath, item)
        load(newpath, TableNames[index])


if __name__ == "__main__":
    exit(main())