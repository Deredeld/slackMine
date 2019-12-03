#!/usr/bin/python
# -*- coding: latin-1 -*-
from mineshop import getuserweapon

def minetop(sc,slack_message,mycursor,cnx):
	res = gettopscore(mycursor)
	t =("```" +
		"╔═════════════════════════╦══════════╦══════════╦═════════╦═════════╦═════════════════╗ \n" +
		"║           Nom           ║   Gold   ║ Pick lvl ║  Health ║  Armor  ║     Weapon      ║ \n" +
		"╠═════════════════════════╬══════════╬══════════╬═════════╬═════════╬═════════════════╣ \n")
	for re in res:
		nom  = sc.api_call("users.info",user=re[0])['user']['real_name']
		weapon =getuserweapon(mycursor,re[0])
		t = t + "║" +str(nom.ljust(25, ' '))[:25] +"║"+ str(re[1]).ljust(10, ' ') +"║"+ str(re[2]).ljust(10, ' ') +"║"+ str(re[4]).ljust(9, ' ')+"║"+ str(re[5]).ljust(9, ' ')+"║"+ str("["+str(weapon[0])+"]"+weapon[1]).ljust(17, ' ')+"║ \n"
	t =(t +
		"╚═════════════════════════╩══════════╩══════════╩═════════╩═════════╩═════════════════╝"+
		" ```")
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=t)

def gettopscore(mycursor):
	mycursor.execute("select * from uti order by score desc LIMIT 5")
	return mycursor.fetchall()