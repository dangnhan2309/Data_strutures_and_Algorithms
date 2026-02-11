class TwoSum():
	def find_twosum(self,target:int,nums:list[int]):
		len_= int(len(nums)) -1
		check=0
		while True:
			checkpoint= len_-check
			result= target - int(nums[checkpoint])
			if result > 0 and nums.index(result)>0:
				return [nums.index(result),checkpoint]
			check =+1 
			if check == len_ -1:
				return None
		return None
if __name__=="__main__":
	t = TwoSum()
	list_raw = input()
	list_ = [int(i.strip()) for i in list_raw.split(",")]
	target = int(input())
	print(t.find_twosum(target,list_))


