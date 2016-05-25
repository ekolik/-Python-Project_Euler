targetK = 12000
limitK = targetK * 2
results = [2*limitK] * limitK


def prodsum(prodOfDivisors, sumOfDivisors, numOfDivisors, addDivisorFrom):
    localK = prodOfDivisors - sumOfDivisors + numOfDivisors
    if localK < limitK:
        if prodOfDivisors < results[localK]:  ## prodOfDivisors is equal to the number itself that we are looking for
            results[localK] = prodOfDivisors
        for newDivisor in range(addDivisorFrom, (limitK//prodOfDivisors) * 2):
            prodsum(prodOfDivisors * newDivisor, sumOfDivisors + newDivisor, numOfDivisors + 1, newDivisor)


prodsum(1, 1, 1, 2)
print(sum(set(results[2:targetK+1])))
