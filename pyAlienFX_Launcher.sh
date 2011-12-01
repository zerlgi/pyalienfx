#!/bin/sh
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

# This file will launch the deamon and the indicator applet !
# You should add it to your Session Auto Launch for a better experience !

python pyAlienFX_daemon.py
sleep 5
python pyAlienFX_Indicator.py