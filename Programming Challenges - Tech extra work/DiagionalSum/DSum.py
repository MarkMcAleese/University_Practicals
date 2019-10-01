import sys


def countDiag( matrix , startIndex  ,  updateIndex ) :

    coloumCount = startIndex 
    sum = 0
    for row in matrix : 
        sum  = sum + row[coloumCount]    
        coloumCount = updateIndex( coloumCount )
        
    return sum

def PosMove( currentIndex  ) :
    return currentIndex + 1

def NegMove( currentIndex  ) :
    return currentIndex - 1

#n = int(raw_input().strip())
#a = []
#for a_i in xrange(n):
#   a_temp = map(int,raw_input().strip().split(' '))
#   a.append(a_temp)

a = [11,2,4]
b = [4,5,6]
c = [10,8,-12]

n = 3
final = []
final.append( a )
final.append( b)
final.append( c)

posSum =  countDiag( final , 0 , PosMove )
negSum =  countDiag( final , n  - 1, NegMove )
print abs(posSum - negSum)