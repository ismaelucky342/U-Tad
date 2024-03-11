#include "3.1.MultVectors.h"

float dotProdV(vector3f v1,vector3f v2){ 
return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z; 
} 
vector3f crossProdV(vector3f v1,vector3f v2){ 
vector3f result; 
result.x=v1.y*v2.z- v1.z*v2.y; 
result.y=v1.z*v2.x-v1.x*v2.z; 
result.z=v1.x*v2.z-v1.z*v2.x; 

return result; 

}