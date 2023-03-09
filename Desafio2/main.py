num = 11
fib = [0, 1]

for i in range(2, num + 1):
    fib.append(fib[i-1] + fib[i-2])

print(f'O número {num} pertence a sequência de fibonacci? {num in fib}')

