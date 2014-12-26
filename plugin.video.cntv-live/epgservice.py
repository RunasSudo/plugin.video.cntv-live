import xbmc
import xbmcaddon

addon = xbmcaddon.Addon(id="plugin.video.cntv-live")
addon_path = xbmc.translatePath(addon.getAddonInfo("path"))

def doUpdate():
	print("Updating EPG")
	
	try:
		#Update EPG
		print("TRY!")
	except Exception as e:
		print(traceback.format_exc())
	
	#Set a timer for the next update
	xbmc.executebuiltin("AlarmClock({0},RunScript({1}),{2},True)".format("EPGUpdate", addon_path + "/epgservice.py", 10)) #10 minutes

if __name__ == '__main__':    
	doUpdate()
