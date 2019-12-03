#!/usr/bin/python
# -*- coding: latin-1 -*-

from mineDataBase import *
from random import randint

def minekill(sc,slack_message,mycursor,cnx,g):
	if g.group(1) is None: target = g.group(2)
	else: target = g.group(1)
	if checkuser(mycursor,slack_message.get("user")):
		user =getuser(mycursor,slack_message.get("user"))
		if target is not None and checkuser(mycursor,target):
			targetData =getuser(mycursor,target)
			luck = 3
			n = randint(1,luck)
			result = getLastKilling(mycursor,user[0],targetData[0],cnx)
			if result is None:
				if user[1]>=targetData[1]:
					mycursor.execute("insert into historique_killing(id,target) values('"+ str(user[0])+"','"+ str(targetData[0])+"')")
					cnx.commit()
					print luck
					print n
					if n==luck :
						addgold(mycursor,user[0],targetData[1],cnx)
						lessgold(mycursor,targetData[0],targetData[1],cnx)
						sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=("You killed <@"+targetData[0]+"> and won " +str(targetData[1])+ " gold.").format())
					else:
						lessgold(mycursor,user[0],user[1],cnx)
						addjackpot(mycursor,cnx,user[1])
						sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=("You failed to kill <@"+targetData[0]+"> and lost "  +str(user[1])+ " gold.").format())
				else:
					sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold.")
			else:
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You already tried to kill this person, wait 1 hour between each attempts. Retry at "+str(result[0]))	
		else:
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="This target has no gold or does not exist.")


	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have gold. Type !mine to mine gold.")
