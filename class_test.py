# -*-coding:utf-8-*-
class Dog():
	def __init__(self,name,age):
		self.name = name
		self.__age = age

	def __str__(self):
		return "%s,%s"%(self.name,self.__age)

	def __del__(self):
		print ("dog sleeping!")

	def __setage(self,age):
		self.__age = age

	def setage(self,age):
		if age >= 0 and age <= 100:
			self.__setage(age)
		else:
			print ("age must be between 0-100")
	def getage(self):
		return self.__age


def main():
	dog1 = Dog("wangcai",10)
	dog2 = Dog("xiaobai",23)
	print (dog1)
	dog1.setage(1022)
	del(dog1)
	dog2.setage(5)
	print(dog2.getage())
	del(dog2)
	


if __name__ == "__main__":
	main()


