import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://demo.videocdn.scaleengine.net/comtelcanada-iphone/play/comtelcanada/playlist.m3u8'
li = xbmcgui.ListItem('Watch Living Faith Church Live!', iconImage='icon.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)



