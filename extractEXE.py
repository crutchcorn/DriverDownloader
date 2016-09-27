import os
for filename in os.listdir('.\drivers'):
     os.system(os.path.dirname(os.path.abspath(__file__)) + "\".\\drivers\\" + filename + "\" /VERYSILENT /DIR=\".\\extracted\\" + filename + "\"")
     #print(filename " + filename + ".e \"xe")


