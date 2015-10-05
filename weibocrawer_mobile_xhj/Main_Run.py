#-*- coding: utf-8 -*-

'''
Created on 2015-08-21

@author: xhj
'''
from craw_page_parse import crawl_real_time_with_keyword,\
    crawl_set_time_with_keyword
import os
import logging
import logging.config
import datetime

if not os.path.exists('logs/'):
    os.mkdir('logs')
curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) ) ) 
logging.config.fileConfig(curpath+'/runtime_infor_log.conf')

if not os.path.exists('data/'):
    os.mkdir('data')
if not os.path.exists('cookies/'):
    os.mkdir('cookies')


# 返回创建好的thread
def crawl_real_time_main(key_words_list):
    thrads_list = []
    for i in range(len(key_words_list)):
        thrads_list.append(crawl_real_time_with_keyword(key_words_list[i],'real_time_'+str(i)))
    return thrads_list

def crawl_set_time_main(key_word,start_time,end_time):
    thrads_list = []
    while start_time+datetime.timedelta(days=30) < end_time:
        end_2 = start_time+datetime.timedelta(days=30)
        thrads_list.append(crawl_set_time_with_keyword(key_word,start_time,end_2,'crawl_settime_thread'+str(start_time)+" to "+str(end_2)))
        start_time = end_2
    if start_time < end_time:
        thrads_list.append(crawl_set_time_with_keyword(key_word,start_time,end_time,'crawl_settime_thread'+str(start_time)+" to "+str(end_time)))
    return thrads_list

if __name__ == '__main__':
    all_thrads_list = []
    
#     key_words_list = ['滨海','香港','上海']
#     all_thrads_list.extend(crawl_real_time_main(key_words_list))
    
    key_word = ""
    start_time = datetime.datetime(2014, 1, 1)
    end_time = datetime.datetime(2015, 1, 1)
    all_thrads_list.extend(crawl_set_time_main(key_word, start_time, end_time))
    
    for thread in all_thrads_list:
        thread.start()
    for thread in all_thrads_list:
        thread.join()    


