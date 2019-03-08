#-*-coding:utf-8-*-

class Cat():
	"""this is a cat class"""

	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def __str__(self):
		return "%s,%s"%(self.name,self.age)



	"""functions"""
	def eat(self):
		print (self.name + "is eating")
	
	def introduce(self):
		print ("%s is %s !"%(self.name,self.age))



def main():
	tom = Cat("tom",80)
	lanmao = Cat("lanmao",10)

	tom.eat()
	tom.introduce()
	print(tom)

	lanmao.eat()
	lanmao.introduce()
	print(lanmao)


if __name__ == "__main__":
	main()





