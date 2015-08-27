#coding:utf-8
'''
Created on 2015年8月10日

@author: Administrator
'''
def main_download_file():
    from urllib2 import urlopen
    url="http://www.gutenberg.org/cache/epub/2554/pg2554.txt"
    file_save = open("CRIME AND PUNISHMENT.txt",'a')
    raw = urlopen(url).read()
    for line in raw:
        file_save.write(line)
    pass

def main_2():
    from __future__ import division
    import nltk,re,pprint
    
    raw = open("CRIME AND PUNISHMENT.txt",'r')
    
    
    pass








if __name__ == '__main__':
    main_2()
    pass