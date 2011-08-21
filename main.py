#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011
import creatingCharacter, io, characters.character, skills.hiding as hiding

x = int(raw_input("Witaj, co chcesz zrobić?\n1. Stwórz nową postać\n2. Coś innego\n3.Wczytać grę\n"))

if x == 1:
	creatingCharacter.createCharacter()
elif x == 2:
	print "haha"
elif x == 3:
	character = io.loadSavedGame()
	print "Dodaję skill hida"
	print character
	print character.name
	if len(character.skills) < 1:
		hid = hiding.Hiding(25)	
		character.addSkill(hid)
	character.skills[0].train()
	io.saveGame(character)

else:
	print "no szkoda :("
