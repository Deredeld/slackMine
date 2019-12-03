#!/usr/bin/python
# -*- coding: latin-1 -*-
from mining import *

def mine(sc,slack_message,mycursor,cnx):
	if checkuser(mycursor,slack_message.get("user")):
		pass
	else:
		try:
			mycursor.execute("insert into uti(id,score) values('"+slack_message.get("user")+"',1)")
			cnx.commit()
		except mysql.connector.Error as err:
			pass
	luck = 10
	n = randint(1,luck)
	user = getuser(mycursor,slack_message.get("user"))
	if n==luck:
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="<@"+(slack_message.get("user")+ "> just found a gold vein and gained " +str(int(10)*int(user[2])))+ " gold")
		mycursor.execute("UPDATE uti SET score = score+"+ str(user[2]*10) +" WHERE id like '"+ str(user[0])+"'")
	else:
		mycursor.execute("UPDATE uti SET score = score+"+ str(user[2]) +" WHERE id like '"+ str(user[0])+"'")
	if (getNumberMining(mycursor,str(user[0]),cnx)[0]>=12000):
		resetPick(mycursor,user[0],cnx)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="<@"+(slack_message.get("user")+ "> 's pickaxe broke because he mined to much"))
	mycursor.execute("insert into historique_mining(id,type_action) values('"+ str(user[0])+"','mining')")
	cnx.commit()
	#sc.api_call("chat.postEphemeral",channel=slack_message.get("channel"),text="You now have "+str(int(user[1]+user[2]))+ " gold",user=slack_message.get("user"),as_user="true")
