#!/usr/bin/python
# -*- coding: latin-1 -*-

from mineDataBase import checkuser,getuser,lessgold

def minearmor(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		user =getuser(mycursor,slack_message.get("user"))
	else:
		user[5] = 0
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You have a "+str(user[5])+ " armor. The next upgrade will cost "+str(pow(2,user[5])*user[5])+" gold. You have " +str(user[1]) +" gold")

def minearmorbuy(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		user =getarmor(mycursor,slack_message.get("user"))
		if user[1]>=pow(2,user[5])*user[5]:
			upgradearmor(mycursor,user[0],cnx)
			lessgold(mycursor,user[0],pow(2,user[5])*user[5],cnx)
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You now have a "+str(user[5]+1)+ " armor. The next upgrade will cost "+str(pow(2,(user[5]+1))*(user[5]+1))+" gold. You have " +str(user[1]-pow(2,user[5])*user[5]) +" gold")
		else:
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")
			minearmor(sc,slack_message,mycursor,cnx)
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")


def getarmor(mycursor,id):
	mycursor.execute("select * from uti where id = '"+id+"'")
	res = mycursor.fetchone()
	return res

def upgradearmor(mycursor,id,cnx):
	mycursor.execute("UPDATE uti SET armor = armor+1 WHERE id like '"+ id+"'")
