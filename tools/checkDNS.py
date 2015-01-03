#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-

import socket

timeout_s = 1.0
retry = 2

def checkURL(hostname, address):
	conn = socket.create_connection(address, timeout_s)
	conn.close()
	print("{0} -> {1} (SUCC)".format(hostname, address[0]))

def checkAllURLs(hostname):
	addrinfos = socket.getaddrinfo(hostname, 80)
	for addrinfo in addrinfos:
		if addrinfo[1] == socket.SOCK_STREAM:
			
			address = addrinfo[4]
			
			for i in range(0, retry):
				try:
					checkURL(hostname, address)
					break
				except socket.timeout:
					if i >= retry - 1:
						print("{0} -> {1} (FAIL)".format(hostname, address[0]))

def addStream(channelID, channelName):
	checkAllURLs(channelID + ".vtime.cntv.cloudcdn.net")

addStream("cctv1", "CCTV-1 综合")
addStream("cctv2", "CCTV-2 财经")
addStream("cctv3", "CCTV-3 综艺")
addStream("cctv4", "CCTV-4 (亚洲)")
addStream("cctveurope", "CCTV-4 (欧洲)")
addStream("cctvamerica", "CCTV-4 (美洲)")
addStream("cctv5", "CCTV-5 体育")
addStream("cctv6", "CCTV-6 电影")
addStream("cctv7", "CCTV-7 军事 农业")
addStream("cctv8", "CCTV-8 电视剧")
addStream("cctvjilu", "CCTV-9 纪录")
addStream("cctvdoc", "CCTV-9 纪录(英)")
addStream("cctv10", "CCTV-10 科教")
addStream("cctv11", "CCTV-11 戏曲")
addStream("cctv12", "CCTV-12 社会与法")
addStream("cctv13", "CCTV-13 新闻")
addStream("cctvchild", "CCTV-14 少儿")
addStream("cctv15", "CCTV-15 音乐")
addStream("cctv9", "CCTV-NEWS")
addStream("cctv5plus", "CCTV体育赛事")
