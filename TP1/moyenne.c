#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
	int i, sum, num;
    float avg;
	if (argc >= 2){
        sum = 0;
        for (i=1; i<argc; i++ ){
            
            if(sscanf (argv[i],"%d",&num)){
                if (num < 0 || num > 20) {
                puts("Erreur: Note non valide connard.");
		        return -1;
                }
            sum += num;
            }
            else {
                puts("Erreur: faut pas mettre autre chose que des nombres connard.");
		        return -1;
            }
        }
        avg = sum / (float)(argc-1);
	    printf("Votre moyenne est : %1.2f\n",avg);
	}
	else
	{
		puts("Erreur: Aucune moyenne à calculer connard.");
		return -1;
	}
	return 0;
}
