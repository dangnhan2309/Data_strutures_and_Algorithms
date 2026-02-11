class Anagra:
	def hasAnagram(self,t,s):
		print(sorted(s))
		print(sorted(t))
		return sorted(t) == sorted(s)
if __name__ =="__main__":
	set_1_raws= input()
	set_2_raws= input()
	check = Anagra()
	print(check.hasAnagram(set_1_raws,set_2_raws))

