#!/usr/bin/python
# -*- coding: latin-1 -*-

from random import randint
from mineDAO import *

def minefight(sc,slack_message,mycursor,cnx,g):
	if g.group(1) is None: f2 = g.group(2)
	else: user2 = g.group(1)
	if checkuser(mycursor,slack_message.get("user")):
		f1 = DAOgetUser(mycursor,slack_message.get("user"))
		if user2 is not None and checkuser(mycursor,user2):
			f2 = DAOgetUser(mycursor,user2)
			w1 = DAOgetWeapon(mycursor,f1.idweapon)
			w2 = DAOgetWeapon(mycursor,f2.idweapon)
			fighting(f1,w1,f2,w2,slack_message,sc)




def fighting(f1,w1,f2,w2,slack_message,sc):
	meter1=w1.speed
	meter2=w2.speed
	nom1  = sc.api_call("users.info",user=f1.id)['user']['real_name']
	nom2  = sc.api_call("users.info",user=f2.id)['user']['real_name']
	ts=sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="```"+str(nom1)+" VS "+str(nom2)+"```")['message']['ts']

	while(f1.health>=0 and f2.health>=0):
		if(meter1<meter2):
			meter1=meter1+w1.speed
			if(randint(1,100)<w1.hitChance):
				f2.health = f2.health-w1.damage
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=str(nom2)+" took "+str(w1.damage)+" damage.",thread_ts=ts)
		else:
			meter2=meter2+w2.speed
			if(randint(1,100)<int(w2.hitChance)):
				f1.health = f1.health-w2.damage
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=str(nom1)+" took "+str(w2.damage)+" damage.",thread_ts=ts)
	if(f1.health>=0):
		sc.api_call("chat.update",channel=slack_message.get("channel"),text="```"+str(nom1)+" VS "+str(nom2)+"\n"+str(nom1)+" won with "+str(f1.health)+" health.```",ts=ts)
	else:
		sc.api_call("chat.update",channel=slack_message.get("channel"),text="```"+str(nom1)+" VS "+str(nom2)+"\n"+str(nom2)+" won with "+str(f2.health)+" health.```",ts=ts)
	del f1
	del f2
	del w1
	del w2

		# t =("```" +
		# "╔═════════════════════════╦══════════╦══════════╦═════════╦═════════╦═════════════════╗ \n" +
		# "║           Nom           ║   Gold   ║ Pick lvl ║  Health ║  Armor  ║     Weapon      ║ \n" +
		# "╠═════════════════════════╬══════════╬══════════╬═════════╬═════════╬═════════════════╣ \n")
		# nom  = sc.api_call("users.info",user=re[0])['user']['real_name']
		# weapon =getuserweapon(mycursor,re[0])
		# t = t + "║" +str(nom.ljust(25, ' '))[:25] +"║"+ str(re[1]).ljust(10, ' ') +"║"+ str(re[2]).ljust(10, ' ') +"║"+ str(re[4]).ljust(9, ' ')+"║"+ str(re[5]).ljust(9, ' ')+"║"+ str("["+str(weapon[0])+"]"+weapon[1]).ljust(17, ' ')+"║ \n"
		# t =(t +
		# "╚═════════════════════════╩══════════╩══════════╩═════════╩═════════╩═════════════════╝"+
		# " ```")