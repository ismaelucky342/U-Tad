#ifndef LIB_HPP
#define LIB_HPP


/*================================INCLUDES===================================*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string>
#include <list>

/*=================================COLORS====================================*/


#define RESET "\033[0m"
#define BLACK "\033[30m"
#define RED "\033[31m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN "\033[36m"
#define BRIGHT_GREEN "\033[38;5;46m"
#define WHITE "\033[37m"

/*==================================CLASS===================================*/

using namespace std;

struct Licencia {
	long codigo;
	string herramienta;
};

struct Nodo
{
	Licencia elemento;
	Nodo *siguienteNodo;
};



#endif
