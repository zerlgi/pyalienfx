#!/usr/bin/python
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
#
#    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. 
#    To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter 
#    to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
#

from AlienFX.AlienFXEngine import *

class AlienFX_Main:
	def __init__(self):
		print "Initializing Driver  ..."
		self.driver = AlienFX_Driver()
		print "Initializing Controller ..."
		self.controller = AlienFX_Controller(self.driver)
		self.Select_Menu()
		
	def Select_Menu(self):
		while True:
			select = raw_input("Please select an action : \n1\tChange the Color of an Area\n2)\tChange the Color of All\n3)\tCreate a Loop\n4)\tExit\n\nSelection : ")
			if select == '1':
				self.Change_color()
			elif select == '2':
				self.Change_color(All=True)
			elif select == '3':
				self.Set_loop()
			elif select == '4':
				sys.exit(0)
			else:
				print "Wrong choice, Please select on of the choice above !"
				time.sleep(1)
				self.Select_Menu()
	
	def Change_color(self,All = False):
		self.Create_Request()
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
	
	def Speed_Creator(self):
		while True:
			s = raw_input("Please enter a speed from 0 - 255 : ")
			if int(s) >= 0 and int(s) <= 255:
				return int(s)
			else:
				print "Please enter a correct value !"
	
	def Create_Request(self):
		self.request = AlienFX_Constructor(self.driver)
	
	def Color_Creator(self):
		c = raw_input("Color Selection : \nPlease enter an HTML color : ")
		color = self.request.Color(c.strip())
		return color
		
	def Area_Creator(self,All=False):
		area = self.driver.computer.regions
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
		area = self.request.Area(area_to_send)
		return area
	
	def Set_loop(self):
		self.Create_Request()
		while True:
			print "Actual request : \n"
			self.request.Show_Request()
			s = raw_input("Loop Creator\n============\n1)\tAdd a loop\n2)\tApply Loop\nPlease make a choice : ")
			if s == '1':
				self.Loop_Creator()
			elif s == '2' and len(self.request) != 0:
				self.request.End_Transfert()
				self.controller.Set_Loop(self.request)
				break
			elif s == '2' and len(self.request) == 0:
				print "Add at least one loop !"
	
	def Loop_Creator(self):
		speed = self.Speed_Creator()
		self.request.Set_Speed(speed)
		while True:
			print "Actual request : \n"
			self.request.Show_Request()
			s = raw_input("Creating loop : \n=============\n1)\tAdd fixed color\n2)\tAdd blink color\n3)\tAdd morph color\n4)\tEnd Loop\nPlease make a choice : ")
			if s in ['1','2','3']:
				All = False
				c = raw_input("All Area ? (Y/N) : ")
				if c.upper() == 'Y':
					All = True
				area = self.Area_Creator(All)
				color = self.Color_Creator()
			if s == '1':
				self.request.Set_Color(area,color)
			elif s == '2':
				self.request.Set_Blink_Color(area,color)
			elif s == '3':
				print "Morph Selected, please choose the second color for the morph !\n"
				color1 = self.Color_Creator()
				self.request.Set_Morph_Color(area,color,color1)
			elif s == '4':
				self.request.End_Loop()
				break

		
if __name__ == "__main__":
	main = AlienFX_Main()