# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

def main():
    html = u'<div class="c">抱歉，未找到“中港矛盾”相关结果。<br/><div class="s"></div>请尝试更换关键词，再次搜索。<br/>查看<a href="/hotword/fav/">已关注的话题</a></div><div class="tip">热搜榜</div>'


    out_soup = BeautifulSoup(html)

    contain_wrong_div_list = out_soup.findAll('div', attrs={'class':'c'})

    for div_one in contain_wrong_div_list:
        print 'ff'
        if u"抱歉，未找到" in str(div_one.getText()):
            print 'a'


if __name__ == '__main__':
    main()
    pass