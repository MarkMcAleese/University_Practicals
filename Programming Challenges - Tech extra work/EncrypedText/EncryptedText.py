import math


def splitIntoEncrpytMatrix( testString , rowSize ) :
    stringLen = len( testString )
    
    currentIndex = 0
    matrix = []
    currentRow = []
    for letter in testString :
        currentRow.append( letter )
        currentIndex = currentIndex + 1
        
        if ( currentIndex == rowSize ) : 
            currentIndex = 0
            matrix.append( currentRow )
            currentRow = []
      
      
    if ( len( currentRow) != 0 ) :
        matrix.append( currentRow )  
      
    return matrix



def printResult( matrix , rowSize ) :
    line = ""
    for index in range( 0 , rowSize ) : 

        for row in matrix : 
            if len( row ) > index : 
               line = line + row[index]
        line = line + " "
        
    print line

def main():
    #testString = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
    testString = "feedthedog"
    testString = testString.strip()

    stringLen = len(testString)
    print stringLen 
    root = math.sqrt( stringLen )
    topRoot = int(math.ceil( root ) )
    
    matrix = splitIntoEncrpytMatrix( testString , topRoot )
    
 
   
    printResult( matrix , topRoot )
   
   

main()

