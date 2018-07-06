#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request

def Post(post_url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
	req = urllib.request.Request(url=post_url, headers=headers)  
	response = urllib.request.urlopen(req)
	data =response.read().decode('UTF-8')
	return data