import math


def printMatrix( matrix ) :
    for row in matrix : 
        print row
            
def CreateTextMatrix( xSize , ySize ) : 
    matrix = []
    
    for x in range( 0 , xSize ) :
        matrix.append( [] ) 
        for y in range( 0 , ySize ) :
            matrix[x].append(x + y)    
    
    return matrix
  
def ShouldStop( min , max ) :
    return min >= max

def MarkMatrix( matrix , newMatrix , startX , endX , startY , endY , depth , numRot ) :
     newMatrix = MarkRow( matrix , newMatrix , 0 , 3 , 0 , 0 , 3 , depth , 1 )
     newMatrix = MarkRow( matrix , newMatrix , 0 , 3 , 3   , 0 , 3 , depth , 1 )
     matrix = MarkColumn( startX , startY , endY , matrix , depth  )
     matrix = MarkColumn( endX - 1 , startY , endY  , matrix , depth  )
     return newMatrix

def MarkDepths( startX , endX , startY , endY , depth , matrix , newMatrix  , numRot ) :
    
    xSize = endX - startX
    ySize = endY - startY 
    
    stop = False    
    if ( xSize < ySize ) :
        stop = ShouldStop( startX , endX )
    else : 
        stop = ShouldStop( startY , endY )
    
    if  stop :
        return matrix
    else :
        newMatrix = MarkMatrix( matrix , newMatrix , startX , endX , startY , endY , str(depth) , numRot  )
        newMatrix = MarkDepths( startX + 1 , endX - 1 , startY + 1 , endY - 1 , depth + 1 , matrix , newMatrix , numRot)
        return newMatrix
        
def MarkRow( matrix , newMatrix , topRow , bottomRow , currentRow ,  startX , endX  , val , numRot ) :
    for x in  range( startX , endX ) :
        newX = x
        newY = currentRow
        for rot in range( 0 , numRot ) :
            
            if newX == startX and newY != bottomRow : 
                newY = newY + 1 
            elif newX == endX and newY != topRow :  
                newY = newY - 1
            elif newY == bottomRow :
                newX = newX + 1
            else :
                newX = newX - 1
          
        
        newMatrix[newY][newX] = str(matrix[currentRow][x]) 
        
    return newMatrix




def MarkColumn( xVal , startY , endY , matrix , val ) :
    for col in range( startY , endY ) :
        matrix[col][xVal] = val
    return matrix 
    
    
def MapoutMatrix( matrixToMap , xSize , ySize , newMatrix ,  rot ) :
    matrixToMap = MarkDepths( 0 , xSize  , 0 , ySize - 1 , 1,  matrixToMap , newMatrix , 1 )
    return matrixToMap


xSize = 4
ySize = 4
numOfRotations = 1
testMatrix = CreateTextMatrix( xSize , ySize  )
printMatrix( testMatrix )
newMatrix = CreateTextMatrix( xSize , ySize )
newMatrix = MapoutMatrix( testMatrix , xSize , ySize , newMatrix ,  numOfRotations  )
printMatrix( newMatrix )



