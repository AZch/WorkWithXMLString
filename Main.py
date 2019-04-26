import re

class dataStr():

    def __init__(self, name, data):
        self.name = name
        self.data = data


def loadFile(path):
    file = open(path, 'r')
    strRes = ''
    for line in file:
        strRes += line
    return strRes


if __name__ == '__main__':
    fileMy = loadFile('/home/azch/StudioProjects/AndroidSource/app/src/main/res/values-am/strings.xml')
    fileMy = re.split('<string name="|">', fileMy)
    fileMy = fileMy[1:]
    name = ""
    data = ""
    allDataStr = list()
    for i in range(len(fileMy)):
        if name == "":
            name = fileMy[i]
        elif data == "":
            data = re.split('</string>', fileMy[i])[0]
            allDataStr.append(dataStr(name, data))
            name = ""
            data = ""

    print(re.split('<string name="|">', fileMy))