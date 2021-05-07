def binomial(N, k, p):
    if N == 0 and k == 0:
        return 1.0
    if N < 0 or k < 0:
        return 0.0
    return (1.0-p) * binomial(N-1, k, p) + p * binomial(N-1, k-1, p)

if __name__=='__main__':
    import time
    startTime = time.time()
    print(binomial(100, 50, 0.25))
    print(time.time()-startTime)