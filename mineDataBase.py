#!/usr/bin/python
# -*- coding: latin-1 -*-

import mysql.connector


def checkuser(mycursor,id):
	try:
		res = mycursor.execute("select id,score from uti where id = '"+id+"'")
		res= mycursor.fetchone()
		if res is None:
			return False
		else:
			return True
	except mysql.connector.Error:
		pass
	return False

def getuser(mycursor,id):
	mycursor.execute("select * from uti where id = '"+id+"'")
	return mycursor.fetchone()


def addgold(mycursor,id,amount,cnx):
	if checkuser(mycursor,id):
		mycursor.execute("UPDATE uti SET score = score+"+ str(amount) +" WHERE id like '"+ id+"'")
	else:
		mycursor.execute("insert into uti(id,score) values('"+id+"',1)")
		mycursor.execute("UPDATE uti SET score = score+"+ str(amount) +" WHERE id like '"+ id+"'")
	cnx.commit()

def lessgold(mycursor,id,amount,cnx):
	if checkuser(mycursor,id):
		mycursor.execute("UPDATE uti SET score = score-"+ str(amount) +" WHERE id like '"+ id+"'")
	else:
		mycursor.execute("insert into uti(id,score) values('"+id+"',1)")
		mycursor.execute("UPDATE uti SET score = score-"+ str(amount) +" WHERE id like '"+ id+"'")
	cnx.commit()

def getmegajacpot(mycursor):
	mycursor.execute("select amountbet from argentbet where idbet=1")
	return int(mycursor.fetchone()[0])

def videjackpot(mycursor,cnx):
	mycursor.execute("UPDATE argentbet SET amountbet = 0 WHERE idbet=1")
	cnx.commit()

def addjackpot(mycursor,cnx,amount):
	mycursor.execute("UPDATE argentbet SET amountbet = amountbet+" +str(amount) +" WHERE idbet=1")
	cnx.commit()

def getpick(mycursor,id):
	mycursor.execute("select id,score,pick from uti where id = '"+id+"'")
	res = mycursor.fetchone()
	return res

def upgradePick(mycursor,id,cnx):
	mycursor.execute("UPDATE uti SET pick = pick+1 WHERE id like '"+ id+"'")

def getNumberMining(mycursor,id,cnx):
	mycursor.execute("select count(*) from historique_mining where temps between DATE_SUB(now(),INTERVAL 1 MINUTE) and now() and  id='"+ id+"'")
	res = mycursor.fetchone()
	return res

def resetPick(mycursor,id,cnx):
	mycursor.execute("UPDATE uti SET pick = 1 WHERE id like '"+ str(id)+"'")
	mycursor.execute("DELETE FROM historique_mining WHERE id like '"+ str(id)+"'")
	cnx.commit()


def getLastKilling(mycursor,id,id2,cnx):
	mycursor.execute("select TIME_FORMAT(DATE_ADD(temps,INTERVAL 1 HOUR),'%H:%i') from historique_killing where temps between DATE_SUB(now(),INTERVAL 1 HOUR) and now() and  id='"+ id+"' and target ='"+ id2+"' order by temps desc")
	res = mycursor.fetchone()
	return res


def getuserweapon(mycursor,id):
	mycursor.execute("select w.* from weaponlist w INNER JOIN uti u ON u.idweapon=w.id WHERE u.id like '"+str(id)+"'")
	return mycursor.fetchone()

def getweaponlist(mycursor):
	mycursor.execute("select * from weaponlist order by id")
	return mycursor.fetchall()

def getweaponprice(mycursor,idw):
	mycursor.execute("select cost from weaponlist where id like '"+idw+"'")
	return mycursor.fetchone()

def getweapon(mycursor,idw):
	mycursor.execute("select * from weaponlist where id like '"+str(idw)+"'")
	return mycursor.fetchone()

def checkweaponprice(mycursor,idw):
	mycursor.execute("select * from weaponlist where id like '"+idw+"'")
	return mycursor.fetchone()

def buyweapon(mycursor,cnx,id,idw):
	mycursor.execute("UPDATE uti SET idweapon = '"+ str(idw)+"' WHERE id like '"+str(id)+"'")
	return mycursor.fetchone()



#######MOD#######
def MODsetgold(mycursor,amount,cnx,id):
	mycursor.execute("UPDATE uti SET score = "+ str(amount) +" WHERE id like '"+ id+"'")
	cnx.commit()