import urllib.request
import re
import ast
from sys import exit

def getDriverList(url):
    opened = urllib.request.urlopen(url)

    listo = []
    line = re.findall(r'"Name":.*?"URL":.*?,', str(opened.read()))
    for i in line:
        collection = []
        thing = re.sub(r',|\{|\}', '\n', i)
        for uh in thing.split('\n'):
            ta = re.sub(r'^(?!.*("Name"|"URL")).*\s*', '', uh)
            if not ta == '':
                collection.append(ta)
        listo.append(collection)
        collection = []

    drivers = []
    for items in listo:
        if not '\"' in items[-2:][0][-1:]:
        	item2 = items[-2:][0] + '\"' # Kludge for any string that have `,` in `"Name"`
        else:
        	item2 = items[-2:][0]
        drivers.append(ast.literal_eval("{" + item2 + ", " + items[len(items)-2:][1] + "}"))

    return drivers