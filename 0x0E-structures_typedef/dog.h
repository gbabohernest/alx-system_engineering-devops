#ifndef DOG_H
#define DOG_H

/**
* struct dog - structure definition of a dog
*
* @name: string of charaters
* @age: integer
* @owner: string of characters
*
*/

typedef struct dog
{
	char *name;
	float age;
	char *owner;
} dog_t;

void dog_init(struct dog *d, char *name, float age, char *owner);
void print_dog_info(struct dog *d);
dog_t *new_dog(char *name, float age, char *owner);
void free_dog(dog_t *d);
#endif
