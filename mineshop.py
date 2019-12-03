#!/usr/bin/python
# -*- coding: latin-1 -*-
from mineDataBase import *


def mineshop(sc,slack_message,mycursor,cnx):
	res = getweaponlist(mycursor)
	t ="```"+	"╔════╦═════════════════╦════════╦═══════╦════════════╦══════════╦═══════╗ \n"+"║ Id ║       Name      ║ Damage ║ Speed ║ HitChance% ║   Cost   ║  DPS  ║\n"+	"╠════╬═════════════════╬════════╬═══════╬════════════╬══════════╬═══════╣\n"
	for re in res:
		t = t + "║" +str(re[0]).ljust(4, ' ') +"║"+ str(re[1]).ljust(17, ' ') +"║"+ str(re[2]).ljust(8, ' ') +"║"+ str(re[3]).ljust(7, ' ') +"║"+ str(re[4]).ljust(12, ' ') +"║"+ str(re[5]).ljust(10, ' ') +"║"+ str(re[6]).ljust(7, ' ') + "║ \n"
	t =t+ "╚════╩═════════════════╩════════╩═══════╩════════════╩══════════╩═══════╝"+	" ```"
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=t)

def mineshopbuy(sc,slack_message,mycursor,cnx,idw):
	if checkuser(mycursor,slack_message.get("user")): #Check if user in database
		weapon = getweapon(mycursor,idw) #Get weapon
		if weapon is not None: #If weapon exists and not 'fist'
			user =getuser(mycursor,slack_message.get("user"))
			if user[1]>=weapon[5]: #If enough money 
				buyweapon(mycursor,cnx,user[0],weapon[0])
				lessgold(mycursor,user[0],weapon[5],cnx)
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You just bought a  "+str(weapon[1])+ " for "+str(weapon[5])+ ". You now have " +str(user[1]-weapon[5]) +" gold")
			else:
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")
		else:
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="This weapon does not exists.")
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")

def mineweapon(sc,slack_message,mycursor,cnx):
	re = getuserweapon(mycursor,slack_message.get("user"))
	t ="```"+	"╔════╦═════════════════╦════════╦═══════╦═══════════╦══════════╦═══════╗ \n"+"║ Id ║       Name      ║ Damage ║ Speed ║ HitChance ║   Cost   ║  DPS  ║\n"+	"╠════╬═════════════════╬════════╬═══════╬═══════════╬══════════╬═══════╣\n"
	t = t + "║" +str(re[0]).ljust(4, ' ') +"║"+ str(re[1]).ljust(17, ' ') +"║"+ str(re[2]).ljust(8, ' ') +"║"+ str(re[3]).ljust(7, ' ') +"║"+ str(re[4]).ljust(11, ' ') +"║"+ str(re[5]).ljust(10, ' ') +"║"+ str(re[6]).ljust(7, ' ') + "║ \n"
	t =t+ "╚════╩═════════════════╩════════╩═══════╩═══════════╩══════════╩═══════╝"+	" ```"
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=t)


