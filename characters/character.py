#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011


"""Postać po prostu"""
class Character(object):
	def __init__(self, name = "defaultName", skills = []):
		self.name = name
		self.skills = skills
		

	def addSkill(self, skill):
		self.skills.append(skill)

	def __repr__(self):
		repr = "Imię: %s" %(self.name)
		i = 1
		for skill in self.skills:
			repr += "Umiejętność %d %s" %(i, skill.name)
			i=+1
		return repr
		
