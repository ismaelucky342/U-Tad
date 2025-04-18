-- Verificar parámetros de rendimiento en MySQL
SHOW VARIABLES LIKE 'key_buffer_size';
SHOW VARIABLES LIKE 'query_cache_size';
SHOW VARIABLES LIKE 'sort_buffer_size';
SHOW VARIABLES LIKE 'table_open_cache';

-- Cambiar dinámicamente el valor de una variable
SET GLOBAL key_buffer_size = 128M;
SET GLOBAL query_cache_size = 64M;
SET GLOBAL sort_buffer_size = 4M;
SET GLOBAL table_open_cache = 2000;
-- Verificar el nuevo valor de la variable
SHOW VARIABLES LIKE 'key_buffer_size';
SHOW VARIABLES LIKE 'query_cache_size';
SHOW VARIABLES LIKE 'sort_buffer_size';
SHOW VARIABLES LIKE 'table_open_cache';
-- Verificar el uso de memoria
SHOW STATUS LIKE 'Key_blocks_used';
SHOW STATUS LIKE 'Qcache_hits';
SHOW STATUS LIKE 'Sort_merge_passes';
SHOW STATUS LIKE 'Open_tables';
-- Verificar el uso de CPU
SHOW STATUS LIKE 'Handler_read_rnd_next';
SHOW STATUS LIKE 'Handler_read_first';
SHOW STATUS LIKE 'Handler_read_rnd';
SHOW STATUS LIKE 'Handler_read_next';
SHOW STATUS LIKE 'Handler_read_prev';
SHOW STATUS LIKE 'Handler_read_key';
SHOW STATUS LIKE 'Handler_write';