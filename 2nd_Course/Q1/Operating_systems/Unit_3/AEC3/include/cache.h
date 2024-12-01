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

#ifndef CACHE_H
#define CACHE_H

/*==================================INCLUDES============================*/

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

/*==================================FUNCTIONS============================*/

void calculate_direct_mapping(unsigned int address, int block_size);
void calculate_associative_mapping(unsigned int address, int block_size);
void calculate_set_associative_mapping(unsigned int address, int block_size, int num_sets);
void cache_problem_1();
void cache_problem_2();
#endif
