#include<stdio.h>
#include<math.h>
#define M_PI 3.14

//struct area
struct Circle
{
    float radix; 
};

struct rectangle
{
    float h; 
    float b; 
};

struct square
{
    float a; 
};

union Figures
{
    struct Circle circle; 
    struct Rectangle rectangle; 
    struct Square square; 
};

enum Type 
{
    CIRCLE, RECTANGLE, SQUARE
};

//main area
int main() {
    union Figures figures;
    enum Type type;
    float area, perimetro, diametro;

    printf("Seleccione el tipo de figura:\n");
    printf("1. CÃ­rculo\n");
    printf("2. RectÃ¡ngulo\n");
    printf("3. Cuadrado\n");
    printf("Ingrese su opciÃ³n: ");
    scanf("%d", &type );

    switch (type) {

        case CIRCLE:
            printf("Ingrese el radio del cÃ­rculo: ");
            scanf("%f", &figures.circle.radix);
            area = M_PI * figures.circle.radix * figures.circle.radix;
            diametro = 2 * figures.circle.radix;
            printf("El Ã¡rea del cÃ­rculo es: %.2f\n", area);
            printf("El diÃ¡metro del cÃ­rculo es: %.2f\n", diametro);
            break;
        
        case RECTANGLE:
            printf("Ingrese la base del rectÃ¡ngulo: ");
            scanf("%f", &figures.rectangle.b);
            printf("Ingrese la altura del rectÃ¡ngulo: ");
            scanf("%f", &figures.rectangle.h);
            area = figures.rectangle.b * figures.rectangle.h;
            perimetro = 2 * (figures.rectangle.b + figures.rectangle.h);
            printf("El Ã¡rea del rectÃ¡ngulo es: %.2f\n", area);
            printf("El perÃ­metro del rectÃ¡ngulo es: %.2f\n", perimetro);
            break;
        
        case SQUARE:
            printf("Ingrese el lado del cuadrado: ");
            scanf("%f", &figures.square.a);
            area = figures.square.a * figures.square.a;
            perimetro = 4 * figures.square.a;
            printf("El Ã¡rea del cuadrado es: %.2f\n", area);
            printf("El perÃ­metro del cuadrado es: %.2f\n", perimetro);
            break;
        
        default:
            printf("OpciÃ³n no vÃ¡lida.\n");
            return 1; // Salir del programa con cÃ³digo de error
    }

    return 0;
}