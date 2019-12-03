#!/usr/bin/python
# -*- coding: latin-1 -*-
import re

def minehelp(sc,slack_message):
	g = re.match('^(!minehelp|!mhelp) (.*)',str(slack_message.get("text")))
	if not g:
		helpmine(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpmineshow(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpminegive(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpminebet(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpminepick(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpminetop(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpminekill(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpmineshop(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
		helpmineweapon(sc,slack_message)
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="\n\n")
	elif g.group(2)=="mine": helpmine(sc,slack_message)
	elif  g.group(2)=="show": helpmineshow(sc,slack_message)
	elif  g.group(2)=="give": helpminegive(sc,slack_message)
	elif  g.group(2)=="bet": helpminebet(sc,slack_message)
	elif  g.group(2)=="pick": helpminepick(sc,slack_message)
	elif  g.group(2)=="top": helpminetop(sc,slack_message)
	elif  g.group(2)=="kill": helpminekill(sc,slack_message)
	elif  g.group(2)=="shop": helpmineshop(sc,slack_message)
	elif  g.group(2)=="weapon": helpmineweapon(sc,slack_message)


def helpmine(sc,slack_message):
		sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="To gain gold type ```!mine``` ")
def helpmineshow(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="To show people how much gold you have ```!mineshow```")
def helpminegive(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="To give gold to people use ```!minegive @user x``` Where x is a number and @user the tag of an user ")
def helpminebet(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text="To bet gold use ```!minebet x``` Where x is a number."
					" 60% lose all | 30% double bet | 8% triple bet | 2% win *MEGA JACKPOT™* ")
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=" The *MEGA JACKPOT™* is 50% of all loses from bets. \n You need to bet at least 10% of the mega jackpot or 100 gold to have a chance to win it. ```!minebet megajackpot```")
def helpminepick(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=" To know the level of your pickaxe and the cost for upgrade use ```!minepick``` To buy an upgrade use ```!minepick buy```")
def helpminetop(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=" To know the current Top 5 players use ```!minetop```")
def helpminekill(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=" To kill a user use: ```!minekill @user``` You need to have more gold than your target. \n You have 10% chance to kill that user, if you succed you will steal all his gold but if you fail you will lose all yours.")
def helpmineshop(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=" To see the list of weapons available use: ```!mineshop``` To buy a weapon use ```!mineshop buy x``` Where x is the id of the weapon you want to buy.")
def helpmineweapon(sc,slack_message):
	sc.api_call("chat.postMessage",channel=slack_message.get("channel"),text=" To see what weapon you have use: ```!mineweapon``` The combat system will be as follow: \nThe combat is started by initiating 2 speed meters for each opponents.\n We then increment each meters by the weapon speed of each weapon. \n Then the players which has the lowest speed meter value attacks and add it to a speed meter then the user.\n When you attack you will deal the damage of your weapon with a chance to miss depending on your hit chance.\n Then, we add up the speed value of your weapon to your speed meter and check if its lower than the enemy speed meter.\n If it is you, you will attack again. If not, the enemy attacks and we add the value of his speed weapon to his speed meter.\n We then check which has the lowest value in his speed meter and that person attacks... \n")
