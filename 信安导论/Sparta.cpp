#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>

//斯巴达手杖密码声明
int keyGen();
int Encrypt(short key, char* plaintext, int plength, char* ciphertext, int* clength);
int Decrypt(short key, char* ciphertext, int clength, char* plaintext, int* plength);

int main(){
	char plaintext[100],ciphertext[100],plaintext1[100];
	printf("请输入您想加密的字符串:");
	gets(plaintext);
	int plength=strlen(plaintext);
	int clength;
	int plength1; 
	int key=keyGen();
	printf("key:%d\n",key);
	
	Encrypt(key,plaintext,plength,ciphertext,&clength);
	printf("字符串长度是：%d\n",plength);
  	printf("加密后的字符串是：");
  	puts(ciphertext);

  	Decrypt(key,ciphertext,clength,plaintext1,&plength1);                                  /*解密过程,并回复用户以便检验是否解密成功 */
  	printf("字符串长度是：%d\n",clength);
	printf("您输入的字符串经加密再解密后：");
  	puts(plaintext1);
}

//斯巴达手杖生成key的函数 
int keyGen(){
	srand((int)time(0));
	return rand()%4+3;	
}

//斯巴达手杖解密 
int Encrypt(short key, char* plaintext, int plength, char* ciphertext, int* clength){
	int m=plength/key;
	int n=plength%key;
	int i,j=0,z=0; 
	while(j<n){               
		for(i=0;i<m+1;i++,z++){
			ciphertext[z]=plaintext[j+i*key];                                   //对刚好可以框入正方形的数据进行加密 
		}
	j++;
    }
    while(j<key){
		for(i=0;i<m;i++,z++){
			ciphertext[z]=plaintext[j+i*key];                                  //对多余部分进行加密 
		}
	j++;
    }
    *clength=strlen(ciphertext);
}

int Decrypt(short key, char* ciphertext, int clength, char* plaintext, int* plength){
	int m=clength/key;
	int n=clength%key;
	int i,j=0,z=0;
	while(j<n){
		for(i=0;i<m+1;i++,z++){
			plaintext[j+i*key]=ciphertext[z];                                   //对刚好可以框入正方形的数据进行解密 
		}
	j++;
    }
    while(j<key){
		for(i=0;i<m;i++,z++){
			plaintext[j+i*key]=ciphertext[z];                                  //对多余部分进行解密
		}
	j++;
    }
    *plength=strlen(plaintext);
}





