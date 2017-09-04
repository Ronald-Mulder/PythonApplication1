import sys
import os
import shutil
import commands
import urllib2
from PIL import Image
import requests
from StringIO import StringIO

def main():
  """
  hoofdfunctie die 
  als eerste gestart wordt! erg handig!
  """
  if len(sys.argv) > 1:
    print 'Hello there', sys.argv[1]
  else:
    print 'Python \n' + str(sys.version).lower()[-45:len(sys.version)]
    #os.mkdir("c:/temp/ronald")
  
    

  #f = open('c:/temp/pythonfiletest.txt', 'a')
  #f.write('Ronald\n')
  #f.write('Henk')
  #f.close()
  #shutil.copy('c:/temp/pythonfiletest.txt','c:/temp/pythonfiletest.txt.backup')
  #sys.stderr.write("Foutje bedankt!\n")

  #wget('http://www.geon.nl');
  url = 'https://geon.nl/wp-content/uploads/2016/02/bedrijfsfotografiegeonmuruelleoldenburger-0572-e1456149973673.jpg'
  response = requests.get(url)
  img = Image.open(StringIO(response.content))
  img.save('c:/temp/bert.jpg')

def wget(url):
  ufile = urllib2.urlopen(url)  ## get file-like object for url
  info = ufile.info()   ## meta-info about the url content
  if info.gettype() == 'text/html':
    print 'base url:' + ufile.geturl()
    text = ufile.read()  ## read all its text
    print text

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()