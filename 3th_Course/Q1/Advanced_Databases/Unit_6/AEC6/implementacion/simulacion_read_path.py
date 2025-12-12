#!/usr/bin/env python3
"""
Simulación del Read Path Flow en Cassandra usando estructuras de datos Python.
Este script demuestra los 3 escenarios con datos ficticios.
"""

import json
import time

class CassandraReadPathSimulator:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.data = json.load(f)
        self.row_cache_enabled = True
        self.partition_key_cache_enabled = True

    def simulate_read(self, partition_key, clustering_key, scenario):
        print(f"\n=== Simulación Escenario {scenario}: Query pk='{partition_key}', ck='{clustering_key}' ===")

        # Escenario 1: Caches habilitadas
        if scenario == 1:
            self.row_cache_enabled = True
            self.partition_key_cache_enabled = True
        # Escenario 2: Solo Row Cache
        elif scenario == 2:
            self.row_cache_enabled = True
            self.partition_key_cache_enabled = False
        # Escenario 3: Ninguna cache
        elif scenario == 3:
            self.row_cache_enabled = False
            self.partition_key_cache_enabled = False

        # Paso 1: Memtable
        print("1. Checking Memtable...")
        if partition_key in self.data['memtable']:
            print(f"   Hit: {self.data['memtable'][partition_key]}")
            return self.data['memtable'][partition_key]
        else:
            print("   Miss")

        # Paso 2: Row Cache
        if self.row_cache_enabled:
            print("2. Checking Row Cache...")
            if partition_key in self.data['row_cache']:
                print(f"   Hit: {self.data['row_cache'][partition_key]}")
                return self.data['row_cache'][partition_key]
            else:
                print("   Miss")
        else:
            print("2. Row Cache disabled")

        # Paso 3: Bloom Filter (simulado como check en SSTables)
        print("3. Checking Bloom Filter...")
        if partition_key in self.data['sstables']['sstable1']:
            print("   Possible hit")
        else:
            print("   Miss - No data")
            return None

        # Paso 4: Partition Key Cache
        if self.partition_key_cache_enabled:
            print("4. Checking Partition Key Cache...")
            if partition_key in self.data['partition_key_cache']:
                print(f"   Hit: {self.data['partition_key_cache'][partition_key]}")
                # Simular acceso directo
                return self.data['sstables']['sstable1'][partition_key]
            else:
                print("   Miss")
        else:
            print("4. Partition Key Cache disabled")

        # Paso 5: Partition Summary
        print("5. Checking Partition Summary...")
        if partition_key in self.data['partition_summary']:
            summary = self.data['partition_summary'][partition_key]
            print(f"   Found: {summary}")
        else:
            print("   Not found")
            return None

        # Paso 6: Partition Index
        print("6. Accessing Partition Index...")
        if partition_key in self.data['partition_index'] and clustering_key in self.data['partition_index'][partition_key]:
            index_data = self.data['partition_index'][partition_key][clustering_key]
            print(f"   Offset: {index_data}")
        else:
            print("   Not found")
            return None

        # Paso 7: Compression Offset Map
        offset = index_data['disk_offset']
        print("7. Checking Compression Offset Map...")
        if str(offset) in self.data['compression_offset_map']:
            uncompressed_pos = self.data['compression_offset_map'][str(offset)]
            print(f"   Uncompressed position: {uncompressed_pos}")
        else:
            print("   Not found")
            return None

        # Paso 8: SSTable Read
        print("8. Reading from SSTable...")
        time.sleep(0.1)  # Simular latencia de disco
        result = self.data['sstables']['sstable1'][partition_key][clustering_key]
        print(f"   Data: {result}")
        return result

def main():
    simulator = CassandraReadPathSimulator('ejemplos/datos_ejemplo.json')

    # Escenario 1
    result1 = simulator.simulate_read('pk1', 'ck1', 1)
    print(f"Resultado: {result1}")

    # Escenario 2
    result2 = simulator.simulate_read('pk2', 'ck2', 2)
    print(f"Resultado: {result2}")

    # Escenario 3
    result3 = simulator.simulate_read('pk3', 'ck3', 3)
    print(f"Resultado: {result3}")

if __name__ == "__main__":
    main()