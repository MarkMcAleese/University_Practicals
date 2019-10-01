
/* Problem
	Given N integers, count the total pairs of integers that have a difference of K.

	Input Format 
	1st line contains N & K (integers).
	2nd line contains N numbers of the set. All the N numbers are assured to be distinct.

	Output Format	
	One integer saying the number of pairs of numbers that have a diff K.

	Constraints:
	N <= 10^5
	0 < K < 10^9
	Each integer will be greater than 0 and at least K away from 2^31-1
*/

using System;
using System.Collections.Generic;
using System.IO;
class Solution {

    static void Main(String[] args) {
       
        int sizeOfA = int.Parse( Console.ReadLine() );
        var a = CreateFrequencyMap( sizeOfA );
        
        int sizeOfB = int.Parse( Console.ReadLine() );
        var b = CreateFrequencyMap( sizeOfB );
        
        
        List<int> tmp = new List<int>();
        string output = "";
        foreach( var val in a )
        {
            if ( b.ContainsKey( val.Key ))
            {
                if ( a[val.Key] < b[val.Key])
                {
                  tmp.Add( val.Key );
                }
            }
        }
      
        tmp.Sort();
        
        foreach( var v in tmp )
        {
            output += v;
            output += " ";
        }
 
        Console.WriteLine( output );
        
    }
    
    public static Dictionary<int,int> CreateFrequencyMap( int size )
    {
        var firstLine = Console.ReadLine().Split();
        
        var  tmpDict = new Dictionary<int,int>();
        
        for( int i = 0; i < size; i++ )
        {
            int tmp = int.Parse( firstLine[i]);
            
            if ( tmpDict.ContainsKey( tmp ) )
               tmpDict[tmp]++;
            else
            {
                tmpDict.Add( tmp , 1 );
            }
        }
        return tmpDict; 
    }
        
}