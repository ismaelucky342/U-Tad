#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC6 - ABBD                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        02/01/2026  -  01:02:11           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    23/01/2026  -  11:14:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

#!/usr/bin/env python3
"""
Simulación del Read Path Flow en Cassandra usando estructuras de datos Python.
Con ella represento los 3 escenarios con datos ficticios de esta AEC3.
"""

import json
import time

class CassandraReadPathSimulator:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.data = json.load(f)

    def simulate_read(self, partition_key, clustering_key, scenario):
        print(f"\n=== Simulación Escenario {scenario}: Query pk='{partition_key}', ck='{clustering_key}' ===")

        # Configuración de caches según escenario
        if scenario == 1:
            row_cache_enabled = True
            partition_key_cache_enabled = True
        elif scenario == 2:
            row_cache_enabled = True
            partition_key_cache_enabled = False
        else:  # escenario 3
            row_cache_enabled = False
            partition_key_cache_enabled = False

        # Paso 1: Memtable
        print("1. Comprobando Memtable...")
        if partition_key in self.data['memtable']:
            print(f"   Hit: {self.data['memtable'][partition_key]}")
            return self.data['memtable'][partition_key]
        else:
            print("   Miss")

        # Paso 2: Row Cache
        if row_cache_enabled:
            print("2. Comprobando Row Cache...")
            if partition_key in self.data['row_cache']:
                print(f"   Hit: {self.data['row_cache'][partition_key]}")
                return self.data['row_cache'][partition_key]
            else:
                print("   Miss")
        else:
            print("2. Row Cache deshabilitada")

        # Paso 3: Bloom Filter
        print("3. Comprobando Bloom Filter...")
        if partition_key in self.data['sstables']['sstable1']:
            print("   Possible hit")
        else:
            print("   Miss - No data")
            return None

        # Paso 4: Partition Key Cache
        if partition_key_cache_enabled:
            print("4. Comprobando Partition Key Cache...")
            if partition_key in self.data['partition_key_cache']:
                print(f"   Hit: {self.data['partition_key_cache'][partition_key]}")
                return self.data['sstables']['sstable1'][partition_key]
            else:
                print("   Miss")
        else:
            print("4. Partition Key Cache deshabilitada")

        # Paso 5: Partition Summary
        print("5. Comprobando Partition Summary...")
        if partition_key in self.data['partition_summary']:
            summary = self.data['partition_summary'][partition_key]
            print(f"   Encontrado: {summary}")
        else:
            print("   No encontrado")
            return None

        # Paso 6: Partition Index
        print("6. Accediendo a Partition Index...")
        if partition_key in self.data['partition_index'] and clustering_key in self.data['partition_index'][partition_key]:
            index_data = self.data['partition_index'][partition_key][clustering_key]
            print(f"   Offset: {index_data}")
        else:
            print("   No encontrado")
            return None

        # Paso 7: Compression Offset Map
        offset = index_data['disk_offset']
        print("7. Comprobando Compression Offset Map...")
        if str(offset) in self.data['compression_offset_map']:
            uncompressed_pos = self.data['compression_offset_map'][str(offset)]
            print(f"   Posición descomprimida: {uncompressed_pos}")
        else:
            print("   No encontrado")
            return None

        # Paso 8: SSTable Read
        print("8. Leyendo desde SSTable...")
        time.sleep(0.1)  # Simular latencia de disco
        result = self.data['sstables']['sstable1'][partition_key][clustering_key]
        print(f"   Datos leídos: {result}")
        return result

def main():
    simulator = CassandraReadPathSimulator('ejemplos/datos_ejemplo.json')

    # Escenario 1
    result1 = simulator.simulate_read('pk1', 'ck1', 1)
    print(f"Resultado Escenario 1: {result1}")

    # Escenario 2
    result2 = simulator.simulate_read('pk2', 'ck2', 2)
    print(f"Resultado Escenario 2: {result2}")

    # Escenario 3
    result3 = simulator.simulate_read('pk3', 'ck3', 3)
    print(f"Resultado Escenario 3: {result3}")

if __name__ == "__main__":
    main()
