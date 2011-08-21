#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011
import hiding

def getSkill(name, value):
	if name == "Hiding":
		return hiding.Hiding(value)
