#!/usr/bin/python
# -*- coding: latin-1 -*-

class Weapon:
  def __init__(self, id, name,damage,speed,hitChance,cost,dps):
  	self.id=int(id)
  	self.name=name
  	self.damage=int(damage)
  	self.speed=int(speed)
  	self.hitChance=int(hitChance)
  	self.cost=int(cost)
  	self.dps=int(dps)