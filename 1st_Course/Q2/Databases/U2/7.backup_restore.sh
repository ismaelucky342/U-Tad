mysqldump -u username -p SchoolDB > school_backup.sql

mysql -u username -p SchoolDB < school_backup.sql
