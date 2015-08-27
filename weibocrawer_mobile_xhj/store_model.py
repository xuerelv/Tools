# -*- coding: utf-8 -*-


'''
Created on 2015-08-21

@author: xhj
'''
from mongoengine.connection import connect
from config_operation import DB_HOST, DB_PORT, DBNAME
from mongoengine.document import Document
from mongoengine.fields import StringField


class SingleWeibo():
    
    def __init__(self,uid,nickname,is_auth,user_url,weibo_url,content,praise_num,retweet_num,comment_num,creat_time,all_weibo_num):
        self.uid = uid
        self.nickname = nickname
        self.is_auth = is_auth
        self.user_url = user_url
        self.weibo_url = weibo_url
        self.content = content
        
        self.praise_num = praise_num
        self.retweet_num = retweet_num
        self.comment_num = comment_num
        
        self.creat_time = creat_time
        self.all_weibo_num = all_weibo_num
        
    def to_string(self):
        return self.uid+'\t'+self.nickname+'\t'+self.is_auth+'\t'+self.weibo_url+'\t'+self.user_url+'\t'+\
            self.content+'\t'+self.praise_num+'\t'+self.retweet_num+'\t'+self.comment_num+'\t'+self.creat_time+'\t'+self.all_weibo_num
            
            



#############################   存到mongodb   #############################################
connect(DBNAME, host=DB_HOST, port=int(DB_PORT))
class Single_weibo_store(Document):
    uid = StringField()
    nickname = StringField()
    is_auth = StringField()
    user_url = StringField()
    weibo_url = StringField(unique=True)
    content = StringField()
        
    praise_num = StringField()
    retweet_num = StringField()
    comment_num = StringField()
        
    creat_time = StringField()
    all_weibo_num = StringField()