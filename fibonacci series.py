from functools import lru_cache  #import lru catch to spped up

@lru_cache  # Use @lru_catch to speed up
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n -1) + fib(n - 2)
    
for i in range(0, 40):
    print(f'{i}: {fib(i)}')