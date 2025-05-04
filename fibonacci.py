def fibonacci(n):
    fiblist=[]
    a=0
    b=1
    for _ in range(n):
        fiblist.append(a)
        a,b=b,a+b
    return fiblist
print(fibonacci(6))