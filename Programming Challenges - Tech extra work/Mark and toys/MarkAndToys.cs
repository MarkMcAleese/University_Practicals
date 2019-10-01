
/* Problem
Mark and Jane are very happy after having their first kid. Their son is very
fond of toys. Therefore, Mark wants to buy some toys for his son. But he has a
limited amount of money. But he wants to buy as many toys as he can. So, he is
in a dilemma and is wondering how he can maximize the number of toys he can buy.
He has N items in front of him, tagged with their prices and he has only K rupees.


Now, you being Mark’s best friend have the task to help him buy as many toys for
his son as possible.

Input Format
The first line will contain two inputs N and K, followed by a line containing N 
integers

Output Format
Maximum number of toys Mark can buy for his son.

Constraints
1<=N<=105
1<=K<=109
1<=price of any toy<=109
*/

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {
    static void Main(String[] args)
    {

        var firstLine = Console.ReadLine().Split();
        
        var noItems = int.Parse( firstLine[0] );
        var budget  = int.Parse( firstLine[1] );
        
        var secondLine = Console.ReadLine().Split();
            
        var  numbers = new List<int>();
        for( int i = 0; i < noItems; i++ )
        {
            int tmp = int.Parse( secondLine[i]);
        
            if ( tmp < budget )
               numbers.Add( tmp);    
        }
           
        numbers.Sort( ( s1 , s2 ) => s1.CompareTo(s2 ) );

        int cost = 0;
        int count = 0;
        for( int i =0; i< numbers.Count && cost < budget; i++)
        {
           cost += numbers[i];
           
            if ( cost <= budget)
            {
                count++;
            }            
        }    
           
        Console.WriteLine( count );
        
    }
}