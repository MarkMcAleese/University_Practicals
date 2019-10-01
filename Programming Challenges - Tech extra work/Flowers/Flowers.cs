
/* Problem
You and your K-1 friends want to buy N flowers. Flower number i has cost ci.
Unfortunately the seller does not like a customer to buy a lot of flowers, 
so he tries to change the price of flowers for customer who had bought flowers 
before. More precisely if a customer has already bought x flowers, he should pay
 (x+1)*ci dollars to buy flower number i.

You and your K-1 friends want to buy all N flowers in such a way that you spend
the least amount of money possible. You can buy the flowers in any order.

Input:

The first line of input contains two integers N and K (K <= N) next line 
contains N positive integers c1,c2,…,cN respectively.

Output:

Print the minimum amount of money you (and your friends) have to pay in order to
buy all N flowers.

*/

using System;
using System.Collections.Generic;
using System.IO;
class Solution {

    static void Main(String[] args) {
       
    int N, K;
    string NK = Console.ReadLine();
    string[] NandK = NK.Split(new Char[] {' ', '\t', '\n'});
    N = Convert.ToInt32(NandK[0]);
    K = Convert.ToInt32(NandK[1]);
      
    int [] C = new int [N];
      
    string numbers = Console.ReadLine(); 
    string[] split = numbers.Split(new Char[] {' ', '\t', '\n'});
      
    int i = 0;

    foreach (string s in split)
    {
        if( s.Trim() != "")
        {
            C[i++] = Convert.ToInt32(s);
        }
    }   
      
    Array.Sort( C );
       
    int total = 0;
    int bought = 0;
    for ( int i = N - 1; i >= 0; i -= K )
    {
        for ( int j = 0; j < K; j++ )
        {
            if ( i - j >= 0)
            {
                total += ( bought + 1 ) * C[i - j];
            }    
        }
        bought++;
     }  
        
    Console.WriteLine(total);
    }
}