# coding=utf-8
import cookielib
import urllib2
import urllib
import base64
import re
import json
import rsa
import binascii
from first_t.conf import get_login_username_password, get_proxy
import sys
import time
import requests

def get_pwd_rsa(pwd, servertime, nonce):
    """
        Get rsa2 encrypted password, using RSA module from https://pypi.python.org/pypi/rsa/3.1.1, documents can be accessed at 
        http://stuvel.eu/files/python-rsa-doc/index.html
    """
    #n, n parameter of RSA public key, which is published by WEIBO.COM
    #hardcoded here but you can also find it from values return from prelogin status above
    weibo_rsa_n = 'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'
    
    #e, exponent parameter of RSA public key, WEIBO uses 0x10001, which is 65537 in Decimal
    weibo_rsa_e = 65537
   
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(pwd)
    
    #construct WEIBO RSA Publickey using n and e above, note that n is a hex string
    key = rsa.PublicKey(int(weibo_rsa_n, 16), weibo_rsa_e)
    
    #get encrypted password
    encropy_pwd = rsa.encrypt(message, key)

    #trun back encrypted password binaries to hex string
    return binascii.b2a_hex(encropy_pwd)


def get_user(username):
    username_ = urllib.quote(username)
    username = base64.encodestring(username_)[:-1]
    return username

def get_prelogin_status(username):
    """
    Perform prelogin action, get prelogin status, including servertime, nonce, rsakv, etc.
    """
    #prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&client=ssologin.js(v1.4.5)'
    prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=' + get_user(username) + \
     '&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.5)';
    data = urllib2.urlopen(prelogin_url).read()
    p = re.compile('\((.*)\)')
    
    try:
        json_data = p.search(data).group(1)
        data = json.loads(json_data)
        servertime = str(data['servertime'])
        nonce = data['nonce']
        rsakv = data['rsakv']
        return servertime, nonce, rsakv
    except:
        return None

def do_login(username,pwd,cookie_file):
    login_data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        'pagerefer':'',
        'vsnf': '1',
        'su': '',
        'service': 'miniblog',
        'servertime': '',
        'nonce': '',
        'pwencode': 'rsa2',
        'rsakv': '',
        'sp': '',
        'encoding': 'UTF-8',
        'prelt': '45',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
        }

    cookie_jar2     = cookielib.LWPCookieJar()
    cookie_support2 = urllib2.HTTPCookieProcessor(cookie_jar2)
    opener2         = urllib2.build_opener(cookie_support2, urllib2.HTTPHandler)
    urllib2.install_opener(opener2)
    login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)'
    try:
        servertime, nonce, rsakv = get_prelogin_status(username)
    except:
        return 0
    
    #Fill POST data
    login_data['servertime'] = servertime
    login_data['nonce'] = nonce
    login_data['su'] = get_user(username)
    login_data['sp'] = get_pwd_rsa(pwd, servertime, nonce)
    login_data['rsakv'] = rsakv
    login_data = urllib.urlencode(login_data)
    http_headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}
    req_login  = urllib2.Request(
        url = login_url,
        data = login_data,
        headers = http_headers
    )
    result = urllib2.urlopen(req_login)
    text = result.read()
    
    
    p = re.compile('location\.replace\(\'(.*?)\'\)')
    
#     print text
#     print p.search(text).group(1)
    try:
        #Search login redirection URL
        login_url = p.search(text).group(1)
        
        data = urllib2.urlopen(login_url).read()
        
        #Verify login feedback, check whether result is TRUE
        patt_feedback = 'feedBackUrlCallBack\((.*)\)'
        p = re.compile(patt_feedback, re.MULTILINE)
        
        feedback = p.search(data).group(1)
        
        feedback_json = json.loads(feedback)
        if feedback_json['result']:
            cookie_jar2.save(cookie_file,ignore_discard=True, ignore_expires=True)
            return 1
        else:
            return 0
    except:
        return 0

def get_uid():
    uid_file = open('out_uid_unique.txt')
    for line in uid_file:
        list_line = line.split(' ')
        if str(list_line[-1]).endswith('\n'):
            list_line[-1] = list_line[-1][:-1]
        if list_line[-1]=='':
            list_line = list_line[:-1]
        for uid in list_line:
            return uid            

if __name__ == '__main__':
    from first_t import crawl_page
    cookie_file = "weibo_login_cookies.dat"

    user_info_file = open("user_info_file.txt","a")
    uid_file = open('out_uid_unique.txt')
    
#     do_login("xuerenlv@163.com", "xxx", cookie_file)
    
    count_uid = 0
    pre = -1
    for line in uid_file:
        list_line = line.split(' ')
        if str(list_line[-1]).endswith('\n'):
            list_line[-1] = list_line[-1][:-1]
        if list_line[-1]=='':
            list_line = list_line[:-1]
        for uid in list_line:
            
            if count_uid<= 143490:
                count_uid = count_uid+1
                continue
#############################
            print count_uid
            i_num = count_uid/36
            str_proxy = ""
            t = i_num%6
            if not t==pre:
                pre =  t
                user_name,password = get_login_username_password(t)
                print user_name
                do_login(user_name, password, cookie_file)
            str_proxy = get_proxy((i_num%9)+1)
#             print uid
            try:
                user_info = crawl_page.crawl_uid(uid,str_proxy)
            except requests.exceptions.ConnectionError:
                try:
                    user_info = crawl_page.crawl_uid(uid,str_proxy)
                except requests.exceptions.ConnectionError:
                    print "proxy error"
                    continue
                    pass
                pass

            write_str = "[uid:"+uid+"]"+user_info.to_string()+"\n"
            user_info_file.write(write_str)
            
            count_uid = count_uid+1
            if count_uid >= 160001:
                user_info_file.flush()
                sys.exit()
                
     
    user_info_file.flush()
    user_info_file.close()
    pass