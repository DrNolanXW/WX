#!C:\Python27\Python.exe
# -*- coding=UTF-8 -*-
import cgi
import cgitb
import web
import os
import sys
import codecs
import hashlib
import base64
import requests
import time
import urlparse
import demjson

import urllib
import urllib2

from wechatpy import parse_message
from wechatpy import create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

from pytesseract import *
from PIL import Image



smartisanM1_ppt="http://pan.baidu.com/s/1mhELU2G  gwiw"
welcome="Welcome to the WeChat ID"
universally="http://pan.baidu.com/s/1sljJPZR    h133"
java="https://pan.baidu.com/s/1miLNGVm     skp2"
XML='https://pan.baidu.com/s/1cEaChg      564s'
Computer_Organization='https://pan.baidu.com/s/1o8nTFMq    jn8n'
OS='https://pan.baidu.com/s/1eR8S2Wy    qb7d'
ele='https://pan.baidu.com/s/1cwzDZw     zxk3'
javaweb='https://pan.baidu.com/s/1c1BEzLI     XFVY'


def check_signature():
    print "Content-Type: text/html"
    query_string = os.environ.get("QUERY_STRING")
    arguments = urlparse.parse_qs(query_string) 
    signature = arguments['signature'][0] 
    timestamp = arguments['timestamp'][0] 
    nonce = arguments['nonce'][0]
    echostr=arguments['echostr'][0]
    token="wx123"
    list=[token,timestamp,nonce]
    list.sort()
    sha1=hashlib.sha1()
    map(sha1.update,list)
    hashcode=sha1.hexdigest()
    if hashcode == signature:
        return echostr


def tulin_reply(info):
    json_info=info
    json_key="c21ca585439844618f87f96832d52684"
    requrl="http://www.tuling123.com/openapi/api"
    data={'key':json_key,'info':json_info}
    data_urlencode=urllib.urlencode(data)
    req=urllib2.Request(url=requrl,data=data_urlencode)
    res_data=urllib2.urlopen(req)
    res=res_data.read()
    res_json=demjson.decode(res)
    try:
        res_url=res_json['url']
        return res_json['text']+res_json['url']
    except KeyError:
        return res_json['text']


def post_content():
    body_text=sys.stdin.read()
    msg=parse_message(body_text)
    #content_txt=msg.content.encode('utf-8')
    if msg.type=='text':
        info=msg.content.encode('utf-8')
        xml_info=tulin_reply(info)
        reply=create_reply('Text:'+xml_info,message=msg)
        return reply
    #elif msg.event=='subscribe':
        #reply=create_reply('Text:'+msg.content.encode('utf-8'),message=msg)
        #return reply
    elif msg.type=='image':
        return reply_verification(msg)


def reply_resource_api(msg):
    content_txt=msg.content.encode('utf-8')
    if msg.content=='M1ppt':
        return reply_resource(msg,smartisanM1_ppt)
    elif msg.content=='other':
        return reply_resource(msg,universally)
    elif msg.content=='java':
        return reply_resource(msg,java)
    elif msg.content=='XML':
        return reply_resource(msg,XML)
    elif msg.content=='CO':
        return reply_resource(msg,Computer_Organization)
    elif msg.content=='OS':
        return reply_resource(msg,OS)
    elif msg.content=='E':
        return reply_resource(msg,ele)
    elif msg.content=='javaweb':
        return reply_resource(msg,javaweb)
    elif content_txt[:6]=='encode':
        txt=base64.b64encode(content_txt[6:])
        return reply_encode64(msg,txt)
    elif content_txt[:6]=='decode':
        txt=base64.b64decode(content_txt[6:])
        return reply_encode64(msg,txt)


def reply_text(msg):
    reply=create_reply('Text:'+msg.content.encode('utf-8'),message=msg)
    return reply


def reply_resource(msg,url):
    reply=create_reply(url,message=msg)
    return reply


def reply_encode64(msg,txt):
    reply=create_reply(txt,message=msg)
    return reply


def reply_verification(msg):
    try:
        r=requests.get(msg.image)
        #urlname='url.txt'
        #file_object=open(urlname,'w')
        #file_object.write(msg.image+'\r\n')
        #file_object.close()
        filename='image/'+str(int(time.time()))+".jpg"
        with open(filename,'wb') as f:
            f.write(r.content)
        #image=Image.open(filename)
        #txt=pytesseract.image_to_string(image)
        txt=verification_img(filename)
        reply=create_reply("result:"+txt,message=msg)
        return reply
    except:
        reply=create_reply('error',message=msg)
    return reply


def verification_img(filename):
    image=Image.open(filename)
    imgry=image.convert('L')
    threshold=140
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    out=imgry.point(table,'1')
    txt=pytesseract.image_to_string(out)
    txt=txt.strip()
    return txt

#reload(sys)
#sys.setdefaultencoding('utf8')
print "Content-Type: text/html"
print ''
cgitb.enable(format='txt')
reply=''
txt=''
print post_content()

