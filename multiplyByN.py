def multiply_direct(N, M):
    return N * M

def multiply_repeated_addition(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

N = 2
M = 3
print("Direct multiplication result:", multiply_direct(N, M))
print("Repeated addition result:", multiply_repeated_addition(N, M))
