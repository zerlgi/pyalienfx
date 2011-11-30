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

#PyALienFX Deamon
#The deamon will load the driver and the controller
#You can comunicate with the Deamon through TCP
#You can send packet so the deamon will control the AlienFX
#That way you can create GUI, plugins, ect to play with the AlienFX ! 


from AlienFX.AlienFXEngine import *
from socket import *
import sys
import os

BUFSIZ = 4096
HOST = 'localhost'
PORT = 25436 #ALIEN port as if you typed ALIEN on your phone ;)
ADDR = (HOST,PORT)

class ServCmd:
	def __init__(s):
		print "Initializing Driver  ..."
		s.driver = AlienFX_Driver()
		print "Initializing Controller ..."
		s.controller = AlienFX_Controller(s.driver)
		s.computer = s.driver.computer
		s.__serv = socket( AF_INET,SOCK_STREAM)
		s.__serv.bind((ADDR))
		s.__cli = None
		s.__imlistening  = 0
		s.__improcessing = 0
		s.__run()

	def __run(s):
		s.__imlistening = 1
		while s.__imlistening:
			s.__listen()
			s.__improcessing = 1
			while s.__improcessing:
				s.__procCmd()
			s.__cli.close()
		s.__serv.close()

	def __listen(s):
		s.__serv.listen(5)
		print '...listening'
		cli,addr = s.__serv.accept()
		s.__cli = cli
		print '...connected: ', addr

	def __procCmd(s):
		cmd = s.__cli.recv(BUFSIZ)
		if not cmd: return
		print cmd
		s.__servCmd(cmd)
		if s.__improcessing:
			for c in cmd.split('|'):
				command = c.split(',')[0]
				arg = c.split(',')[1:]
				if command == "Set_Loop":
					action = arg[0]
					s.controller.Set_Loop(action)
				elif command == "Set_Loop_Conf":
					if arg[0] == "True":
						Save = True
					elif arg[0] == "False":
						Save = False
					else:
						Save = None
					if arg[1]:
						block = int(arg[1])
					else:
						block = None
					if Save and block:
						s.controller.Set_Loop_Conf(Save,block)
					elif Save:
						s.controller.Set_Loop_Conf(Save=Save)
					elif block:
						s.controller.Set_Loop_Conf(block=block)
				elif command == "Add_Loop_Conf":
					area,mode,color1,color2 = arg[0],arg[1],arg[2],arg[3]
					if not color2:
						color2 = None
					if area and mode and color1:
						s.controller.Add_Loop_Conf(area,mode,color1,color2)
				elif command == "Add_Speed_Conf":
					if arg[0]:
						speed = int(arg[0])
						s.controller.Add_Speed_Conf(speed)
					else:
						s.controller.Add_Speed_Conf()
				elif command == "End_Loop_Conf":
					s.controller.End_Loop_Conf()
				elif command == "End_Transfert_Conf":
					s.controller.End_Transfert_Conf()
				elif command == "Write_Conf":
					s.controller.Write_Conf()
				elif command == "Set_Color":
					Area,Color = arg[0],arg[1]
					if arg[2]:
						if arg[2] == "False":
							Save = False
						elif arg[2] == "True":
							Save = True
						else:
							Save = None
					else:
						Save = None
					if arg[3]:
						if arg[3] == "False":
							Apply = False
						elif arg[3] == "True":
							Apply = True
						else:
							Apply = None
					else:
						Apply = None
					if arg[4]:
						block = int(arg[4])
					else:
						block = None
					if Save and Apply and block:
						s.controller.Set_Color(Area, Color, Save = Save, Apply = Apply, block = block)
					elif Save and Apply:
						s.controller.Set_Color(Area, Color, Save = Save, Apply = Apply)
					elif Save and block:
						s.controller.Set_Color(Area, Color, Save = Save, block = block)
					elif Apply and block:
						s.controller.Set_Color(Area, Color, Apply = Apply, block = block)
					elif Save:
						s.controller.Set_Color(Area, Color, Save = Save)
					elif Apply:
						s.controller.Set_Color(Area, Color, Apply = Apply)
					elif block:
						s.controller.Set_Color(Area, Color, block = block)
				elif command == "Set_Color_Blink":
					Area,Color = arg[0],arg[1]
					if arg[2]:
						if arg[2] == "False":
							Save = False
						elif arg[2] == "True":
							Save = True
						else:
							Save = None
					else:
						Save = None
					if arg[3]:
						if arg[3] == "False":
							Apply = False
						elif arg[3] == "True":
							Apply = True
						else:
							Apply = None
					else:
						Apply = None
					if arg[4]:
						block = int(arg[4])
					else:
						block = None
					if Save and Apply and block:
						s.controller.Set_Color_Blink(Area, Color, Save = Save, Apply = Apply, block = block)
					elif Save and Apply:
						s.controller.Set_Color_Blink(Area, Color, Save = Save, Apply = Apply)
					elif Save and block:
						s.controller.Set_Color_Blink(Area, Color, Save = Save, block = block)
					elif Apply and block:
						s.controller.Set_Color_Blink(Area, Color, Apply = Apply, block = block)
					elif Save:
						s.controller.Set_Color_Blink(Area, Color, Save = Save)
					elif Apply:
						s.controller.Set_Color_Blink(Area, Color, Apply = Apply)
					elif block:
						s.controller.Set_Color_Blink(Area, Color, block = block)
				elif command == "Set_Color_Morph":
					Area,Color1,Color2 = arg[0],arg[1],arg[2]
					if arg[3]:
						if arg[3] == "False":
							Save = False
						elif arg[3] == "True":
							Save = True
						else:
							Save = None
					else:
						Save = None
					if arg[4]:
						if arg[4] == "False":
							Apply = False
						elif arg[4] == "True":
							Apply = True
						else:
							Apply = None
					else:
						Apply = None
					if arg[5]:
						block = int(arg[5])
					else:
						block = None
					if Save and Apply and block:
						s.controller.Set_Color_Morph(Area,Color1,Color2, Save = Save, Apply = Apply, block = block)
					elif Save and Apply:
						s.controller.Set_Color_Morph(Area,Color1,Color2, Save = Save, Apply = Apply)
					elif Save and block:
						s.controller.Set_Color_Morph(Area,Color1,Color2, Save = Save, block = block)
					elif Apply and block:
						s.controller.Set_Color_Morph(Area,Color1,Color2, Apply = Apply, block = block)
					elif Save:
						s.controller.Set_Color_Morph(Area,Color1,Color2, Save = Save)
					elif Apply:
						s.controller.Set_Color_Morph(Area,Color1,Color2, Apply = Apply)
					elif block:
						s.controller.Set_Color_Morph(Area,Color1,Color2, block = block)
				elif command == "WaitForOk":
					s.controller.WaitForOk()
				elif command == "Get_State":
					s.controller.Get_State()
			s.__cli.send('executed')

	def __servCmd(s,cmd):
		cmd = cmd.strip()
		if cmd == 'BYE':
			s.__improcessing = 0
		elif cmd == 'EXIT':
			s.__improcessing = 0
			s.__imlistening = 0
		elif cmd == 'RESTART':
			s.__improcessing = 0
			s.__imlistening = 0
			s.__init__()

if __name__ == '__main__':
    Daemon = ServCmd()