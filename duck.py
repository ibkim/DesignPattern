import sys
import os

class QuackBehavior:
	def quack(self):
		raise NotImplementedError ("Quck Method not implemented")

class FlyBehavior:
	def fly(self):
		raise NotImplementedError ("Fly Method not implemented")

class FlyWithWings (FlyBehavior):
	def fly(self):
		print "Fly~~~ I can fly~"

class FlyNoWay (FlyBehavior):
	def fly(self):
		pass

class Quack (QuackBehavior):
	def quack(self):
		print "Quack! Quack!"

class Squeak (QuackBehavior):
	def quack(self):
		print "ppppppp"

class MuteQuack (QuackBehavior):
	def quack(self):
		pass

class Duck:
	quackAction = None
	flyAction = None

	def display(self):
		raise NotImplementedError ("Display method not implemented")

class MallardDuck (Duck):
	def __init__ (self):
		Duck.quackAction = Quack()
		Duck.flyAction = FlyWithWings()

	def performQuack(self):
		Duck.quackAction.quack()

	def performFly(self):
		Duck.flyAction.fly()

	def display(self):
		print "Mallarrrrd~"

class RedHeadDuck (Duck):
	def __init__ (self):
		quackAction = Squeak()
		flyAction = FlyNoWay()

	def performQuack(self):
		quackAction.quack()

	def performFly(self):
		flyAction.fly()

	def display(self):
		print "I have Red hair~"

mall = MallardDuck()
red = RedHeadDuck()

mall.performFly()

