#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>



import addonHandler
import gui
import wx
import config

addonHandler.initTranslation()

## Translators: message box when user is installing the addon in NVDA and an older version prevents the update to be done.
oldaddonmsg = _("""An older version of this addon has been detected.
This prevents the installation to be completed.
Please uninstall the previous version before proceeding with the Lambda addon setup.
""")

## Translators: message box when user is installing the addon in NVDA and a "lambda" profile is already present. 
profilefoundmsg = _("""Another profile named "lambda" is already present in your NVDA configuration. 
This prevents the addon on create and configure the lambda profile correctly.
If you want the addon to configure a lambda profile for you, please delete the old one named "lambda" using the NVDA "Configuration Profiles" dialog.
The new profile will be created the next time you'll start the Lambda app.
Otherwise please edit your profile configuration file manually.
""")

def onInstall():
	if "Lambda" in [a.name for a in addonHandler.getRunningAddons()] :
		gui.messageBox(oldaddonmsg)
		raise Exception("Old version prevents the update.")
	
	try :
		if config.conf._getProfile("lambda") :
			gui.messageBox(profilefoundmsg)
	except : return
    
