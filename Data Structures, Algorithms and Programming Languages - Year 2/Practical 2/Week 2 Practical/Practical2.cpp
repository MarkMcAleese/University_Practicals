#include <iostream>
#include "arrayChec.h"

void insert(int* &array, int &array_len, int pos, int val){
	if (!array || array_len < 0){
		return;
	}
	auto *e = array;
	array_len++;
	auto *p = new int[array_len];

	for (int i = 0; i < array_len; i++){
		if (pos == i){
			p[i] = val;
		}
		else{
			p[i] = *e++;
		}
	}
	delete[] array;

	array = p;

}

void remove(int* &array, int &array_len, int pos){

	if (!array || array_len < 0) {
		return;
	}
	auto *e = array;
	array_len--;
	auto *p = new int[array_len];

	for (int i = 0; i < array_len; i++) {
		if (pos == i) *e++;
		p[i] = *e++;
		
	}
	delete[] array;

	array = p;
}
int main(){
	int MAX_A = 5;
	//Task 1
		/* int sample[10];
		for (int t = 0; t < 10; t++)
		sample[t] = t;*/

	//int sample[10] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
	//int sample2[10] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };

	int * insertTest = new int[MAX_A];
	//int * removeTest = new int[MAX_A];
	for (int t = 0; t < MAX_A; ++t)
		insertTest[t] = t;

	insert(insertTest, MAX_A, 2, 300);

	auto p = insertTest;
	for (int t = 0; t < MAX_A; ++t)
		std::cout << "This is sample [" << t << "]:  " << *p++ << std::endl;
	
	std::cout << "Test 2" << std::endl;

	for (int t = 0; t < MAX_A; ++t)
		insertTest[t] = t;

	remove(insertTest, MAX_A, 2);

	int* b = insertTest;
	for (int t = 0; t < MAX_A; ++t)
		std::cout << "This is sample [" << t << "]:  " << *b++ << std::endl;



	//system("pause");

	//for (int t = 0; t < 10; ++t){
	//	std::cout << "This is sample [" << t << "]:  " << sample[t] << std::endl;
	//}

	//Task 2
	//int* p = sample;

	//for (int t = 0; t < 10; t++){
	//	*p++ = t * t;
	//}

	//p = sample;
	//
	//for (int t = 0; t < 10; ++t)
	//	std::cout << "This is sample [" << t << "]:  " << *p++ << std::endl;

	////TASK 3
	//int i = 27;
	//int *i_ptr = &i; // declare a pointer and give it the value of the address of i
	//std::cout << "value in i is " << i << std::endl;
	//std::cout << "address of i is " << &i << std::endl;
	//std::cout << "value in pointer is " << i_ptr << std::endl;
	//std::cout << "value from dereferencing pointer is " << *i_ptr << std::endl;
	//*i_ptr = 35; // change the value in i through pointer
	//std::cout << "value in i is " << i << std::endl;
	//double* d_ptr = NULL; // declare a pointer and initialise it to a NULL pointer
	//std::cout << "value in pointer is " << d_ptr << std::endl;
	//*d_ptr = 0.25; // error! NULL is not a valid memory address

	//Task 4
	/*int x = 10;
	int* p = &x;

	std::cout << *p << std::endl;
	*/

	//Task 5
	//int* p = NULL;
	//if (p == NULL) {
	//	int x = 10;
	//	p = &x;
	//}
	//// x falls out of scope (“x” is undefined)
	//// p is now a dangling pointer
	//*p = 3;





	//Task 6
	int a[10] = { 121, 144, 19, 161, 19, 144, 19, 11 };
	int bTask2[10] = { 121, 1144, 19, 161, 19, 144, 19, 11 };
	int *a_ptr = a;
	int *b_ptr = bTask2;

	bool check = same_elements(a, bTask2, 8);
	std::cout << check << std::endl;
	system("Pause");
} 
