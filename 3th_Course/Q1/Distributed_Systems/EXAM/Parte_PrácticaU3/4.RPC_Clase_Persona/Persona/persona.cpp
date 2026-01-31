#include "persona.h"
#include <fstream>  

Persona::Persona(string nombre,int edad):nombre(nombre),edad(edad){}

Persona::Persona():nombre(""),edad(0){}

Persona::~Persona(){}

void Persona::setEdad(int edad){this->edad=edad;}
int Persona::getEdad(){return edad;}
        
void Persona::setNombre(string nombre){this->nombre=nombre;}
string Persona::getNombre(){return nombre;}

void Persona::escribirAFichero(string nombreFichero){
    //Abrir fichero
    ofstream fich(nombreFichero);
    //Escribir datos
    fich<<getNombre()<<endl;
    fich<<getEdad()<<endl;
    //cerrar
    fich.close();
}


void Persona::leerDeFichero(string nombreFichero){
    //Abrir fichero
    ifstream fich(nombreFichero);
    //Si existe
    if (fich.is_open())
    {
        //Leer datos
        getline(fich,nombre);
        fich>>edad;
        //cerrar
        fich.close();
    }else //si no existe, error
    {
        nombre="Error de lectura de fichero";        
    }
}

ostream& operator<<(ostream& os,const Persona &p)
{
    os << "Nombre: "<< p.nombre <<"\nEdad:"<<p.edad<<endl;
    return os;
}