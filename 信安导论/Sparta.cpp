#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>

//˹�ʹ�������������
int keyGen();
int Encrypt(short key, char* plaintext, int plength, char* ciphertext, int* clength);
int Decrypt(short key, char* ciphertext, int clength, char* plaintext, int* plength);

int main(){
	char plaintext[100],ciphertext[100],plaintext1[100];
	printf("������������ܵ��ַ���:");
	gets(plaintext);
	int plength=strlen(plaintext);
	int clength;
	int plength1; 
	int key=keyGen();
	printf("key:%d\n",key);
	
	Encrypt(key,plaintext,plength,ciphertext,&clength);
	printf("�ַ��������ǣ�%d\n",plength);
  	printf("���ܺ���ַ����ǣ�");
  	puts(ciphertext);

  	Decrypt(key,ciphertext,clength,plaintext1,&plength1);                                  /*���ܹ���,���ظ��û��Ա�����Ƿ���ܳɹ� */
  	printf("�ַ��������ǣ�%d\n",clength);
	printf("��������ַ����������ٽ��ܺ�");
  	puts(plaintext1);
}

//˹�ʹ���������key�ĺ��� 
int keyGen(){
	srand((int)time(0));
	return rand()%4+3;	
}

//˹�ʹ����Ƚ��� 
int Encrypt(short key, char* plaintext, int plength, char* ciphertext, int* clength){
	int m=plength/key;
	int n=plength%key;
	int i,j=0,z=0; 
	while(j<n){               
		for(i=0;i<m+1;i++,z++){
			ciphertext[z]=plaintext[j+i*key];                                   //�Ըպÿ��Կ��������ε����ݽ��м��� 
		}
	j++;
    }
    while(j<key){
		for(i=0;i<m;i++,z++){
			ciphertext[z]=plaintext[j+i*key];                                  //�Զ��ಿ�ֽ��м��� 
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
			plaintext[j+i*key]=ciphertext[z];                                   //�Ըպÿ��Կ��������ε����ݽ��н��� 
		}
	j++;
    }
    while(j<key){
		for(i=0;i<m;i++,z++){
			plaintext[j+i*key]=ciphertext[z];                                  //�Զ��ಿ�ֽ��н���
		}
	j++;
    }
    *plength=strlen(plaintext);
}





