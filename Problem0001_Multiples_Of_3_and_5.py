





listMultiplesOF3=set(range(3,1000,3))
listMultiplesOF5=set(range(5,1000,5))
listMultiplesOF3_5 = listMultiplesOF3.intersection(listMultiplesOF5)
print sum(listMultiplesOF3)+sum(listMultiplesOF5)-sum(listMultiplesOF3_5)
