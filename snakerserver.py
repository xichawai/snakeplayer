#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import logging
import sys
import sp


app = Flask(__name__)
reload(sys)
sys.setdefaultencoding("utf-8")

@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.get_data()
        dict = json.loads(a)
        logging.info(dict['name'])
        logging.info(dict['ep'])
        spider = sp.spider(dict['name'])
        spider.get_entrace_url()
        video_list=[]
        video_list=spider.get_video_list()
        return video_list[dict['ep']]


if __name__ =='__main__':
    #logging.basicConfig(filename='myapp.log', level=logging.INFO)
    #logging.info('Started')
    app.run('#',port=2013,debug=True)
