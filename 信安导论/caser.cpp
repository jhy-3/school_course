#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#define MAX 101

char ciphertext[MAX];    //密文数组 
char plaintext[MAX];     //明文数组 
int key;	//密钥 

//生成key的函数 
int keyGen(){
	srand((int)time(0));	//调用time头文件生成随机数 
	return rand()%25+1;		//规定随机数的生成范围 ，凯撒加密算法位移密钥key的区间在(1,25) 
}
//加密函数 
void Encryption()
{
	printf("please input plaintext：");
	gets(plaintext);
	printf("ciphertext：");
	for(int i=0;plaintext[i]!='\0';i++){
        if(plaintext[i]>='A'&&plaintext[i]<='Z'){	//如果当前字符是大写，就和‘A’比较 
           ciphertext[i]=(plaintext[i]-'A'+key)%26+'A';
        }
        else if(plaintext[i]>='a'&&plaintext[i]<='z'){	//如果当前字符是小写，就和‘a’比较 
            ciphertext[i]=(plaintext[i]-'a'+key)%26+'a';
        }
        else
			ciphertext[i]=plaintext[i]+key;		//非大小写，直接位移 
        printf("%c",ciphertext[i]);		//输出当前字符 
    }
    printf("\n");
}

//解密函数 
void Decryption()
{
	printf("please input ciphertext：");
	gets(ciphertext);
	int len=strlen(ciphertext);
	printf("plaintext：");
	for(int i=0;i<len;i++)
	{
        if(ciphertext[i]>='A'&&ciphertext[i]<='Z'){		//如果当前字符是大写，就和‘A’比较
           plaintext[i] = ((ciphertext[i]-'A'-key)%26+26)%26 +'A';
        }
        else if(ciphertext[i]>='a'&&ciphertext[i]<='z'){	//如果当前字符是小写，就和‘a’比较
            plaintext[i]=((ciphertext[i]-'a'-key)%26+26)%26+'a';
        }
        else
			plaintext[i]=ciphertext[i]+key;		//非大小写，直接位移
        printf("%c",plaintext[i]);	//输出当前字符
    }
    printf("\n");
}

int main()
{
    int n,flag=1;
	key=keyGen();	//调用keyGen()函数生成随即加密密钥key 
	printf("key: %d\n",key);
	while(flag){		//死循环，只有当用户手动输入才结束 
		printf("please choose（1:Encryption，2:Decryption,3:exit）：");
		scanf("%d",&n);
		getchar();
		switch(n){
		case 1:
			Encryption();	//加密 
			break;
		case 2:
			Decryption();	//解密 
			break;
		case 3:exit(0);		//退出 
		}
	}
}

