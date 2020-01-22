def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# bottom-up approach
def fibonacci2(n):
    arr = [0, 1]
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

# recursion with memo-ization
def fibonacciMemo(n, memo):
    memo[0] = 0
    memo[1] = 1
    if n in memo:
        return memo[n]
    result = fibonacciMemo(n-1, memo) + fibonacciMemo(n-2, memo)
    memo[n] = result
    return result

n = int(input())
print(fibonacci(n))

