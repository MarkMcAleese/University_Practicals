
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
       
        var line = Console.ReadLine().Split();
        
        var numberOfIntegers = int.Parse( line[0] );
        var kDifference = int.Parse( line[1] );
        

        var NumDict = new Dictionary<int,int>();
        var numbers = Console.ReadLine().Split();
        
        for( int i = 0; i < numberOfIntegers; i++ )
        {
            var tmp = int.Parse( numbers[i]);
            NumDict.Add( tmp , tmp );
        }

        int count = 0;
        foreach(KeyValuePair<int, int> entry in NumDict)
        {
            if( NumDict.ContainsKey( (int)(entry.Key + kDifference )) )
                count++;
            
        }
        
        Console.WriteLine( count );
        
    }
}
}