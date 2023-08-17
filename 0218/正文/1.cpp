#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main(void){
	srand((unsigned)time(NULL));
    int i; 
	for(i = 0; i < 100; ++i){
		printf("%f\n",(double)(rand() % 10 + 9)/10+0.16);//[3, 8]
	}
} 
