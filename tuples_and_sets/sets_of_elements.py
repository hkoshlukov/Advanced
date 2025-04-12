n, m = input().split()
set_n = set(int(input()) for n in range(int(n)))
set_m = set(int(input()) for m in range(int(m)))
print(*set_n.intersection(set_m), sep='\n')
