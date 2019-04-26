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

def compareOneParam(param, dataComp):
    for data in dataComp:
        if param.name == data.name:
            if (param.data == data.data):
                return True, None
            else:
                return False, data
    return False, None

def compare(firstData, secondData):
    for data in firstData:
        compRes, secData = compareOneParam(data, secondData)
        if not compRes:
            print('различия: ')
            print(data.name + " <====> " + data.data)
            if secData is not None:
                print(secData.name + " <====> " + secData.data)
            else:
                print('нет')

def parseFile(wordParse, howSkipFirst, howSkipEnd, data):
    data = re.split('<' + wordParse + ' name="|<' + wordParse + '-array name="|<plurals name="', data)
    data = data[howSkipFirst:]
    allDataStr = list()
    for i in range(len(data)):
        allDataStr.append(dataStr(
            re.split('">', data[i])[0],
            re.split('</' + wordParse + '>|</' + wordParse + '-array>', ''.join(re.split('">', data[i])[1:]))[0]))
    return allDataStr

if __name__ == '__main__':
    compare(parseFile('string', 1, 1,
                          loadFile('/home/azch/StudioProjects/AndroidSource/app/src/main/res/values-am/strings.xml')),
            parseFile('string', 1, 1,
                      loadFile('/home/azch/check.xml'))
            )



