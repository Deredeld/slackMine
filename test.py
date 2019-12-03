#!/usr/bin/python
# -*- coding: latin-1 -*-

import mysql.connector
import time
import random

from mineDataBase import *
from minefight import *

from minetop import minetop
from slackclient import SlackClient
from random import randint
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
import datetime as dt


def main():
	config = {
	  'user': 'norman',
	  'password': 'root',
	  'host': '127.0.0.1',
	  'database': 'norman',
	  'raise_on_warnings': True,
	}
	
	cnx = mysql.connector.connect(**config)
	mycursor = cnx.cursor(buffered=True)

	proxies = dict(https="https://trendupdate:opla5271@proxy.cg49.fr:8080", http="http://trendupdate:opla5271@proxy.cg49.fr:8080")
	sc = SlackClient("xoxb-233810080487-407497712721-kwZkQKmYdZaoPDEDtlouy2S3", proxies=proxies)
	if sc.rtm_connect():

		while True:
			for slack_message in sc.rtm_read():
				if slack_message.get("type")=="message" and (slack_message.get("subtype")==None or  slack_message.get("subtype")!="bot_message" or slack_message.get("subtype")!="message_changed"):
#mine fight
					g = re.match('^!mfight <@([A-Z0-9]{0,9})>',str(slack_message.get("text")))
					if g:
						minefight(sc,slack_message,mycursor,cnx,g)
	cnx.close()




if __name__ == '__main__':
	main()