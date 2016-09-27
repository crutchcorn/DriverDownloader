from urllib.request import Request, urlopen
import re
import ast
from sys import exit
import codecs

def getDriverList(url):
    opened = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    opened = urlopen(opened)

    opened = re.sub(r'[^\x00-\x7F]+',' ', opened.read().decode('utf-8'))
    opened = re.sub(r'<a id="down"', '\n', opened)
    opened = re.findall('(.*(7x86|AllNT).*\n)', opened)

    drivers = []

    for i in opened:
        i = re.sub('.*href="', '', str(i))
        i = re.sub('".*', '', i)
        if re.match('^(?!(http://drivers.drp.su)).*\s*', i) is None: 
            i = re.sub('.*', '{"URL":"\g<0>"},', i)
            drivers.append(ast.literal_eval(i[:-1]))

    return drivers