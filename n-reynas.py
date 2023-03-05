import math

v = [1, 2, 0, 2]

def ataques(n):
    a = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] == v[j]:
                a += 2
                return a
            if abs(i-j) - abs(v[i]-v[j]) == 0:
                a += 2
                return a
            print(a)
    return a

if __name__ == "__main__":
    print("Ingrese n")
    n = int(input())
    print(ataques(n))