#include "Person.h"
#include<iostream>
#include"check_vector.h"
void create_person_1_and_2(){
	Person p1("Adam", "Jones", "1234", 0);
	p1.set_birth_year(1990);
	Person p2;
	p2.set_given_name("Eve");
	p2.set_family_name(p1.get_family_name());
	p2.set_birth_year(p1.get_birth_year() + 10);

	if (p1 == p2)
		std::cout << p1 << " is the same person as " << '\n' << p2 << '\n';
	else
		std::cout << p1 << " is not the same as " << '\n' << p2 << '\n';
}


int main(){

	//TASK 1: Person* mark = new Person("Mark", "McAleese", "ABC", 23);//mark->set_family_name("Not that");//std::string name = mark->get_family_name();//Person* array1 = new Person[385];//array1[13].set_given_name("John");
	//Task 2: create_person_1_and_2();
	double vector1[10] = { 1.5, 3., 4.5, 6., 7.5, 9., 10.5, 12., 13.5, 15. };
	double vector2[10] = { 3., 4.5, 6., 7.5, 9., 10.5, 12., 13.5, 15., 16.5 };	vecsim vs(vector1, vector2, 10);
	std::cout << "Euclidean dis = " << vs.Euclidean() << std::endl;
	std::cout << "Cosine sim = "<< vs.Cosine() << std::endl;

	vecsim vs2;
	std::cout << "Euclidean dis = " << vs2.Euclidean(vector1, vector2, 10) << std::endl;
	std::cout << "Cosine sim = " << vs2.Cosine(vector1, vector2, 10) << std::endl;

	system("pause");
	return 0;
}