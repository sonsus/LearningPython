#include <stdio.h>
int main(){
	float a;
	printf("This program converts your GPA into letter grades\n");
	printf("What is your GPA in 4.5 scale?\n");
	scanf("%2f"&a);
	if (a>4.5){
		printf("you are lying!\n", );
	}
	else if (a==4.5){
		printf("youre A+! fuck you.");
	}
	else if (a<4.5 && a>=4.0){
		printf("fuck you\n you know youre good enough (A, again fuck you)");
	}
	else if (a<4.0 && a>=3.5){
		printf("youre still ok B+");
	}
	else{
		printf("youre B or less than that: youre fucked up! bye");
	}
	return 0;
}