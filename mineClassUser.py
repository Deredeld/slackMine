#!/usr/bin/python
# -*- coding: latin-1 -*-

class User:
  def __init__(self, id, score,pick,idweapon,health,armor):
  	self.id=id
  	self.score=int(score)
  	self.pick=int(pick)
  	self.idweapon=int(idweapon)
  	self.health=int(health)
  	self.armor=int(armor)
