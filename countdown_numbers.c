#include <stdio.h>
#include <stdlib.h>

void findSolution(int chosen_numbers[6], int target_number){

  int currentDistance = 1000;
  int i;
  int j;
  int sum;

  for(i=0; i<6; i++){
    if(currentDistance == 0){
      break;
    }
    for(j=i; j<6; j++){
      sum = chosen_numbers[i] + chosen_numbers[j];
      currentDistance = abs(sum - target_number);
      if(currentDistance == 0){
        printf("Solution found with %d + %d\n", chosen_numbers[i], chosen_numbers[j]);
        break;
      }
    }
  }
  for(i=0; i<6; i++){
    if(currentDistance == 0){
      break;
    }
    for(j=i; j<6; j++){
      sum = chosen_numbers[i] * chosen_numbers[j];
      currentDistance = abs(sum - target_number);
      if(currentDistance == 0){
        printf("Solution found with %d x %d\n", chosen_numbers[i], chosen_numbers[j]);
        break;
      }
    }
  }

}

int main(){

  int target;
  int chose_numbers[6];
  int i;
  int proof = 0;

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
    for(i = 0; i < 6; i++)
      printf("%d ", chose_numbers[i]);
    printf("\nWith a target of %d\n", target);
    // giving option to redo the setup process 
    printf("Is this correct (1 = yes, 0 = no)? \n"); // would prefer y/n
    scanf("%d", &proof);
  }

  findSolution(chose_numbers, target);
 
  return 0;

}
