# -*- coding: UTF-8 -*-

#This file is part of pyAlienFX.
#
#    pyAlienFX is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyAlienFX is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyAlienFX.  If not, see <http://www.gnu.org/licenses/>.


import usb
import platform
import sys,os
from copy import *
import time

from AlienFX.AlienFXProperties import *
from AlienFX.AlienFXTexts import *
from AlienFX.AlienFXComputers import AllComputers


class AlienFX_Driver(AllComputers):
	def __init__(self):
		#Define I/O Reqquest types
		self.SEND_REQUEST_TYPE = 0x21
		self.SEND_REQUEST = 0x09
		self.SEND_VALUE = 0x202
		self.SEND_INDEX = 0x00
		self.READ_REQUEST_TYPE = 0xa1
		self.READ_REQUEST = 0x01
		self.READ_VALUE = 0x101
		self.READ_INDEX = 0x0
		
		
		self.debug = False
		
		self.AlienFXProperties = AlienFXProperties()
		self.AlienFXTexts = AlienFXTexts()
				
		#Initializing !
		# find our device 
		if not self.FindDevice():
			print "No AlienFX USB controler found ! Go see the list of supported computer on : https://code.google.com/p/pyalienfx/wiki/SupportedComputer "
			sys.exit(1)
		self.Take_over()
		#dev.claimInterface()
	
	def FindDevice(self):
		"""Look for all the devices listed in the AlienFXComputer file, if found return True, else return False.
		If a computer is found, the device is loaded, as well as all the parameters for the computer (which are in the AlienFXComputer)"""
		ok = False
		for computer in self.computerList.keys():
			dev = usb.core.find(idVendor=self.computerList[computer].vendorId, idProduct=self.computerList[computer].productId)
			if dev != None:
				print "Comnputer %s found ! Loading the parameters ..."%self.computerList[computer].name
				self.computer = self.computerList[computer].computer
				self.vendorId = self.computerList[computer].vendorId
				self.productId = self.computerList[computer].productId
				self.dev = dev
				return True
		return False
	
	def WriteDevice(self,MSG):
		if len(MSG[0].packet) == self.computer.DATA_LENGTH:
			for msg in MSG:
				if self.debug:
					print "Sending : %s\nPacket : %s"%(msg.legend,msg.packet)
				self.dev.ctrl_transfer(self.SEND_REQUEST_TYPE, self.SEND_REQUEST, self.SEND_VALUE, self.SEND_INDEX, msg.packet)
		else:
			self.dev.ctrl_transfer(self.SEND_REQUEST_TYPE, self.SEND_REQUEST, self.SEND_VALUE, self.SEND_INDEX, MSG)
			
	def ReadDevice(self,msg):
		msg = self.dev.ctrl_transfer(self.READ_REQUEST_TYPE, self.READ_REQUEST, self.READ_VALUE, self.READ_INDEX, len(msg[0].packet))
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
				sys.exit(1)


class AlienFX_Controller:
	def __init__(self,driver):
		self.driver = driver
		
	def Set_Loop(self,action):
		self.WaitForOk()
		self.driver.WriteDevice(action)
		time.sleep(0.1)
		self.driver.WriteDevice(action)
	
	def Set_Color(self,Area,Color):
		"""Set the Color of an Area """
		self.WaitForOk()
		request = AlienFX_Constructor(self.driver)
		request.Set_Color(Area,Color)
		request.End_Loop()
		request.End_Transfert()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
	
	def Set_Color_Blink(self,Area,Color):
		self.WaitForOk()
		request = AlienFX_Constructor(self.driver)
		request.Set_Speed()
		request.Set_Blink_Color(Area,Color)
		request.End_Loop()
		request.End_Transfert()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
		
	def Set_Color_Morph(self,Area,Color1,Color2):
		self.WaitForOk()
		request = AlienFX_Constructor(self.driver)
		request.Set_Speed()
		request.Set_Morph_Color(Area,Color1,Color2)
		request.End_Loop()
		request.End_Transfert()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
	
	def Send_Request(self,request):
		self.WaitForOk()
		self.driver.WriteDevice(request)
		time.sleep(0.1)
		self.driver.WriteDevice(request)
	
	def WaitForOk(self):
		self.driver.Take_over()
		request = AlienFX_Constructor(self.driver)
		while True:
			request.Get_Status()
			self.driver.WriteDevice(request)
			msg = self.driver.ReadDevice(request)
			#print msg
			if msg[0] == 0x10:
				break
			request.raz()
			request.Get_Status()
			request.Reset_all()
			self.driver.WriteDevice(request)
			msg =  self.driver.ReadDevice(request)
			#print msg
			if msg[0] == 0x10:
				break
		return True
	
class AlienFX_Constructor(list):
	def __init__(self,driver):
		self.raz()
		self.computer = driver.computer
		self.void = [self.computer.FILL_BYTE]*self.computer.DATA_LENGTH
		self.Id = 0x01		
	
	def Show_Request(self):
		for i in self:
			packet = ""
			for j in i.packet:
				packet += hex(j) + " "
			print "%s\t:\t%s"%(i.legend,packet)
	
	def Set_Speed(self,Speed = 0xc8):
		cmd = copy(self.void)
		legend = "Set Speed : %s"%Speed
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_SPEED
		cmd[3] = Speed
		self.append(Request(legend,cmd))
	
	def Set_Blink_Color(self,Area,Color):
		cmd = copy(self.void)
		legend = "Set Blink Color, Area : %s, Color : r = %s, g = %s, b = %s"%(hex(Area[0]*65536 + Area[1]*256 + Area[2]),hex((Color[0]/16)),hex(Color[0]-(Color[0] - (Color[0]/16)*16)),hex(Color[1]+16))
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_BLINK_COLOR
		cmd[2] = self.Id
		cmd[3] = Area[0]
		cmd[4] = Area[1]
		cmd[5] = Area[2]
		cmd[6] = Color[0]
		cmd[7] = Color[1]
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
	
	def Set_Morph_Color(self,Area,Color1,Color2):
		cmd = copy(self.void)
		legend = "Set Morph Color, Area : %s , Color1 : r = %s, g = %s, b = %s, Color2 : r = %s, g = %s, b = %s"%(hex(Area[0]*65536 + Area[1]*256 + Area[2]),hex((Color1[0]/16)),hex(Color1[0]-(Color1[0] - (Color1[0]/16)*16)),hex(Color1[1]+16),hex((Color2[0]/16)),hex(Color2[0]-(Color2[0] - (Color2[0]/16)*16)),hex(Color2[1]+16))
		Color2[1] = Color2[1]/16 + Color2[0] - (Color2[0]/16)*16
		Color12 = Color1[1] + Color2[0]/16
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_MORPH_COLOR
		cmd[2] = self.Id
		cmd[3] = Area[0]
		cmd[4] = Area[1]
		cmd[5] = Area[2]
		cmd[6] = Color1[0]
		cmd[7] = Color12
		cmd[8] = Color2[1]
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
		
	def Area(self, areas): # gotta check the power button to understand it ...
		area = 0x000000
		ret = [0x00,0x00,0x00]
		for key in areas:
			area += self.computer.regions[key].regionId
		ret[0] = area/65536				#Takes the two first digit
		ret[1] = area/256 - ret[0] * 256		#Takes the four first digit and remove the two first digit ret[0] = 0x12 => ret[0] * 256 = 0x1200
		ret[2] = area - ret[0] * 65536 - ret[1] * 256	#Same but remove the first 4 digit
		return ret
	
	def Set_Color(self,Area,Color,Id = 0x01):
		cmd = copy(self.void)
		legend = "Set Fixed Color, Area : %s, Color : r = %s, g = %s, b = %s"%(hex(Area[0]*65536 + Area[1]*256 + Area[2]),hex((Color[0]/16)),hex(Color[0]-(Color[0] - (Color[0]/16)*16)),hex(Color[1]+16))
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_SET_COLOR
		cmd[2] = self.Id
		cmd[3] = Area[0]
		cmd[4] = Area[1]
		cmd[5] = Area[2]
		cmd[6] = Color[0]
		cmd[7] = Color[1]
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
	
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
		legend = "Get Status"
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_GET_STATUS
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
		
	def Reset_all(self):
		cmd = copy(self.void)
		legend = "Reset All Lights On"
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_RESET
		cmd[2] = self.computer.RESET_ALL_LIGHTS_ON
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
	
	def End_Loop(self):
		cmd = copy(self.void)
		legend = "End Loop"
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_LOOP_BLOCK_END
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
		
	def End_Transfert(self):
		cmd = copy(self.void)
		legend = "End Transfert"
		cmd[0] = self.computer.START_BYTE
		cmd[1] = self.computer.COMMAND_TRANSMIT_EXECUTE
		#print "constructor : ",cmd
		self.append(Request(legend,cmd))
	
	def raz(self):
		while len(self) != 0:
			self.pop()
			

class Request:
	def __init__(self,legend,packet):
		self.legend = legend
		self.packet = packet