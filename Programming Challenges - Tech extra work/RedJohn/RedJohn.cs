
/* Problem
Red John has committed another murder. But this time, he doesn’t leave a red
smiley behind. What he leaves behind is a puzzle for Patrick Jane to solve.
 He also texts Teresa Lisbon that if Patrick is successful, he will turn himself
  in. The puzzle begins as follows.

There is a wall of size CxN in the victim’s house where C is the 1st composite
number. The victim also has an infinite supply of bricks of size Cx1 and 1xC in
her house. There is a hidden safe which can only be opened by a particular 
configuration of bricks on the wall. In every configuration, the wall has to be
completely covered using the bricks. There is a phone number written on a note in
the safe which is of utmost importance in the murder case. Gale Bertram wants to
know the total number of ways in which the bricks can be arranged on the wall
so that a new configuration arises every time. He calls it M. 

Since Red John is back after a long time, he has also gained a masters degree in
Mathematics from a reputed university. So, he wants Patrick to calculate the
number of prime numbers (say P) up to M (i.e. <= M). If Patrick calculates P,
Teresa should call Red John on the phone number from the safe and he will
surrender if Patrick tells him the correct answer. Otherwise, Teresa will get 
another murder call after a week.

You are required to help Patrick correctly solve the puzzle.

Sample Input
The first line of input will contain an integer T followed by T lines each 
containing an integer N.

Sample Output
Print exactly one line of output for each test case. The output should contain 
the number P.
*/
using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    
    static void Main(String[] args) {
        
        int numTestCases = int.Parse( Console.ReadLine() );
            
        numBricks.Add( 1 , 1);
        numBricks.Add( 2, 1 );
        numBricks.Add( 3, 1 );
        numBricks.Add( 4 , 2);

        primes.Add( 2);
        
        for ( int i =0; i < numTestCases; i++ )
        {
            int bricks = int.Parse( Console.ReadLine() );
            
            int numMoves = GetNumOfPossiblities( bricks);
           Console.WriteLine( GetNumOfPrimesBefore( numMoves) );
        
        }
    }
    
    static Dictionary<int,int> numBricks = new Dictionary<int,int>();
    static int highestBricks = 4;
    static public int GetNumOfPossiblities( int bricks )
    {
        if ( bricks <= 3)
            return 1;
        
        if ( bricks == 4 )
            return 2;
        
        if ( bricks <= highestBricks)
        {
            return numBricks[bricks];
        }
            
        for ( int i = highestBricks + 1; i <= bricks; i++)
        {
            int newMoves = numBricks[i - 1] + numBricks[i-4];
            numBricks.Add(i,newMoves);
        }
        highestBricks = bricks;
        return numBricks[bricks];
    }
    
    static List<int> primes = new List<int>();
    static public int GetNumOfPrimesBefore( int num )
    {
        if ( num <= 1)
            return 0;
        
        if ( num <= 2)
            return 1;
               
        if ( num < highestPrimeCheck )
        {
           int count = 0;
           foreach( int prime in primes )
           {
               if ( prime > num )
               {
                   return count;
               }
               count++;
           }
           return count;
        }
        
        GenerateNewPrimes( num );
            
        return primes.Count;
 
    }
 
    static int highestPrimeCheck = 3;
    static void GenerateNewPrimes( int checkUpTo )
    {
        for ( int i = highestPrimeCheck; i <= checkUpTo; i+= 2 )
        {            
            bool isPrime  = true;
          
            foreach( int prime in primes)
            {       
                if ( i % prime == 0)
                {       
                    isPrime = false;
                   break;
                }
            }
            if ( isPrime )
            { 
                primes.Add( i );
            }
        }
   
        if ( checkUpTo % 2 == 0 )
        {
            highestPrimeCheck = checkUpTo + 1;
        }
        else
        {
            highestPrimeCheck = checkUpTo;
        }
    }    
}
