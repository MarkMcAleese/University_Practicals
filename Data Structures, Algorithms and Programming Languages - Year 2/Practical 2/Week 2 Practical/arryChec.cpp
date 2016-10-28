#include "arrayChec.h"
#include <map>
#include "catch.hpp"
bool same_elements(int* arrayA, int* b, int n){

	//for (int i = 0; i < n; i++){
	//	int *u = arrayA;
	//	int checka = 0;
	//	int checkb = 0;

	//	for (int x = 0; i < n; i++){
	//		int numberToCheck  = *u;
	//		int *p				= b;
	//		
	//		if (*arrayA == numberToCheck){
	//		checka++;
	//		}
	//		if (*b == numberToCheck){
	//		checkb++;
	//		}
	//		arrayA++;
	//		b++;

	//	}
	//	if (checka++ != checkb++)
	//	return false;
	//	u++;

	//return true;


	//}
	//return true;
	//

	std::map<int, int> m;
	int *u = arrayA;
	for (int x = 0; x < n; x++) {

		if (m.find(*u) == m.end())
			m.insert(std::make_pair(*u, 1));
		else
			m[*u] = m[*u]++;
		u++;
	}

	for (int i = 0; i < n; i++) {
		if (m.find(*b) == m.end())
			return false;
		else
			m[*b] = m[*b]--;

		if (m[*b] < 0) return false;
		b++;
	}

	return true;

	

	
}