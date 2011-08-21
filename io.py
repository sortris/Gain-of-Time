#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011
import characters.character as character
import skills.skill as skill
import skills.skills

def loadSavedGame():
	filename = raw_input("Podaj imię postaci:")
	plik = open(filename+".txt", "r")
	linie = plik.readlines()
	imie = linie[0].strip()
	char = character.Character(imie)
	for linia in linie:
		items = linia.split(" ")
		if len(items) > 1:
			sk = skills.skills.getSkill(items[0], float(items[1]))
			#sk = skill.Skill(items[0], items[1])
			char.addSkill(sk)
	
	plik.close()
	return char

def saveGame(char):
	filename = char.name
	plik = open(filename+".txt", "w+")
	plik.write(char.name+"\n")
	for skill in char.skills:
		plik.write(skill.name+" "+str(skill.value)+"\n")
	plik.close()
