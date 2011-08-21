#-*- coding: utf-8 -*-
#
# author: Tobiasz Siemiński
# creation date: 21.08.2011
import skill, random, time

class Hiding(skill.Skill):
	def __init__(self, value = 0):
		self.name = "Hiding"
		self.value = value
		skill.__init__(self.name, self.value)

	def train(self):
		print "Trenujesz: "+self.name
		x = random.randint(0, 100)
		e = raw_input()
		print e
		while e != 'q':
			if x < self.value:
				print "Ukryłeś się"
				self.value += 0.1
				print "Twoja umiejętność in %s jest teraz równa %2.2f" %(self.name, self.value)
			else:
				print "Nie udało Ci się ukryć"
			time.sleep(2)
			x = random.randint(0, 100)
			e = raw_input()
			
