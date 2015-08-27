#-*- coding: utf-8 -*-

'''
Created on 2015-08-21

@author: xhj
'''
from Queue import Queue
import threading


class URL_Queue():
    
    url_queue = Queue;
    url_queue_mutex = threading.Lock()
    
    def __init__(self):
        pass
    
    def get_url(self):
        URL_Queue.url_queue_mutex.acquire()
        url = URL_Queue.url_queue.get()
        URL_Queue.url_queue_mutex.release()
        return url
    
    def add_one_url(self,url):
        URL_Queue.url_queue_mutex.acquire()
        URL_Queue.url_queue.put(url)
        URL_Queue.url_queue_mutex.release()
    
    def add_list_url(self,url_list):
        URL_Queue.url_queue_mutex.acquire()
        for url in url_list:
            URL_Queue.url_queue.put(url)
        URL_Queue.url_queue_mutex.release()