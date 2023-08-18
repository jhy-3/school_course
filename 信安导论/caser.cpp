#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#define MAX 101

char ciphertext[MAX];    //�������� 
char plaintext[MAX];     //�������� 
int key;	//��Կ 

//����key�ĺ��� 
int keyGen(){
	srand((int)time(0));	//����timeͷ�ļ���������� 
	return rand()%25+1;		//�涨����������ɷ�Χ �����������㷨λ����Կkey��������(1,25) 
}
//���ܺ��� 
void Encryption()
{
	printf("please input plaintext��");
	gets(plaintext);
	printf("ciphertext��");
	for(int i=0;plaintext[i]!='\0';i++){
        if(plaintext[i]>='A'&&plaintext[i]<='Z'){	//�����ǰ�ַ��Ǵ�д���ͺ͡�A���Ƚ� 
           ciphertext[i]=(plaintext[i]-'A'+key)%26+'A';
        }
        else if(plaintext[i]>='a'&&plaintext[i]<='z'){	//�����ǰ�ַ���Сд���ͺ͡�a���Ƚ� 
            ciphertext[i]=(plaintext[i]-'a'+key)%26+'a';
        }
        else
			ciphertext[i]=plaintext[i]+key;		//�Ǵ�Сд��ֱ��λ�� 
        printf("%c",ciphertext[i]);		//�����ǰ�ַ� 
    }
    printf("\n");
}

//���ܺ��� 
void Decryption()
{
	printf("please input ciphertext��");
	gets(ciphertext);
	int len=strlen(ciphertext);
	printf("plaintext��");
	for(int i=0;i<len;i++)
	{
        if(ciphertext[i]>='A'&&ciphertext[i]<='Z'){		//�����ǰ�ַ��Ǵ�д���ͺ͡�A���Ƚ�
           plaintext[i] = ((ciphertext[i]-'A'-key)%26+26)%26 +'A';
        }
        else if(ciphertext[i]>='a'&&ciphertext[i]<='z'){	//�����ǰ�ַ���Сд���ͺ͡�a���Ƚ�
            plaintext[i]=((ciphertext[i]-'a'-key)%26+26)%26+'a';
        }
        else
			plaintext[i]=ciphertext[i]+key;		//�Ǵ�Сд��ֱ��λ��
        printf("%c",plaintext[i]);	//�����ǰ�ַ�
    }
    printf("\n");
}

int main()
{
    int n,flag=1;
	key=keyGen();	//����keyGen()���������漴������Կkey 
	printf("key: %d\n",key);
	while(flag){		//��ѭ����ֻ�е��û��ֶ�����Ž��� 
		printf("please choose��1:Encryption��2:Decryption,3:exit����");
		scanf("%d",&n);
		getchar();
		switch(n){
		case 1:
			Encryption();	//���� 
			break;
		case 2:
			Decryption();	//���� 
			break;
		case 3:exit(0);		//�˳� 
		}
	}
}

