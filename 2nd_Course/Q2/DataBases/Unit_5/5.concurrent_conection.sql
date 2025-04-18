-- Ver las conexiones actuales
SHOW STATUS LIKE 'Threads_connected';

-- Establecer el número máximo de conexiones simultáneas
SET GLOBAL max_connections = 200;

-- Comprobar la configuración de conexiones simultáneas
SHOW VARIABLES LIKE 'max_connections';

-- Ver las conexiones activas
SHOW PROCESSLIST;
