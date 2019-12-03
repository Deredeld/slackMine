#!/usr/bin/python
# -*- coding: latin-1 -*-

from mineDataBase import *
from random import randint

def minebet(sc,slack_message,mycursor,cnx,g):
	n = randint(1,100)
	if checkuser(mycursor,slack_message.get("user")):
		user =getuser(mycursor,slack_message.get("user"))
		if (g.group(1) is not None and g.group(1)=="all") or (g.group(2) is not None and g.group(2)=="all"):
			amount = int(user[1])
		elif g.group(1) is not None: 
			amount = int(g.group(1))
		else: amount = int(g.group(2))

		if int(user[1])>=int(amount) and int(amount)>0:
			jackpot = getmegajacpot(mycursor)
			if (n>=98 and (amount>=jackpot*0.1 or amount>=100)):
				addgold(mycursor,user[0],jackpot,cnx)
				videjackpot(mycursor,cnx)
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You won the *MEGA JACKPOT™* !!!! You won "+ str(jackpot) +" gold")
			elif (n>=90):
				addgold(mycursor,user[0],int(amount*2),cnx)
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You won the small jackpot !!!! You won "+str(amount*3) +" gold")
			elif (n>=63):
				addgold(mycursor,user[0],amount,cnx)
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You won "+str(amount*2) +" gold")
			else:
				lessgold(mycursor,user[0],amount,cnx)
				addjackpot(mycursor,cnx,int(amount*0.5))
				sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You lost "+str(amount) +" gold")
				if getmegajacpot(mycursor) > 100:
					minebet_jackpot(sc,slack_message,mycursor)
		else:
			sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")
	else:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="You don't have enough gold. Type !mine to mine gold")

def minebet_jackpot(sc,slack_message,mycursor):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="The *MEGA JACKPOT™* is at "+ str(getmegajacpot(mycursor))
		+" ! Bet *"+ str(min(int(getmegajacpot(mycursor)/10),100))+ "* to have a chance to win it !!")
