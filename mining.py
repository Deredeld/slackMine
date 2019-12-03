#!/usr/bin/python
# -*- coding: latin-1 -*-
#"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump" -u root -p norman > "C:\Users\n.oshea\Desktop\tset\slack mine\BD.sql"
import mysql.connector
import time
import random

from minehelp import *
from mine import *
from minekill import *
from mineDataBase import *
from minebet import *
from mineshop import *
from minearmor import *
from minehealth import *
from mineshow import *
from minefight import *

from minetop import minetop
from slackclient import SlackClient
from random import randint
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
import datetime as dt


def main():
	config = {
	  'user': 'norman',
	  'password': 'root',
	  'host': '127.0.0.1',
	  'database': 'norman',
	  'raise_on_warnings': True,

	}
	cnx = mysql.connector.connect(**config)
	mycursor = cnx.cursor(buffered=True)
	sc = SlackClient("xoxb-233810080487-757853189332-iGTli25SzWYFJOtzpdXqxMqj")
	if sc.rtm_connect():

		while True:
			for slack_message in sc.rtm_read():
				if slack_message.get("type")=="message" and (slack_message.get("subtype")==None or  slack_message.get("subtype")!="bot_message" or slack_message.get("subtype")!="message_changed"):
#mine
					g = re.match('^!mine\\b|^!m\\b',str(slack_message.get("text")))
					if g :
						mine(sc,slack_message,mycursor,cnx)
#mine pick 
					g = re.match('^!minepick\\b|^!mpick\\b',str(slack_message.get("text")))
					if g :
						g1 = re.match('^!minepick buy|^!mpick buy',str(slack_message.get("text")))
						if g1:
							minepickbuy(sc,slack_message,mycursor,cnx)
						else:
							minepick(sc,slack_message,mycursor,cnx)
#mine show
					s = re.match('^!mineshow\\b|^!mshow\\b',str(slack_message.get("text")))
					if s :
						ss = re.match('^(!mineshow|!mshow) weapon',str(slack_message.get("text")))
						if ss:
							mineshowweapon(sc,slack_message,mycursor,cnx)
						else:
							mineshow(sc,slack_message,mycursor,cnx)

#mine give
					g = re.match('^!minegive <@([A-Z0-9]{0,9})> ([1-9]\d*)|^!mgive <@([A-Z0-9]{0,9})> ([1-9]\d*)',str(slack_message.get("text")))
					if g:
						minegive(sc,slack_message,mycursor,cnx,g)
#mine bet
					g = re.match('^!minebet ([1-9]\d*|all)|^!mbet ([1-9]\d*|all)',str(slack_message.get("text")))
					if g:
						minebet(sc,slack_message,mycursor,cnx,g)
#mine bet jackpot
					megajacpot = re.match('^!minebet megajackpot|^!mbet mj',str(slack_message.get("text")))
					if megajacpot:
						minebet_jackpot(sc,slack_message,mycursor)
#mine help
					g = re.match('^!minehelp\\b|^!mhelp\\b',str(slack_message.get("text")))
					if g:
						minehelp(sc,slack_message)
#mine classement
					g = re.match('^!minetop|^!mtop',str(slack_message.get("text")))
					if g:
						minetop(sc,slack_message,mycursor,cnx)
#mine kill
					g = re.match('^!minekill <@([A-Z0-9]{0,9})>|^!mkill <@([A-Z0-9]{0,9})>',str(slack_message.get("text")))
					if g:
						minekill(sc,slack_message,mycursor,cnx,g)
#MOD givegold
					g = re.match('^!modsetgold <@([A-Z0-9]{0,9})> ([0-9]\d*)',str(slack_message.get("text")))
					if g and slack_message.get("user")=="U75NSUFLP":
							if g.group(1) is None:
								MODsetgold(mycursor,g.group(2),cnx,slack_message.get("user"))
							else:
								MODsetgold(mycursor,g.group(2),cnx,g.group(1))
#mine shop
					g = re.match('^!mineshop$|^!mshop$',str(slack_message.get("text")))
					if g:
						mineshop(sc,slack_message,mycursor,cnx)
#mine weapon
					g = re.match('^!mineweapon|^!mweapon',str(slack_message.get("text")))
					if g:
						mineweapon(sc,slack_message,mycursor,cnx)
#mine buy
					g = re.match('^!mineshop buy ([0-9]\d*)|^!mshop buy ([0-9]\d*)',str(slack_message.get("text")))
					if g:
						if g.group(2) is None:
							mineshopbuy(sc,slack_message,mycursor,cnx,g.group(1))
						else:	
							mineshopbuy(sc,slack_message,mycursor,cnx,g.group(2))
#mine health 
					g = re.match('^!minehealth\\b|^!mhealth\\b',str(slack_message.get("text")))
					if g :
						g1 = re.match('^!minehealth buy|^!mhealth buy',str(slack_message.get("text")))
						if g1:
							minehealthbuy(sc,slack_message,mycursor,cnx)
						else:
							minehealth(sc,slack_message,mycursor,cnx)
#mine armor
					g = re.match('^!minearmor\\b|^!marmor\\b',str(slack_message.get("text")))
					if g :
						g1 = re.match('^!minearmor buy|^!marmor buy',str(slack_message.get("text")))
						if g1:
							minearmorbuy(sc,slack_message,mycursor,cnx)
						else:
							minearmor(sc,slack_message,mycursor,cnx)
#mine fight
					g = re.match('^!mfight <@([A-Z0-9]{0,9})>',str(slack_message.get("text")))
					if g:
						minefight(sc,slack_message,mycursor,cnx,g)

	cnx.close()





def minegive(sc,slack_message,mycursor,cnx,g):
	if g.group(1) is not None:
		id = g.group(1)
		amount = g.group(2)
	else:
		id = g.group(3)
		amount = g.group(4)
	if checkuser(mycursor,slack_message.get("user")):
		user =getuser(mycursor,slack_message.get("user"))
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have gold. Type !mine to mine gold")
	if int(user[1])>=int(amount):
		addgold(mycursor,id,amount,cnx)
		lessgold(mycursor,user[0],amount,cnx)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=("You gave "+str(amount)+ " gold to <@"+id+">").format())
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")

def minepick(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		user =getuser(mycursor,slack_message.get("user"))
	else:
		user[2] = 1
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You have a level "+str(user[2])+ " pickaxe. The next upgrade will cost "+str(pow(2,user[2])*user[2])+" gold. You have " +str(user[1]) +" gold")

def minepickbuy(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		user =getpick(mycursor,slack_message.get("user"))
		if user[1]>=pow(2,user[2])*user[2]:
			upgradePick(mycursor,user[0],cnx)
			lessgold(mycursor,user[0],pow(2,user[2])*user[2],cnx)
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You now have a level "+str(user[2]+1)+ " pickaxe. The next upgrade will cost "+str(pow(2,(user[2]+1))*(user[2]+1))+" gold. You have " +str(user[1]-pow(2,user[2])*user[2]) +" gold")
		else:
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")
			minepick(sc,slack_message,mycursor,cnx)
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")


if __name__ == '__main__':
	main()