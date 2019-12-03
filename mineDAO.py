#!/usr/bin/python
# -*- coding: latin-1 -*-


import mysql.connector
from mineDataBase import *
from mineClassUser import *
from mineClassWeapon import *


def DAOgetUser(mycursor,id):
	a = getuser(mycursor,id)
	return User(a[0],a[1],a[2],a[3],a[4],a[5])


def DAOgetWeapon(mycursor,id):
	a = getweapon(mycursor,id)
	return Weapon(a[0],a[1],a[2],a[3],a[4],a[5],a[6])