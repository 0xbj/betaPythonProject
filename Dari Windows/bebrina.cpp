#include <iostream>
#include <cstdio>
#include <stdio.h>
using namespace std;

int main(){
	int jam,menit,detik,sisa,input;
	system("cls");
	printf("\n\t\t== Fakhrizal Asshiddiq ==");

	printf("\n\n [?] Masukkan Detik : ");
	scanf("%d",&input);

	jam = input / 3600;
	sisa = input % 3600;

	menit = sisa / 60;
	detik = sisa % 60;

	if(jam >= 1){
		printf("\n\n %d : %d : %d\n",jam,menit,detik);
	}else if(jam <= 0 ){
		printf("\n\n %d : %d\n",menit,detik);
	}else{
		printf("\n ERROR");
	}


}
