def maxCommonDivisor(p, q):
    print(p, q)
    if q == 0:
        return p
    else:
        return maxCommonDivisor(q, p % q)

if __name__ == '__main__':
    print(maxCommonDivisor(123123123, 12121212))