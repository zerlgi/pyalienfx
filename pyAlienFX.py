#!/usr/bin/python

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import usb
import platform
import sys,os
from copy import *
import time





class AlienFXProperties:
	def __init__(self):
		self.isDebug = False
		
		self.AUTHOR = "Blondel Leo"
		
		#Application info
		self.ALIEN_FX_VERSION = "pre alpha"
		self.ALIEN_FX_APPLICATION_RAW_NAME = "pyAlienFX"
		self.ALIEN_FX_APPLICATION_NAME = self.ALIEN_FX_APPLICATION_RAW_NAME +" "+ self.ALIEN_FX_VERSION
		
		#java properties
		self.PROPERTY_OS_NAME = platform.platform()
		self.USER_HOME = os.path.expanduser('~')
		self.JAVA_ARCHITECTURE = platform.machine()
		
		#used properties
		self.arch = platform.machine()
		self.userHomePath = os.path.expanduser('~')
		self.osName = sys.platform
		
		#OS checks
		self.WINDOWS_OS = "Windows"
		self.isWindows = self.isWindows()

		#native libraries
		self.ALIENFX_NATIVE_LIBRARY_NAME = "Alien"
		self.ALIENFX_NATIVE_LIBRARY = self.ALIENFX_NATIVE_LIBRARY_NAME+self.arch
		
		#powermodes and region ids
		self.ALIEN_FX_DEFAULT_POWER_MODE = ""
		self.POWER_BUTTON_ID = "PB"
		self.POWER_BUTTON_EYES_ID = "PBE"
		self.MEDIA_BAR_ID = "MB"
		self.TOUCH_PAD_ID = "TP"
		self.ALIEN_LOGO_ID = "AL"
		self.ALIEN_HEAD_ID = "AH"
		self.LEFT_SPEAKER_ID = "LS"
		self.RIGHT_SPEAKER_ID = "RS"
		self.LEFT_CENTER_KEYBOARD_ID = "LCK"
		self.LEFT_KEYBOARD_ID = "LK"
		self.RIGHT_CENTER_KEYBOARD_ID = "RCK"
		self.RIGHT_KEYBOARD_ID = "RK"
		
		self.ON_BATTERY_ID = "BAT"
		self.CHARGING_ID = "CH"
		self.AC_POWER_ID = "AC"
		self.STANDBY_ID = "SB"
		
	def isWindows(self):
		if self.WINDOWS_OS in platform.platform():
			return True
		return False
		
class AlienFXPowerMode:
	def __init__(self, name, description, block):
		self.description = description
		#self.blockId = block
		self.name = name

class AlienFXRegion:
	def __init__(self, name, description, regionId, maxCommands, canBlink, canMorph, canLight, supportedModes):
		self.description = description
		self.regionId = regionId
		self.name = name
		self.canLight = canLight
		self.canBlink = canBlink
		self.canMorph = canMorph
		self.maxCommands = maxCommands
		self.supportedModes = supportedModes

class AlienFXTexts:
	def __init__(self):
		#errors:
		self.ALIEN_FX_ERROR_TITLE_TEXT = "AlienFX error"
		self.DATA_LENGTH_ERROR_FORMAT = "Data length should be %d but was %d"
		self.DEVICE_NOT_PRESENT_ERROR_TEXT = "The application was unable to communicate with the alienFX device. The device is either not present, or the application lacks sufficient rights to access the device"
		self.COMMUNICATION_ERROR_FORMAT = "Error occured while trying to communicate with the AlienFX device: %s\n"
		self.DEVICE_PERMISSION_ERROR_TEXT = "The Device was found, but the application was unable to communicate with the alienFX controller. Do you have the right to access the alienfx device(e.g. are you running as admin)"
		self.SYSTEM_UI_NOT_FOUND = "System UI not Found"
		self.PROFILE_EXISTS_ERROR_TEXT = "Profile with that name already exists"
		self.PROFILE_NAME_EMPTY_ERROR_TEXT = "Name cannot be empty"
		self.SAVE_PROFILE_ERROR_FORMAT = "Failed to save the Profile: %s\n"
		self.ALREADY_RUNNING_ERROR_TEXT = "AlienFX is already running"
		
		#warnings
		self.ALIEN_FX_WARNING_TITLE_TEXT = "AlienFX Warning"
		self.SYSTEM_TRAY_WARNING_TEXT = "It seems the system does not support system trays. The Application will not run in background."
		
		#info messages
		self.ALIEN_FX_INFO_TITLE_TEXT = "AlienFx Info"
		self.SHOW_ALIEN_FX_LITE_TEXT = "Show AlienFXLite"
		self.ALIEN_FX_BACKGROUND_TEXT = "Still running in the background"
		self.ENTER_NAME_TITLE_TEXT = "Enter Name"
		self.ENTER_NAME_TEXT = "Enter a name for the new profile"
		self.USAGE_TITLE = "Usage"
		self.USAGE = "The Application is very similar in use as the AlienFX application developed by Alienware. \nFirst, create a new profile. Then you can select the colors for the given regions of your computer. \nAdding an action (Color, Blink, Morph) is done by pressing one of the small dropdown buttons.\nTo copy paste a given sequence of actions, just select the actions by pressing on the section they are in, and drag the mouse over them.\n Additionally, one can use modifiers such as shift and control to modify the way in which selection behaves. \nTo paste the selected section, click on the add button and then select the paste icon (the last one).\n Additionally, one can easily change the colors of profile by selecting a new color and pressing on a color in the Color used panel.\n This will change all actions with the color pressed on, to the selected color. \nPressing with the right mouse button on any color button or action will result in selecting that color.\nFinally, if you get weird behaviour, reset the AlienFX device by pressing on the Reset button under the help menu"
		self.ABOUT_FORMAT = "AlienFX Lite %s developed by %s"
		self.ABOUT_TITLE = "About"
		self.HELP_TITLE = "Help"
		self.RESET_TITLE = "Reset AlienFx"
		
		
		#Events
		self.EVENT_TURN_OFF_ALL = "Turn off AlienFX"
		self.EVENT_TURN_OFF_ALL_BUT_KEYBOARD = "Turn off All but Keyboard"
		self.EVENT_TURN_OFF_KEYBOARD = "Turn off keyboard"
		
		#controls
		self.EXIT_TEXT = "Exit"
		self.PREVIEW_LABEL_TEXT = "Preview"
		self.SELECT_PROFILE_TEXT = "Please select a profile from the combobox or create a new one"
		
		self.APPLY_THE_CURRENT_PROFILE = "Apply the current Profile"
		self.DELETE_THE_CURRENT_PROFILE = "Delete the current Profile"
		self.SAVE_THE_CURRENT_PROFILE = "Save the current Profile"
		self.CREATE_A_NEW_PROFILE = "Create a new Profile"
		self.PREVIEW_TOOL_TIP = "Preview Colors on AlienFX"
		
		self.PROFILE_SPEED_TEXT = "Speed:"
		self.COLORS_PROFILE_TITLE = "Colors Used in Profile"
		self.DEFAULT_TEXT = "Default"
		self.COLORS_TEXT = "Colors"
		self.PROFILE_TEXT = "Profile"
		
		self.PROFILE_SPEED_SLOW = "Slow"
		self.PROFILE_SPEED_FAST = "Fast"
		
		self.ACTION_COLOR_TEXT = "Color"
		self.ACTION_BLINK_TEXT = "Blink"
		self.ACTION_MORPH_TEXT = "Morph"
		

		self.DEFAULT_PROFILE_TEXT = "Default Profile"
		
		#Alienware devices:
		self.POWER_BUTTON_DESCRIPTION = "Power Button"
		self.ALIENWARE_POWERBUTTON_EYES_DESCRIPTION = "Powerbutton Eyes"
		self.MEDIA_BAR_DESCRIPTION = "Media Bar"
		self.TOUCHPAD_DESCRIPTION = "Touchpad"
		self.ALIENWARE_LOGO_DESCRIPTION = "Alienware logo"
		self.ALIENWARE_HEAD_DESCRIPTION = "Alienware head"
		self.LEFT_SPEAKER_DESCRIPTION = "Left Speaker"
		self.RIGHT_SPEAKER_DESCRIPTION = "Right Speaker"
		self.LEFT_CENTER_KEYBOARD_DESCRIPTION = "Left Center Keyboard"
		self.LEFT_KEYBOARD_DESCRIPTION = "Left Keyboard"
		self.RIGHT_CENTER_KEYBOARD_DESCRIPTION = "Right Center Keyboard"
		self.RIGHT_KEYBOARD_DESCRIPTION = "Right Keyboard"
		self.KEYBOARD_DESCRIPTION = "Keyboard"
		

		self.STEALTH_MODE_DESCRIPTION = "Stealth Mode"
		self.LID_CLOSED_DESCRIPTION = "Closed Lid"
		self.ON_BATTERY_DESCRIPTION = "On Battery"
		self.CHARGING2_DESCRIPTION = "Charging"
		self.AC_POWER_DESCRIPTION = "AC Power"
		self.STAND_BY_DESCRIPTION = "StandBy"

class M11xR3:
	def __init__(self):
		self.AlienFXProperties = AlienFXProperties()
		self.AlienFXTexts = AlienFXTexts()
		self.regions = {}
		self.suportedMode = {}
		
		#Define Alienware M11x Device Control
		self.STATE_BUSY = 0x11
		self.STATE_READY = 0x10
		self.STATE_UNKNOWN_COMMAND = 0x12
			
		self.SUPPORTED_COMMANDS = 15
		self.COMMAND_END_STORAGE = 0x00 # = End Storage block (See storage)
		self.COMMAND_SET_MORPH_COLOR = 0x01# = Set morph color (See set commands)
		self.COMMAND_SET_BLINK_COLOR = 0x02# = Set blink color (See set commands)
		self.COMMAND_SET_COLOR = 0x03# = Set color (See set commands)
		self.COMMAND_LOOP_BLOCK_END = 0x04# = Loop Block end (See loops)
		self.COMMAND_TRANSMIT_EXECUTE = 0x05# = End transmition and execute
		self.COMMAND_GET_STATUS = 0x06# = Get device status (see get device status)
		self.COMMAND_RESET = 0x07# = Reset (See reset)
		self.COMMAND_SAVE_NEXT = 0x08# = Save next instruction in storage block (see storage)
		self.COMMAND_SAVE = 0x09# = Save storage data (See storage)
		self.COMMAND_BATTERY_STATE = 0x0F# = Set batery state (See set commands)
		self.COMMAND_SET_SPEED = 0x0E# = Set display speed (see set speed)
			
		self.RESET_TOUCH_CONTROLS = 0x01
		self.RESET_SLEEP_LIGHTS_ON = 0x02
		self.RESET_ALL_LIGHTS_OFF = 0x03
		self.RESET_ALL_LIGHTS_ON = 0x04
			
		self.DATA_LENGTH = 9
			
		self.START_BYTE = 0x02
		self.FILL_BYTE = 0x00
			
		self.BLOCK_LOAD_ON_BOOT = 0x01
		self.BLOCK_STANDBY = 0x02
		self.BLOCK_AC_POWER = 0x05
		self.BLOCK_CHARGING = 0x06
		self.BLOCK_BAT_POWER = 0x08
			
		self.REGION_RIGHT_KEYBOARD = 0x0001 
		self.REGION_RIGHT_SPEAKER = 0x0020 
		self.REGION_LEFT_SPEAKER = 0x0040
		self.REGION_ALIEN_NAME = 0x0100 
		self.REGION_MEDIA_BAR = 0x0800
		self.REGION_POWER_BUTTON = 0x6000
		
		self.suportedMode["normal"] = AlienFXPowerMode(self.AlienFXProperties.ALIEN_FX_DEFAULT_POWER_MODE,self.AlienFXProperties.ALIEN_FX_DEFAULT_POWER_MODE, self.BLOCK_LOAD_ON_BOOT),
		self.suportedMode["standby"] = AlienFXPowerMode(self.AlienFXProperties.STANDBY_ID, self.AlienFXTexts.STAND_BY_DESCRIPTION, self.BLOCK_STANDBY),
		self.suportedMode["acPower"] = AlienFXPowerMode(self.AlienFXProperties.AC_POWER_ID, self.AlienFXTexts.AC_POWER_DESCRIPTION, self.BLOCK_AC_POWER),
		self.suportedMode["charging"] = AlienFXPowerMode(self.AlienFXProperties.CHARGING_ID, self.AlienFXTexts.CHARGING2_DESCRIPTION, self.BLOCK_CHARGING),
		self.suportedMode["onBat"] = AlienFXPowerMode(self.AlienFXProperties.ON_BATTERY_ID, self.AlienFXTexts.ON_BATTERY_DESCRIPTION, self.BLOCK_BAT_POWER)
		
		self.regions[self.AlienFXProperties.RIGHT_KEYBOARD_ID] = AlienFXRegion(self.AlienFXProperties.RIGHT_KEYBOARD_ID, self.AlienFXTexts.KEYBOARD_DESCRIPTION, self.REGION_RIGHT_KEYBOARD,self.SUPPORTED_COMMANDS,True,True,True, self.suportedMode)
		self.regions[self.AlienFXProperties.RIGHT_SPEAKER_ID] = AlienFXRegion(self.AlienFXProperties.RIGHT_SPEAKER_ID, self.AlienFXTexts.RIGHT_SPEAKER_DESCRIPTION, self.REGION_RIGHT_SPEAKER,self.SUPPORTED_COMMANDS,True,True,True, self.suportedMode)
		self.regions[self.AlienFXProperties.LEFT_SPEAKER_ID] = AlienFXRegion(self.AlienFXProperties.LEFT_SPEAKER_ID, self.AlienFXTexts.LEFT_SPEAKER_DESCRIPTION, self.REGION_LEFT_SPEAKER,self.SUPPORTED_COMMANDS,True,True,True, self.suportedMode)
		self.regions[self.AlienFXProperties.ALIEN_LOGO_ID] = AlienFXRegion(self.AlienFXProperties.ALIEN_LOGO_ID, self.AlienFXTexts.ALIENWARE_LOGO_DESCRIPTION, self.REGION_ALIEN_NAME,self.SUPPORTED_COMMANDS,True,True,True, self.suportedMode)
		self.regions[self.AlienFXProperties.MEDIA_BAR_ID] = AlienFXRegion(self.AlienFXProperties.MEDIA_BAR_ID, self.AlienFXTexts.MEDIA_BAR_DESCRIPTION, self.REGION_MEDIA_BAR,self.SUPPORTED_COMMANDS,True,True,True, self.suportedMode)
		self.regions[self.AlienFXProperties.POWER_BUTTON_ID] = AlienFXRegion(self.AlienFXProperties.POWER_BUTTON_ID, self.AlienFXTexts.POWER_BUTTON_DESCRIPTION, self.REGION_POWER_BUTTON,2,True,True,True, self.suportedMode)

			
class AlienFX_Driver:
	def __init__(self):
		vendor_id=0x187c
		product_id=0x0522
		self.idVendor = vendor_id
		self.idProduct = product_id
		
		#Define I/O Reqquest types
		self.SEND_REQUEST_TYPE = 0x21
		self.SEND_REQUEST = 0x09
		self.SEND_VALUE = 0x202
		self.SEND_INDEX = 0x00
		self.READ_REQUEST_TYPE = 0xa1
		self.READ_REQUEST = 0x01
		self.READ_VALUE = 0x101
		self.READ_INDEX = 0x0
		
		
		#Define General Device controls
		self.ALIENFX_USER_CONTROLS = 0x01
		self.ALIENFX_SLEEP_LIGHTS = 0x02
		self.ALIENFX_ALL_OFF = 0x03
		self.ALIENFX_ALL_ON = 0x04

		self.ALIENFX_MORPH = 0x01
		self.ALIENFX_BLINK = 0x02
		self.ALIENFX_STAY = 0x03
		self.ALIENFX_BATTERY_STATE = 0x0F

		self.ALIENFX_TOUCHPAD        = 0x000001
		self.ALIENFX_LIGHTPIPE       = 0x000020
		self.ALIENFX_ALIENWARE_LOGO  = 0x000080
		self.ALIENFX_ALIENHEAD       = 0x000100
		self.ALIENFX_POWER_BUTTON    = 0x008000
		self.ALIENFX_TOUCH_PANEL     = 0x010000

		self.ALIENFX_DEVICE_RESET = 0x06
		self.ALIENFX_READY = 0x10
		self.ALIENFX_BUSY = 0x11
		self.ALIENFX_UNKOWN_COMMAND = 0x12
		
		self.debug = False
		
		self.AlienFXProperties = AlienFXProperties()
		self.AlienFXTexts = AlienFXTexts()
		
		#Initializing !
		# find our device   187c:0522 
		self.dev = usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)
		# was it found?
		if self.dev is None:
			print "The USB controler coresponding to %s:%s was not found !"%(hex(self.idVendor),hex(self.idProduct))
			sys.exit(1)
		self.computer = M11xR3()
		self.Take_over()
		#dev.claimInterface()

	def WriteDevice(self,MSG):
		if len(MSG[0]) == 9:
			for msg in MSG:
				if self.debug:
					print msg
				self.dev.ctrl_transfer(self.SEND_REQUEST_TYPE, self.SEND_REQUEST, self.SEND_VALUE, self.SEND_INDEX, msg)
		else:
			self.dev.ctrl_transfer(self.SEND_REQUEST_TYPE, self.SEND_REQUEST, self.SEND_VALUE, self.SEND_INDEX, MSG)
			
	def ReadDevice(self,msg):
		msg = self.dev.ctrl_transfer(self.READ_REQUEST_TYPE, self.READ_REQUEST, self.READ_VALUE, self.READ_INDEX, len(msg[0]))
		if self.debug:
			print msg
		return msg
		
		
	def Take_over(self):
		try:
			self.dev.set_configuration()
		except:
			self.dev.detach_kernel_driver(0)
			try:
				self.dev.set_configuration()
			except Exception,e:
				raise DeviceNotFound("Can't set the configuration. Error : %s"%e)

	def WaitForOk(self):
		self.Take_over()
		request = AlienFX_Constructor()
		while True:
			request.Get_Status()
			self.WriteDevice(request)
			msg = self.ReadDevice(request)
			#print msg
			if msg[0] == 0x10:
				break
			request.raz()
			request.Get_Status()
			request.Reset_all()
			self.WriteDevice(request)
			msg =  self.ReadDevice(request)
			#print msg
			if msg[0] == 0x10:
				break
		return True
	
class AlienFX_Main:
	def __init__(self):
		print "Initializing Controler ..."
		self.controller = AlienFX_Controler()
		self.Select_Menu()
		
	def Select_Menu(self):
		while True:
			select = raw_input("Please select an action : \n1\tChange the Color of an Area\n2)\tChange the Color of All\n3)\tExit\n\nSelection : ")
			if select == '1':
				self.Change_color()
			elif select == '2':
				self.Change_color(All=True)
			elif select == '3':
				sys.exit(0)
			else:
				print "Wrong choice, Please select on of the choice above !"
				time.sleep(1)
				self.Select_Menu()
	
	def Change_color(self,All = False):
			area = self.Area_Creator(All)
			color = self.Color_Creator()
			option = self.Option_Creator()
			if option == "morph":
				print "Morph Selected, please choose the second color for the morph !\n"
				color1 = self.Color_Creator()
			if option == "fixed":
				self.controller.Set_Color(area,color)
			elif option == "blink":
				self.controller.Set_Color_Blink(area,color)
			elif option == "morph":
				self.controller.Set_Color_Morph(area,color,color1)
	
	def Option_Creator(self):
		c = raw_input("Please select an option : \n1)\tFixed Color\n2)\tBlinking Color\n3)\tMorph Color\n\nSelection : ")
		if c == '1':
			return "fixed"
		elif c == '2':
			return "blink"
		elif c == '3':
			return "morph"
		else:
			print "Wrong choice, Please select on of the choice above !"
			time.sleep(1)
			self.Option_Creator()
		
	def Color_Creator(self):
		c = raw_input("Color Selection : \nPlease enter an HTML color : ")
		request = AlienFX_Constructor()
		color = request.Color(c.strip())
		return color
		
		
	def Area_Creator(self,All=False):
		request = AlienFX_Constructor()
		area = driver.computer.regions
		area_to_send = []
		keep = False
		if not All:
			while not keep:
				print "Select the areas for which the modifications applies\n"
				for i in area.keys():
					ok = raw_input("Area : %s (Y/N) : "%(area[i].description))
					if ok.upper() == 'Y':
						area_to_send.append(i)
						keep = True
				if not keep:
					print "Please select at least one Area !"
		if All:
			print "All Areas selected !"
			for i in area.keys():
				area_to_send.append(i)
		request = AlienFX_Constructor()
		area = request.Area(area_to_send)
		return area
		
	
class AlienFX_Controler:
	def __init__(self):
		self.driver = driver
	
	def Set_Color(self,Area,Color):
		"""Set the Color of an Area """
		self.driver.WaitForOk()
		request = AlienFX_Constructor()
		request.Set_Color(Area,Color)
		request.End_Loop()
		request.End_Transfert()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
	
	def Set_Color_Blink(self,Area,Color):
		self.driver.WaitForOk()
		request = AlienFX_Constructor()
		request.Set_Speed()
		request.Set_Blink_Color(Area,Color)
		request.End_Loop()
		request.End_Transfert()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
		
	def Set_Color_Morph(self,Area,Color1,Color2):
		self.driver.WaitForOk()
		request = AlienFX_Constructor()
		request.Set_Speed()
		request.Set_Morph_Color(Area,Color1,Color2)
		request.End_Loop()
		request.End_Transfert()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
	
	
class AlienFX_Constructor(list):
	def __init__(self):
		self.raz()
		self.computer = driver.computer
		self.void = [self.computer.FILL_BYTE]*9
		self.Id = 1
		self.default_area = {"r_speaker" : False, "l_speaker" : False, "keyboard" : False, "logo" : False, "media" : False, "power" : False}
		
		
	def Set_Speed(self,Speed = 0xc8):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_SPEED
		cmd[3] = Speed
		self.append(cmd)
	
	def Set_Blink_Color(self,Area,Color):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_BLINK_COLOR
		cmd[2] = self.Id
		cmd[4] = Area[0]
		cmd[5] = Area[1]
		cmd[6] = Color[0]
		cmd[7] = Color[1]
		#print "constructor : ",cmd
		self.append(cmd)
	
	def Set_Morph_Color(self,Area,Color1,Color2):
		cmd = copy(self.void)
		Color2[1] = Color2[1]/16 + Color2[0] - (Color2[0]/16)*16
		Color12 = Color1[1] + Color2[0]/16
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_MORPH_COLOR
		cmd[2] = self.Id
		cmd[4] = Area[0]
		cmd[5] = Area[1]
		cmd[6] = Color1[0]
		cmd[7] = Color12
		cmd[8] = Color2[1]
		print "constructor : ",cmd
		self.append(cmd)
	
	def Area(self, areas): # gotta check the power button to understand it ...
		area = 0x0000
		ret = [0x00,0x00]
		for key in areas:
			area += self.computer.regions[key].regionId
		n = 0
		a = ""
		while len(a) != 2:
			n -= 1
			if hex(area)[n] != 'x':
				a += hex(area)[n]
			else:
				n+=1
				break
		if len(a) == 2:
			a = a[1] + a[0]
		ret[1] = int(a,16)
		a = ""
		while len(a) != 2:
			n -= 1
			if hex(area)[n] != 'x':
				a += hex(area)[n]
			else:
				if not a:
					a = '00'
				break
		if len(a) == 2:
			a = a[1] + a[0]
		ret[0] = int(a,16)
		return ret
	
	def Set_Color(self,Area,Color,Id = 0x01):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_COLOR
		cmd[2] = Id
		cmd[4] = Area[0]
		cmd[5] = Area[1]
		cmd[6] = Color[0]
		cmd[7] = Color[1]
		#print "constructor : ",cmd
		self.append(cmd)
	
	def Color(self,color):
		r = int(color[0:2],16)/16
		g = int(color[2:4],16)/16
		b = int(color[4:6],16)/16
		c = [0x00,0x00]
		c[0] = r * 16 + g  # if r = 0xf > r*16 = 0xf0 > and b = 0xc r*16 + b 0xfc 
		c[1] = b * 16
		return c
		
		
		
	def Get_Status(self):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_GET_STATUS
		#print "constructor : ",cmd
		self.append(cmd)
		
	def Reset_all(self):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_RESET
		cmd[2] = self.computer.RESET_ALL_LIGHTS_ON
		#print "constructor : ",cmd
		self.append(cmd)
	
	def End_Loop(self):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_LOOP_BLOCK_END
		#print "constructor : ",cmd
		self.append(cmd)
		
	def End_Transfert(self):
		cmd = copy(self.void)
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_TRANSMIT_EXECUTE
		#print "constructor : ",cmd
		self.append(cmd)
	
	def raz(self):
		while len(self) != 0:
			self.pop()
		self.default_area = {"r_speaker" : False, "l_speaker" : False, "keyboard" : False, "logo" : False, "media" : False, "power" : False}
		
		
if __name__ == "__main__":
	driver = AlienFX_Driver()
	main = AlienFX_Main()