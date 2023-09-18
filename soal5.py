A = {'a', 'b', 'c', 'd'} 
B = {'c', 'd', 'e' } 
C = {}
#A symmetric difference B 
print(A^B)
#B symmetric difference A 
print(B^A)
#A symmetric difference C 
print(A.symmetric_difference(C))
#B symmetric difference C
print(B.symmetric_difference(C))