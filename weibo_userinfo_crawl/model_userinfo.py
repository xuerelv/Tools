# coding=utf-8

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

class UserInfo():
    
    def __init__(self):
        pass
    
    nickname = ""
    location = ""
    sex = ""
    birth = ""
    intro = ""
    check_or_not = u"否"
    check_info = ""
    
    def print_self(self):
        print    "info:"+self.nickname
        print    "info:"+self.location 
        print    "info:"+self.sex 
        print    "info:"+self.birth 
        print    "info:"+self.intro 
        print "[是否验证：" + self.check_or_not+"]"


    def to_string(self):
        return "[昵称：" + self.nickname + "]" + "[所在地：" + self.location + "]" + "[性别：" + self.sex + "]"+ "[是否验证：" + self.check_or_not + "]"+ "[" + self.check_info + "]"+"[生日：" + self.birth + "]"+"[简介：" + self.intro + "]"
