# FIBONACCI 
# Recursive (naive)
def fibonacci(n):
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

# Memoization (Top-Down DP)
def fib_memoization(n, memo):
    if n in memo: 
        return memo[n]
    if n <= 1: 
        return n 
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

def main(): 
    n = 4
    memo = {}
    print("Naive Style: " + str(fibonacci(n)))
    print("Memoization Style O(n): " + str(fib_memoization(n, memo)))

if __name__ == '__main__':
    main()
# FIBONACCI 
# Recursive (naive) -> basic O(n^2)
def fibonacci(n):
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

# Memoization (Top-Down DP,) O(n)
def fib_memoization(n, memo):
    if n in memo: 
        return memo[n]
    if n <= 1: 
        return n 
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]
def fib_space_op(n):
	if n <= 1 :
		return
	a,b = 0,1 
	for _ in range(2,n+1):
		a,b = b , a+b
		print(a,b)

	return b 


def main(): 
    n = 4
    memo = {}
    print("Naive Style: " + str(fibonacci(n)))
    print("Memoization Style O(n): " + str(fib_memoization(n, memo)))
    print("Space Optimize Style O(n): " + str(fib_space_op(n)))


if __name__ == '__main__':
    main()


