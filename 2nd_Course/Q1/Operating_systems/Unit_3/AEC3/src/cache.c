/****************************************************************************************************/
/*                                                                                                  */
/*                            ██╗   ██╗   ████████╗ █████╗ ██████╗                                  */
/*                            ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗                                 */
/*                            ██║   ██║█████╗██║   ███████║██║  ██║                                 */
/*                            ██║   ██║╚════╝██║   ██╔══██║██║  ██║                                 */
/*                            ╚██████╔╝      ██║   ██║  ██║██████╔╝                                 */
/*                             ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝                                  */
/*                                                                                                  */
/*                              ismael.hernandez@live.u-tad.com                                     */
/*                                                                                                  */
/****************************************************************************************************/

#include "cache.h"
#include "utils.h"

void calculate_direct_mapping(unsigned int address, int block_size)
{
    int block_offset = address % block_size;
    int line_number = (address / block_size) % 256;
    int tag = address / (block_size * 256);

    printf("Direct Mapping:\n");
    printf("Block Offset: %d\n", block_offset);
    printf("Line Number: %d\n", line_number);
    printf("Tag: %d\n", tag);
}

void calculate_associative_mapping(unsigned int address, int block_size)
{
    int block_offset = address % block_size;
    int tag = address / block_size;

    printf("Associative Mapping:\n");
    printf("Block Offset: %d\n", block_offset);
    printf("Tag: %d\n", tag);
}

void calculate_set_associative_mapping(unsigned int address, int block_size, int num_sets)
{
    int block_offset = address % block_size;
    int set_number = (address / block_size) % num_sets;
    int tag = address / (block_size * num_sets);

    printf("Set-Associative Mapping:\n");
    printf("Block Offset: %d\n", block_offset);
    printf("Set Number: %d\n", set_number);
    printf("Tag: %d\n", tag);
}

void cache_problem_1()
{
    unsigned int address;
    printf("Ingrese una dirección en hexadecimal (sin 0x): ");
    validate_hex_input(&address);

    printf("La dirección ingresada es: 0x%X\n", address);

    int block_size = 16;
    int num_sets = 4;

    calculate_direct_mapping(address, block_size);
    calculate_associative_mapping(address, block_size);
    calculate_set_associative_mapping(address, block_size, num_sets);
}

void cache_problem_2()
{
    int block_size;
    printf("Ingrese el tamaño del bloque de línea: ");
    validate_int_input(&block_size);

    printf("El tamaño del bloque de línea ingresado es: %d\n", block_size);

    unsigned int address = 0x12345678; // Ejemplo de dirección
    int num_sets = 4;

    calculate_direct_mapping(address, block_size);
    calculate_associative_mapping(address, block_size);
    calculate_set_associative_mapping(address, block_size, num_sets);
}