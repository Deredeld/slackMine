#!/usr/bin/python
# -*- coding: latin-1 -*-


from mineDataBase import checkuser,getuser,lessgold
from mineshop import getuserweapon
def mineshow(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		re =getuser(mycursor,slack_message.get("user"))
		t =("```" +
		"╔═════════════════════════╦══════════╦══════════╦═════════╦═════════╦═════════════════╗ \n" +
		"║           Nom           ║   Gold   ║ Pick lvl ║  Health ║  Armor  ║     Weapon      ║ \n" +
		"╠═════════════════════════╬══════════╬══════════╬═════════╬═════════╬═════════════════╣ \n")
		nom  = sc.api_call("users.info",user=re[0])['user']['real_name']
		weapon =getuserweapon(mycursor,re[0])
		t = t + "║" +str(nom.ljust(25, ' '))[:25] +"║"+ str(re[1]).ljust(10, ' ') +"║"+ str(re[2]).ljust(10, ' ') +"║"+ str(re[4]).ljust(9, ' ')+"║"+ str(re[5]).ljust(9, ' ')+"║"+ str("["+str(weapon[0])+"]"+weapon[1]).ljust(17, ' ')+"║ \n"
		t =(t +
		"╚═════════════════════════╩══════════╩══════════╩═════════╩═════════╩═════════════════╝"+
		" ```")
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=t)

def mineshowweapon(sc,slack_message,mycursor,cnx):
	re =getuserweapon(mycursor,slack_message.get("user"))
	t ="```"+	"╔════╦═════════════════╦════════╦═══════╦════════════╦══════════╦═══════╗ \n"+"║ Id ║       Name      ║ Damage ║ Speed ║ HitChance% ║   Cost   ║  DPS  ║\n"+	"╠════╬═════════════════╬════════╬═══════╬════════════╬══════════╬═══════╣\n"
	t = t + "║" +str(re[0]).ljust(4, ' ') +"║"+ str(re[1]).ljust(17, ' ') +"║"+ str(re[2]).ljust(8, ' ') +"║"+ str(re[3]).ljust(7, ' ') +"║"+ str(re[4]).ljust(12, ' ') +"║"+ str(re[5]).ljust(10, ' ') +"║"+ str(re[6]).ljust(7, ' ') + "║ \n"
	t =t+ "╚════╩═════════════════╩════════╩═══════╩════════════╩══════════╩═══════╝"+	" ```"
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=t)
