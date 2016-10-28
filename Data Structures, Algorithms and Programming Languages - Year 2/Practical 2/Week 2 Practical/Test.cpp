#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "arrayChec.h"
unsigned int Factorial(unsigned int number) {
	return number <= 1 ? number : Factorial(number - 1)*number;
}

TEST_CASE("Factorials are computed", "[factorial]") {
	REQUIRE(Factorial(1) == 1);
	REQUIRE(Factorial(2) == 2);
	REQUIRE(Factorial(3) == 6);
	REQUIRE(Factorial(10) == 3628800);
	int a[10] = { 121, 144, 19, 161, 19, 144, 19, 11 };
	int b[10] = { 121, 1144, 19, 161, 19, 144, 19, 11 };
	REQUIRE(same_elements(a, b, 10) == 0);
	system("pause");
}