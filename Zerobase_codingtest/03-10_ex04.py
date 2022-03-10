def solution(useageArr, fee):

    totalFee = 0
    for each in useageArr:
        totalFee += each * fee
        
    return totalFee
