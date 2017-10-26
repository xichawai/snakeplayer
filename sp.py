# -*- coding: utf-8 -*-
import logging
import requests
from lxml import etree
import re,sys
reload(sys)
sys.setdefaultencoding("utf-8")
class spider:
    def __init__(self,name):
        self.search_name=name
        self.search_url='http://www.soku.com/search_video/q_'+self.search_name
        self.video_entrace_url=''

    def get_entrace_url(self):
        r=requests.get(self.search_url).content
        tree=etree.HTML(r)
        try:
            video_url = tree.xpath("/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[4]/ul/li[1]/a/@href")[0]
            video_url = "http:"+video_url
            video_url = re.search(r'//(.*?)html',video_url).group()
        except:
            try:
                logging.info("excepte 1 content:   "+str(r))
                video_url = tree.xpath("/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[4]/div[1]/ul/li[1]/a/@href")[0]
            except:
                logging.info("excepte 1 content:   "+str(r))
            video_url = re.search(r'//(.*?)html',video_url).group()
        video_url = "http:"+video_url
        self.video_entrace_url = video_url
        print "video_entrace:  "+video_url

    def get_video_list(self):
        r=requests.get(self.video_entrace_url).content
        tree=etree.HTML(r)
        if "iqiyi" in self.video_entrace_url:
            r=requests.get(self.search_url).content
            tree=etree.HTML(r)
            temp =tree.xpath('/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div[1]/div[4]/ul/li/a/@href')
            video_list_url=[]
            for each in temp:
                each = re.search(r'//(.*?)html',str(each)).group()
                video_list_url.append(each)
            print "video_list_url:   ",str(video_list_url)
            return  video_list_url
        if "动漫" in str(self.get_tilte()[0].decode('utf-8')):
            print "heihei"
            video_list_url=tree.xpath('//*[@id="vpofficiallistv5_wrap"]/div[1]/div/div[1]/li/a/@href')
        else:
            video_list_url=tree.xpath('//*[@id="vpofficiallistv5_wrap"]/div[1]/div/div/div/a/@href')
        logging.info ("video_list_url:   "+str(video_list_url))
        logging.info (len(video_list_url))
        return video_list_url

    def get_poster(self):
        r=requests.get(self.search_url).content
        tree=etree.HTML(r)
        poster_url = tree.xpath("/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[1]/div[1]/img/@src")[0]
        poster_url = "http://" + poster_url
        print (poster_url)

    def get_tilte(self):
        r=requests.get(self.video_entrace_url).content
        tree=etree.HTML(r)
        title = tree.xpath("//*[@id=\"module_basic_title\"]/div[1]/h1/a/text()")
        print title[0].decode('utf-8')
        return title
