#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011

def createCharacter():
	#KOMENTARZ DLA TESTU
	name = raw_input("Podaj imię postaci:\n")
	file = open(name+".txt", 'w+')
	file.write(name)
	file.close()
	
