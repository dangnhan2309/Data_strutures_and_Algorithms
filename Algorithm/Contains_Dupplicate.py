class Contains_Dupplicate:
	def hasDuplicate(self,nums):
		set_Nums = set(nums)
		return len(set_Nums) !=len(nums)

if __name__ =='__main__':
	
	raws = input()
	num = [int(x.strip()) for x in raws.split(',')]	

	Dupplicate = Contains_Dupplicate()

	print(Dupplicate.hasDuplicate(num))
