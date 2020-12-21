#include <stdio.h>
#include <stdlib.h>

int main(){

  int target;
  int chose_numbers[6];
  int loop;
  int proof = 0;
  // using numbers to corrispond to operations
  int operations[] = {1, 2, 3, 4};

  while(proof == 0){
    // asking user for the input numbers and target
    printf("What is your first number \n");
    scanf("%d", &chose_numbers[0]);
    printf("What is your second number \n");
    scanf("%d", &chose_numbers[1]);
    printf("What is your third number \n");
    scanf("%d", &chose_numbers[2]);
    printf("What is your fourth number \n");
    scanf("%d", &chose_numbers[3]);
    printf("What is your fifth number \n");
    scanf("%d", &chose_numbers[4]);
    printf("What is your sixth number \n");
    scanf("%d", &chose_numbers[5]);
    printf("What is your target \n");
    scanf("%d", &target);

    // letting user proof read their numbers
    printf("Your numbers are: ");
    for(loop = 0; loop < 6; loop++)
      printf("%d ", chose_numbers[loop]);
    printf("\nWith a target of %d\n", target);
    printf("Is this correct (1 = yes, 0 = no)? \n"); // would prefer y/n
    scanf("%d", &proof);
  }

  return 0;
}
