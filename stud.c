#include<stdio.h>

typedef struct{
    char name[50];
    int roll;
    int marks;
}student;

int num;

int main () {

    printf("\nWelcome to INFONEST!\n");

 while(1){

    FILE *fp;
    fp=fopen("info.txt", "a+");
    FILE *fp1;
    fp1=fopen("data.txt", "a+");

    printf("\nWhat would you like to do?\n 1)Add Student Data\n 2)Search Student Record\n 3) Exit\n ");
    int choice;
    scanf("%d", &choice);

    switch(choice){

     case 1: {
     printf("Enter number of students: ");
     scanf("%d", &num);
     student s[num];

     for(int i=1; i<=num; i++){
        printf("Name: ");
        scanf("%s", &s[i].name);
        printf("Roll Number: ");
        scanf("%d", &s[i].roll);
        printf("Marks: ");
        scanf("%d", &s[i].marks);
        
        printf("Updated memory\n");
     }
     for(int i=1; i<=num; i++){
        fputs("-----------------\n", fp);
        fprintf(fp, "Name: %s\n", s[i].name);
        fprintf(fp, "Roll Number: %d\n", s[i].roll);
        fprintf(fp, "Marks: %d\n", s[i].marks);
        fputs("-----------------\n", fp);
        fprintf(fp1, "%s %d %d\n", s[i].name, s[i].roll, s[i].marks);
     }
   
     for(int i=1; i<=num; i++){
        printf("-----------------\n");
        printf("Name: %s\n", s[i].name);
        printf("Roll Number: %d\n", s[i].roll);
        printf("Marks: %d\n", s[i].marks);
        printf("-----------------\n");
     }
      printf("Records have been stored successfully\n");
      fclose(fp);
      fclose(fp1);
     break;
     }
     
     case 2: {
     int search;
     char name[50];
     int roll, marks;
     student s[num];
     printf("Enter Roll Number: \n");
     scanf("%d", &search);

     while (fscanf(fp1, "%s %d %d", name, &roll, &marks) != EOF) {
        if (roll == search) {
            printf("Record Found:\n");
            printf("-----------------------------\n");
            printf("Name: %s, Roll: %d, Marks: %d\n", name, roll, marks);
            printf("-----------------------------\n");
        }
      }
      break;
     }
     
     case 3: {
     printf("Exiting...\n");
     fclose(fp);
     fclose(fp1);
     return 0;
     }
    }
   }
}