#include "persona.h"
#include <map>


int main(int argc, char** argv)
{
    //El siguiente mapa permite almacenar
    //una lista de personas y buscarlas usando
    //su nombre como índice
    map<string, Persona*> personas;
    //Variables para leer opciones, nombres y edades
    string opcion;
    string linea;
    string nombre;
    
    int edad;
    do{
        //Menú principal para operar con la lista de personas
        cout<<"Seleccionar una opción numérica:"<<endl;
        cout<<"1: Crear nueva persona"<<endl;
        cout<<"2: Ver personas almacenadas"<<endl;
        cout<<"3: Salvar a fichero una persona"<<endl;
        cout<<"4: Cargar desde fichero una persona"<<endl;
        cout<<"5: Exit"<<endl;
        
        getline(cin,linea);
        
        stringstream ss(linea); 
        ss>>opcion;        
        
        if(opcion=="1")
        {
            //Pedir datos de persona:
            cout<<"Introduzca nombre de persona"<<endl;
            getline(cin,nombre); //Leemos nombres simples o compuestos
            cout<<"Introduzca edad de persona"<<endl;
            getline(cin,linea);//Podemos leer línea completa 
            stringstream ss(linea);  
            ss>>edad;//Leemos sólo datos numéricos de la línea
            //Creamos una persona y la almacenamos
            Persona* p=new Persona(nombre,edad);
            personas[nombre]=p;//Usamos el nombre como índice
        }else if(opcion=="2")
        {            
            cout<<"Listando personas almacenadas:"<<endl;
            
            //Este es un bucle "for each": 
            //- Por cada elemento de la lista nos devuelve 
            //  un par "clave-valor", almacenado en la variable iteradora "entry"
            //- Los iteradores son variables "genéricas" que permiten "iterar"
            //  en estructuras de almacenamiento de datos (vectores, listas, mapas...)            
            //- Este iterador de mapa permite acceder al par "clave-valor":
            //    - La clave sería el registro "first"
            //    - El valor el registro "second" 
            
            for (const auto& entry : personas) {
                    //Podemos mostrar directamente las personas
                    cout<<*(entry.second)<<endl; 
                }
            cout<<endl;
        }else if(opcion=="3")
        {
            //Pedir datos de la persona
            cout<<"Introduzca el nombre de la persona:"<<endl;
            getline(cin, nombre);
            //Averiguar si existe
            //- El método find devuelve un iterador, si es distinto del 
            //  final de la lista, es que existe
            if(personas.find(nombre)!=personas.end())
            {
                //Si existe, pedir nombre de fichero y guardar la persona
                cout<<"Introduzca el nombre del fichero:"<<endl;
                getline(cin,linea);
                personas[nombre]->escribirAFichero(linea);
            }else{
                //Si no existe, error
                cout<<"Error: No existe esa persona"<<endl;
            }
        }else if(opcion=="4")
        {
            //Pedir datos de la persona
            cout<<"Introduzca el nombre del fichero:"<<endl;
            getline(cin, nombre);
            //Crear una persona y leer sus datos
            Persona* p=new Persona();
            p->leerDeFichero(nombre);
            personas[p->getNombre()]=p;
        }else if(opcion=="5")
        {
            cout<<"Abandonando el sistema (Cualquier dato no salvado se perderá)"<<endl;
			//borrar las personas para invocar su destructor
			for (const auto& entry : personas) {
                    delete entry.second;
                }
        }else{
            cout<<"ERROR: opción "<<opcion<<" no válida"<<endl;
        }
        
    }while(opcion!="5");
    return 0;
}