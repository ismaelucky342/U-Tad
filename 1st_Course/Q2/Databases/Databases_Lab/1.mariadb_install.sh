## install steps mariadb
# download the latest version of Mariadb  from https://downloads.mariadb

#STEPS 
### STEP 1: Prepare ubuntu
sudo apt update 

sudo apt upgrade -y

sudo apt -y install mariadb-server mariadb-client

#CHECK

sudo apt policy mariadb-server

echo '>>> Checking MariaDB systemd service...'

systemctl status mariadb

echo '>>> Checking MariaDB port (3306)...' 

sudo netstat -putan | grep -i 3306

#STEP 2: Mariadb config

sudo su 

mysql_secure_installation
