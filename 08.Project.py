search_term = input("Enter search term:")
import requests
response = requests.get('https://www.usconstitution.net/const.txt')
filestring = response.text
filestringlist = filestring.split("\n")
while search_term != '':
    for i in range(len(filestringlist)):
        if filestringlist[i].find != -1:
            print(filestringlist[i])
            for j in range(-1,0, 1):
                if filestringlist[j] == "":
                    begin = j
                    break
            for a in range(-1, len(filestringlist)):
                if filestringlist[a] == "":
                    end = a
                    break
            for i in range (begin,end):
                print(filestringlist(i).format("Line:("")",begin,end))

search_term = input("Enter search term:")
