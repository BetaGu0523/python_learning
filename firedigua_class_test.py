#-*-coding:utf-8-*-

class FireDiGua():
	"""A class for firedigua"""
	#属性
	def __init__(self,cookedlevel=0,condiments=[]):
		
		self.cookedlevel = cookedlevel
		
		self.cookedString =self.toString(self.cookedlevel)
		
		self.condiments = condiments
	
	def __str__(self):
		return "%s,%s"%(self.cookedString,self.condiments)

	#方法
	def cook(self, mins):
		'''cook for a while'''
		self.cookedlevel = self.cookedlevel + mins
		self.cookedString = self.toString(self.cookedlevel)
		
	def toString(self,cookedlevel):
		if self.cookedlevel>0 and self.cookedlevel < 3:
			return "生的"
		elif self.cookedlevel < 5:
			return "半生不熟"
		elif self.cookedlevel < 8:
			return "熟的"
		elif self.cookedlevel > 8:
			return "焦的"
		else:
		    print ("不合法！")

	def addCondiments(self,*condiments):
		self.condiments.append(condiments)

		
		

def main():
	di_gua  = FireDiGua()
	di_gua.cook(3)
	print (di_gua.cookedlevel)
	print (di_gua.cookedString)
	di_gua.addCondiments('fanqie','lajiao')
	print (di_gua.condiments)

	di_gua.cook(3)
	print (di_gua.cookedlevel)
	print (di_gua.cookedString)
	di_gua.addCondiments('jiemo')
	print (di_gua.condiments)

	di_gua.cook(3)
	print (di_gua.cookedlevel)
	print (di_gua.cookedString)
	di_gua.addCondiments('fanqie','lajiao')
	print (di_gua.condiments)

	print(di_gua)
if __name__ == "__main__":
	main()
