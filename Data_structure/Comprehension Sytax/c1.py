# giving a number n create a list of squares of the number 
# from 1 to n 

def s1(n): 
	squares=[]
	for k in range(1,n+1): 
		squares.append(k*k)
	return squares
def s2(n):
	squares =[k*k for k in range(1,n+1)]
	return squares


def main ():
	n=3
	print(f"This is Comprehension Syntax Example:n = {n} ")
	print(f"This is method 1 result: standar ways {s1(n)}")
	print(f"This is method 2 result: using syntax {s2(n)}")
if __name__ == "__main__":
	main()