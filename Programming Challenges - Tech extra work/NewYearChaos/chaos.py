

gNumSteps = 0

def main(): 

    sizeOfLine = 5
    firstLine = [2,1,5,3,4]
    global gNumSteps
    
    if checkIfPossible( firstLine ) == False :
        return
    
    currentIndex = isLineCorrect( firstLine, sizeOfLine )
    while ( currentIndex != -1 ) :
        firstLine = sortLine( 0 , firstLine , sizeOfLine )
        currentIndex = isLineCorrect( firstLine, sizeOfLine )
        
    print gNumSteps

    
    
def checkIfPossible( line ) :

    expectedVal = 1 
    
    for index in range( 0 , len( line) ) :
        currentVal =  line[index]
        diff = currentVal - expectedVal 
        
        if diff > 2 : 
            print "Cant be done "
            return False 
        else :
            expectedVal = expectedVal + 1
  
    
def isLineCorrect( line , size ) :
    expectedVal = 1 
    for index in range( 0, size  )  :
        if line[index] != expectedVal :
            return index
        expectedVal = expectedVal + 1 
    return -1


def sortLine( startIndex , line , size ) : 

    global gNumSteps
    
    currentIndex = startIndex
    expectedVal = startIndex + 1
    while currentIndex < size  :
        currentVal = line[currentIndex ]
        
        if currentVal == expectedVal :
            currentIndex = currentIndex + 1
            expectedVal = expectedVal + 1
        else :

            if  currentIndex < ( size - 1 ) :
                gNumSteps = gNumSteps + 1
                line[currentIndex] = line[currentIndex + 1]
                line[currentIndex + 1 ] = currentVal
                
            currentIndex = currentIndex + 1 
            expectedVal = expectedVal + 1

    return line
    
 
main()
    
    
    


