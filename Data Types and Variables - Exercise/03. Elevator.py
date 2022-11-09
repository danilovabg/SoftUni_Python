import math
def elevator(N,P):
    result = math.ceil(N/P)
    return result
N = int(input())
P = int(input())
print(elevator(N, P))