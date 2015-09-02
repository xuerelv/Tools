# -*- coding: utf-8 -*-

try:
	import sys
	import yaml

except ImportError:
	print >> sys.stderr
	sys.exit()

try:
	conf_file = open("weibosearch.yaml", 'r')
	conf_dic = yaml.load(conf_file)
	conf_file.close()
except:
	try:
		conf_file = open("../weibosearch.yaml", 'r')
	except:
		print 'weibo.yaml not found'

	conf_dic = yaml.load(conf_file)
	conf_file.close()

def get_login_username_password(i_num):
	return conf_dic['login'][int(i_num)]['username'],conf_dic['login'][int(i_num)]['password']

def get_proxy(i_num):
	return conf_dic['proxies'][i_num][i_num+1]

if __name__ == '__main__':	
	conf_dic = yaml.load(conf_file)
	print conf_dic['proxies']
	print conf_dic['login']
	name,pas = get_login_username_password(10)
	print type(name)
	print type(pas)
	print str(name)+str(pas)
	print get_proxy(9)
	conf_file.close()


