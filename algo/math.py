# 筛质数

# 埃氏筛
# 埃氏筛
MX = 10**6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False
primes.extend((MX, MX))  # 保证下面下标不会越界


# 线性筛(欧拉筛)
MX = 10**6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        if i * p >= MX:
            break
        is_prime[i * p] = False
        if i % p == 0:
            break
primes.extend((MX, MX))  # 保证下面下标不会越界
