# coding=utf-8
from bs4 import BeautifulSoup
import re
import json
from first_t import model_userinfo

def parseer_phone_html(html,weibo_user_type=1001):
    user_info = model_userinfo.UserInfo()
    bs_all = BeautifulSoup(html)
    div_all = bs_all.findAll('div', attrs={'class':'c'})
    for div in div_all:
        for str_in in str(div.getText(u'\n')).split(u'\n'):
            en_str = str_in.encode('utf-8')
            
            if(en_str.startswith(u"昵称")):
                user_info.nickname = en_str[en_str.find(':')+1:]
            elif(en_str.startswith(u"地区")):
                user_info.location = en_str[en_str.find(':')+1:]
            elif(en_str.startswith(u"性别")):
                user_info.sex = en_str[en_str.find(':')+1:]
            elif(en_str.startswith(u"生日")):
                user_info.birth = en_str[en_str.find(':')+1:]
            elif(en_str.startswith(u"简介")):
                user_info.intro = en_str[en_str.find(':')+1:]
            elif(en_str.startswith(u"认证信息")):
                print en_str.find(u':')
                user_info.check_or_not = u'是'
                user_info.check_info = en_str
    return user_info 

if __name__ == '__main__':
    html = open('phone_html.txt').read()
    user_info = model_userinfo.UserInfo()
#     user_info = parse_user_profile(html)
    user_info = parseer_phone_html(html)
    print user_info.to_string()
    pass
