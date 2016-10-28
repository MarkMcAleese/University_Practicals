#include"check_vector.h"
#include<math.h>
vecsim::vecsim(double* v1, double* v2, int v_len){
	vec1 = v1;
	vec2 = v2;
	vec_len = v_len;
}

vecsim::vecsim(){
	vec1 = nullptr;
	vec2 = nullptr;
	vec_len = 0;
}

double vecsim::Euclidean(){
	return vecsim::Euclidean(vec1, vec2, vec_len);
}
double vecsim::Euclidean(double* v1, double* v2, int v_len){
	if (v1 == 0 || v2 == 0 || v1 == nullptr || v2 == nullptr)
		return 0.0;
	if (v_len < 0)
		return 0.0;

	double d = 0.0;
	for (int i = 0; i < v_len; i++){
		int num = (v1[i] - v2[i]);
		d += (num * num);
	}
	d = sqrt(d);

	return d;
}

double vecsim::Cosine(){
	return vecsim::Cosine(vec1, vec2, vec_len);
}

double vecsim::Cosine(double* v1, double* v2, int v_len){

	if (v1 == 0 || v2 == 0 || v1 == nullptr || v2 == nullptr)
		return 0.0;
	if (v_len < 0)
		return 0.0;

	double totalX = 0.0, totalY = 0.0, totalDot = 0.0;

	for (int i = 0; i < v_len; i++){
		totalX += v1[i] * v1[i];
		totalY += v2[i] * v2[i];
		totalDot += v1[i] * v2[i];
	}

	return totalDot / (sqrt(totalX) * sqrt(totalY));

}