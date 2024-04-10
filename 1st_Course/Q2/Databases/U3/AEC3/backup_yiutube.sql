-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: yiutube
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0ubuntu0.23.10.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Comentario`
--

DROP TABLE IF EXISTS `Comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comentario` (
  `id_comentario` int(11) NOT NULL AUTO_INCREMENT,
  `id_user_coment` int(11) DEFAULT NULL,
  `id_contenido_coment` int(11) DEFAULT NULL,
  `comentario` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_comentario`),
  KEY `id_user_coment` (`id_user_coment`),
  KEY `id_contenido_coment` (`id_contenido_coment`),
  CONSTRAINT `Comentario_ibfk_1` FOREIGN KEY (`id_user_coment`) REFERENCES `Usuario` (`id_usuario`),
  CONSTRAINT `Comentario_ibfk_2` FOREIGN KEY (`id_contenido_coment`) REFERENCES `Contenido` (`id_contenido`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comentario`
--

LOCK TABLES `Comentario` WRITE;
/*!40000 ALTER TABLE `Comentario` DISABLE KEYS */;
INSERT INTO `Comentario` VALUES
(1,1,1,'¡Genial!'),
(2,2,1,'Me encantó'),
(3,3,2,'Interesante'),
(4,4,3,'Buen trabajo'),
(5,5,3,'Excelente contenido');
/*!40000 ALTER TABLE `Comentario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contenido`
--

DROP TABLE IF EXISTS `Contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Contenido` (
  `id_contenido` int(11) NOT NULL AUTO_INCREMENT,
  `id_user_cont` int(11) DEFAULT NULL,
  `fecha_cont` date DEFAULT NULL,
  `visualizaciones` int(11) DEFAULT NULL,
  `nombre_fichero` varchar(100) NOT NULL,
  `puntuacion` int(11) DEFAULT NULL,
  `nombre_contenido` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_contenido`),
  KEY `id_user_cont` (`id_user_cont`),
  CONSTRAINT `Contenido_ibfk_1` FOREIGN KEY (`id_user_cont`) REFERENCES `Usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contenido`
--

LOCK TABLES `Contenido` WRITE;
/*!40000 ALTER TABLE `Contenido` DISABLE KEYS */;
INSERT INTO `Contenido` VALUES
(1,1,'2023-01-01',100,'/ruta/a/archivo1.mp4',4,'Contenido 1'),
(2,2,'2023-01-02',200,'/ruta/a/archivo2.mp4',3,'Contenido 2'),
(3,3,'2023-01-03',150,'/ruta/a/archivo3.mp4',5,'Contenido 3'),
(4,4,'2023-01-04',120,'/ruta/a/archivo4.mp4',2,'Contenido 4'),
(5,5,'2023-01-05',180,'/ruta/a/archivo5.mp4',4,'Contenido 5');
/*!40000 ALTER TABLE `Contenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `nombre_usuario` varchar(100) NOT NULL,
  `contraseña_usuario` varchar(100) NOT NULL,
  `ciudad_residencia` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES
(1,'usuario1@example.com','Usuario 1','contraseña1','Ciudad 1'),
(2,'usuario2@example.com','Usuario 2','contraseña2','Ciudad 2'),
(3,'usuario3@example.com','Usuario 3','contraseña3','Ciudad 3'),
(4,'usuario4@example.com','Usuario 4','contraseña4','Ciudad 4'),
(5,'usuario5@example.com','Usuario 5','contraseña5','Ciudad 5');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Voto_Comment`
--

DROP TABLE IF EXISTS `Voto_Comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Voto_Comment` (
  `id_voto_comment` int(11) NOT NULL AUTO_INCREMENT,
  `id_usu_voto_comment` int(11) DEFAULT NULL,
  `id_com_voto_comment` int(11) DEFAULT NULL,
  `valor_voto_comment` int(11) DEFAULT NULL,
  `fecha_voto_commet` date DEFAULT NULL,
  PRIMARY KEY (`id_voto_comment`),
  UNIQUE KEY `Voto_Comment_UN` (`id_usu_voto_comment`,`id_com_voto_comment`),
  KEY `id_com_voto_comment` (`id_com_voto_comment`),
  CONSTRAINT `Voto_Comment_ibfk_1` FOREIGN KEY (`id_usu_voto_comment`) REFERENCES `Usuario` (`id_usuario`),
  CONSTRAINT `Voto_Comment_ibfk_2` FOREIGN KEY (`id_com_voto_comment`) REFERENCES `Comentario` (`id_comentario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Voto_Comment`
--

LOCK TABLES `Voto_Comment` WRITE;
/*!40000 ALTER TABLE `Voto_Comment` DISABLE KEYS */;
INSERT INTO `Voto_Comment` VALUES
(1,1,1,1,'2023-01-01'),
(2,2,1,1,'2023-01-02'),
(3,3,2,1,'2023-01-03'),
(4,4,3,-1,'2023-01-04'),
(5,5,4,1,'2023-01-05');
/*!40000 ALTER TABLE `Voto_Comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Voto_Contenido`
--

DROP TABLE IF EXISTS `Voto_Contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Voto_Contenido` (
  `id_voto_cont` int(11) NOT NULL AUTO_INCREMENT,
  `id_usu_voto_cont` int(11) DEFAULT NULL,
  `id_cont_voto_cont` int(11) DEFAULT NULL,
  `valor_voto_cont` int(11) DEFAULT NULL,
  `fecha_voto_cont` date DEFAULT NULL,
  PRIMARY KEY (`id_voto_cont`),
  UNIQUE KEY `voto_contenido_un` (`id_usu_voto_cont`,`id_cont_voto_cont`),
  KEY `id_cont_voto_cont` (`id_cont_voto_cont`),
  CONSTRAINT `Voto_Contenido_ibfk_1` FOREIGN KEY (`id_usu_voto_cont`) REFERENCES `Usuario` (`id_usuario`),
  CONSTRAINT `Voto_Contenido_ibfk_2` FOREIGN KEY (`id_cont_voto_cont`) REFERENCES `Contenido` (`id_contenido`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Voto_Contenido`
--

LOCK TABLES `Voto_Contenido` WRITE;
/*!40000 ALTER TABLE `Voto_Contenido` DISABLE KEYS */;
INSERT INTO `Voto_Contenido` VALUES
(1,1,1,1,'2023-01-01'),
(2,2,1,1,'2023-01-02'),
(3,3,2,1,'2023-01-03'),
(4,4,3,-1,'2023-01-04'),
(5,5,4,1,'2023-01-05');
/*!40000 ALTER TABLE `Voto_Contenido` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-10 13:43:35
