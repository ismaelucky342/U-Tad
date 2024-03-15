#include "3.1.MultVectors.h" 

 

int main(int argc,char** argv) 

{ 
vector3f v1={.x=1,.y=2,.z=3}; 
vector3f v2={.x=3,.y=2,.z=1}; 
float dot=0; 
vector3f cross={.x=0,.y=0,.z=0}; 
dot=dotProdV(v1,v2); 
cross=crossProdV(v1,v2); 
return 0; 
}

