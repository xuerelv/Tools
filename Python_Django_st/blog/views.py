#coding=utf8
from django.http.response import HttpResponse
from django.template import loader,Context

'''
def index(req):
    loader_t = loader.get_template('index.html') 
    context_t = Context({})
    return HttpResponse(loader_t.render(context_t)) 
'''
from django.shortcuts import render_to_response

def index(req):
    params = {'title':'我的主页' ,'username':'(雪天)'}
    return render_to_response('index.html',params)