#-*- coding: UTF-8 -*- 。
import urllib2
from StringIO import StringIO
import gzip
import requests
from first_t.conf import get_proxy

def urlfetch(url):
        '''
        open the url and return html, may raise URLError
        '''
        HTTP_HEADERS= {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}
        request = urllib2.Request(url, headers=HTTP_HEADERS)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            #print 'gzip'
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
            return data
        else:
            return response.read()
    
def urlfetch_requests(url,str_proxy):
    cookies = get_cookie('weibo_login_cookies.dat')
    proxies = {"http": str_proxy}
    HTTP_HEADERS= {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0','Accept-encoding':'gzip'}
    reponse_h = requests.get(url,cookies=cookies ,proxies=proxies,headers=HTTP_HEADERS)
    if reponse_h.headers['content-type'] == 'gzip':
        buf = StringIO(reponse_h.text)
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        return data
    else:
        return reponse_h.text
    pass

def get_cookie(cookiefile):
    cookie = {}
    with open(cookiefile) as f:
        lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        space_index = line.find(' ')
        pair = line.split(';')[0][space_index:]
        pair = pair.replace('\"','')
        equal_index = pair.find('=')
        key = pair[:equal_index]
        value = pair[equal_index+1:]
        cookie[key] = value
    return cookie

def crawl_uid(uid,str_proxy):
    from  first_t import page_paser
#     url = 'http://weibo.com/' + uid + '/info'
    url = 'http://weibo.cn/' + uid + '/info'
#     html = urlfetch(url)
    html = urlfetch_requests(url,str_proxy)
    
#     print html
#     file_h = open(str(uid)+"_info.html",'a')
#     for line in html:
#         file_h.write(line)
    user_info = page_paser.parseer_phone_html(html)
    print user_info.to_string()
    return user_info
