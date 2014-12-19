# -*- coding: utf-8 -*-

import sys
import xbmcgui
import xbmcplugin

import urllib2

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

resp = urllib2.urlopen("http://vdn.live.cntv.cn/api2/liveHtml5.do?channel=pa://cctv_p2p_hdcctv13&client=html5")

data = resp.read().decode("utf-8")

url = data[data.index('"hls3":"') + 8:]
url = url[:url.index('"')]
url = url.replace("master.m3u8?b=100-300&", "index_500_av-p.m3u8?")

print(url)

li = xbmcgui.ListItem('CCTV-13 新闻', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
