#ifndef  MULTVECTOR_H 
#define  MULTVECTOR_H 
#include <stdio.h> 
#include <stdlib.h> 

typedef struct vector3f{ 
float x,y,z; 

}vector3f; 
float dotProdV(vector3f v1,vector3f v2); 
vector3f crossProdV(vector3f v1,vector3f v2); 

#endif

