#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import socket
import sys
import traceback
import urllib.parse
import urllib.request
try:
	import simplejson as jsonimpl
except ImportError:
	import json as jsonimpl

timeout_s = 2.0
retry = 2

def checkURL(url, hostname, address):
	req = urllib.request.Request(url)
	req.add_header("Host", hostname)
	
	conn = urllib.request.urlopen(req, timeout=timeout_s)
	conn.read()
	
	print("{0} -> {1} (SUCC)".format(hostname, address))

def checkAllURLs(url):
	hostname = urllib.parse.urlparse(url).netloc
	
	addrinfos = socket.getaddrinfo(hostname, 80)
	for addrinfo in addrinfos:
		if addrinfo[1] == socket.SOCK_STREAM:
			
			address = addrinfo[4][0]
			
			for i in range(0, retry):
				try:
					checkURL(url.replace(hostname, address), hostname, address)
					break
				except Exception:
					if i >= retry - 1:
						print("{0} -> {1} (FAIL)".format(hostname, address))

def addStream(channelID, channelName):
	resp = urllib.request.urlopen("http://vdn.live.cntv.cn/api2/live.do?channel=pa://cctv_p2p_hd" + channelID)
	data = resp.read().decode("utf-8")
	jsondata = jsonimpl.loads(data)
	url = jsondata["hls_url"]["hls4"]
	url = url.replace("vtime.cntv.cloudcdn.net:8000", "vtime.cntv.cloudcdn.net")
	
	checkAllURLs(url)

#checkURL("localhost", "127.0.0.1:8000")

#addStream("cctv1", "CCTV-1 综合")
#addStream("cctv2", "CCTV-2 财经")
#addStream("cctv3", "CCTV-3 综艺")
#addStream("cctv4", "CCTV-4 (亚洲)")
##addStream("cctveurope", "CCTV-4 (欧洲)")
##addStream("cctvamerica", "CCTV-4 (美洲)")
##addStream("cctv5", "CCTV-5 体育")
##addStream("cctv6", "CCTV-6 电影")
##addStream("cctv7", "CCTV-7 军事 农业")
#addStream("cctv8", "CCTV-8 电视剧")
##addStream("cctvjilu", "CCTV-9 纪录")
##addStream("cctvdoc", "CCTV-9 纪录(英)")
##addStream("cctv10", "CCTV-10 科教")
##addStream("cctv11", "CCTV-11 戏曲")
##addStream("cctv12", "CCTV-12 社会与法")
#addStream("cctv13", "CCTV-13 新闻")
##addStream("cctvchild", "CCTV-14 少儿")
##addStream("cctv15", "CCTV-15 音乐")
##addStream("cctv9", "CCTV-NEWS")
##addStream("cctv5plus", "CCTV体育赛事")
