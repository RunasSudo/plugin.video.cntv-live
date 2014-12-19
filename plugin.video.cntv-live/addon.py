# -*- coding: utf-8 -*-

import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import urllib2

addon = xbmcaddon.Addon(id="plugin.video.cntv-live")
addon_path = xbmc.translatePath(addon.getAddonInfo("path"))
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, "movies")

def addStream(channelID, channelName):
	resp = urllib2.urlopen("http://vdn.live.cntv.cn/api2/liveHtml5.do?channel=pa://cctv_p2p_hd" + channelID + "&client=html5")
	data = resp.read().decode("utf-8")

	url = data[data.index('"hls3":"') + 8:]
	url = url[:url.index('"')]
	url = url.replace("master.m3u8?b=100-300&", "index_500_av-p.m3u8?")

	li = xbmcgui.ListItem(channelName, iconImage=addon_path + "/resources/media/" + channelID + ".png")
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addStream("cctv1", "CCTV-1 综合")
addStream("cctv2", "CCTV-2 财经")
addStream("cctv3", "CCTV-3 综艺")
addStream("cctv4", "CCTV-4 (亚洲)")
addStream("cctveurope", "CCTV-4 (欧洲)")
addStream("cctvamerica", "CCTV-4 (美洲)")
addStream("cctv5", "CCTV-5 体育")
addStream("cctv6", "CCTV-6 电影")
addStream("cctv7", "CCTV-7 军事农业")
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

xbmcplugin.endOfDirectory(addon_handle)
