#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011

def createCharacter():
	name = raw_input("Podaj simię postaci:\n")
	file = open(name+".txt", 'w+')
	file.write(name)
	file.close()
	
