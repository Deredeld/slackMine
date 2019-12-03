#!/usr/bin/python
# -*- coding: latin-1 -*-

from mineDataBase import checkuser,getuser,lessgold

def minehealth(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		user =getuser(mycursor,slack_message.get("user"))
	else:
		user[4] = 0
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You have a "+str(user[4])+ " health. The next upgrade will cost "+str(pow(2,user[4])*user[4])+" gold. You have " +str(user[1]) +" gold")

def minehealthbuy(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		user =gethealth(mycursor,slack_message.get("user"))
		if user[1]>=pow(2,user[4])*user[4]:
			upgradehealth(mycursor,user[0],cnx)
			lessgold(mycursor,user[0],pow(2,user[4])*user[4],cnx)
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You now have a "+str(user[4]+1)+ " health. The next upgrade will cost "+str(pow(2,(user[4]+1))*(user[4]+1))+" gold. You have " +str(user[1]-pow(2,user[4])*user[4]) +" gold")
		else:
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")
			minehealth(sc,slack_message,mycursor,cnx)
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")

def gethealth(mycursor,id):
	mycursor.execute("select * from uti where id = '"+id+"'")
	res = mycursor.fetchone()
	return res

def upgradehealth(mycursor,id,cnx):
	mycursor.execute("UPDATE uti SET health = health+1 WHERE id like '"+ id+"'")
