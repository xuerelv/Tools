#encoding=utf-8
import urllib2
from StringIO import StringIO
import gzip
import requests
from first_t.conf import get_proxy
from werkzeug.urls import Href

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

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


def crawl_keyword_comment_url(crawl_keyword,str_proxy,page_index):
    url = ""
    if page_index == 0:
        url = "http://weibo.cn/search/mblog?hideSearchFrame=&keyword="+crawl_keyword
    else:
        url = "http://weibo.cn/search/mblog?hideSearchFrame=&keyword="+crawl_keyword+"&page="+str(page_index)
    html = urlfetch_requests(url,str_proxy)
    from bs4 import BeautifulSoup
    out_soup = BeautifulSoup(html)
    out_a = out_soup.findAll('a', attrs={"class":"cc"})
    file_h = open("query_result_comment_url.txt",'a')
    for a_cc in out_a:
        num_str = a_cc.contents[0][a_cc.contents[0].find('[')+1:a_cc.contents[0].find(']')]
        num = int(num_str)
        if not num==0:
            line_str = "["+str(a_cc['href']) +"]"+"["+str(num)+"]"
            print str(line_str)+str(page_index)
            file_h.write(line_str+'\n')
#             print str(a_cc['href']) +"   "+"["+str(num)+"]"
 
    
#     print html
#     file_h = open("query_result.html",'a')
#     for line in html:
#         file_h.write(str(line).encode("utf-8"))
    pass

def crawl_keyword_comment(url,str_proxy,page_num):
    url = url[0:-7] + "&page="+str(page_num)
    print url
    html = urlfetch_requests(url,str_proxy)
    from bs4 import BeautifulSoup
    out_soup = BeautifulSoup(html)
#     print html
    span_ctt = out_soup.findAll('span', attrs={"class":"ctt"})
    file_h = open("comment.txt",'a')
    for i in range(len(span_ctt)):
        if(i==1):
            print "xhj---------"+str(span_ctt[i].contents[0])
        file_h.write(str(span_ctt[i].contents[0])+'\n')
#         print span_in.contents[0]
    
    pass