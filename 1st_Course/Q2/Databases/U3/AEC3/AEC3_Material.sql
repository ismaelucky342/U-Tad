-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: yiutube
-- ------------------------------------------------------
-- Server version	10.4.11-MariaDB

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
-- Table structure for table `comentario`
--

DROP TABLE IF EXISTS `comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comentario` (
  `id_comentario` int(11) NOT NULL,
  `id_user_coment` int(11) DEFAULT NULL,
  `id_contenido_coment` int(11) DEFAULT NULL,
  `comentario` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '1',
  PRIMARY KEY (`id_comentario`),
  KEY `Comment_FK` (`id_contenido_coment`),
  KEY `Comment_FK_1` (`id_user_coment`),
  CONSTRAINT `Comment_FK` FOREIGN KEY (`id_contenido_coment`) REFERENCES `contenido` (`id_contenido`),
  CONSTRAINT `Comment_FK_1` FOREIGN KEY (`id_user_coment`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentario`
--

LOCK TABLES `comentario` WRITE;
/*!40000 ALTER TABLE `comentario` DISABLE KEYS */;
INSERT INTO `comentario` VALUES (1,2,3,'Como mola este video'),(2,2,3,'Me encanta la cancion'),(3,2,1,'Me reucerda cuando yo era pequeña'),(4,2,4,'No soporto los videos como este'),(5,1,3,'Vaya postureo'),(6,5,4,'jajajajaja'),(7,5,4,'Nada que decir'),(8,1,1,'Puede que me sume a este reto'),(9,1,4,'Me encanta');
/*!40000 ALTER TABLE `comentario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenido`
--

DROP TABLE IF EXISTS `contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenido` (
  `id_contenido` int(11) NOT NULL AUTO_INCREMENT,
  `id_user_cont` int(11) DEFAULT NULL,
  `fecha_cont` date DEFAULT NULL,
  `visualizaciones` int(11) DEFAULT NULL,
  `nombre_fichero` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `puntuacion` int(11) DEFAULT NULL,
  `nombre_contenido` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_contenido`),
  KEY `Content_FK` (`id_user_cont`),
  CONSTRAINT `Content_FK` FOREIGN KEY (`id_user_cont`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenido`
--

LOCK TABLES `contenido` WRITE;
/*!40000 ALTER TABLE `contenido` DISABLE KEYS */;
INSERT INTO `contenido` VALUES (1,1,'2010-10-10',100,'/home/foto.jpg',3,'Foto Vacaciones'),(2,2,'2010-10-10',10,'/home/video.mp4',0,'Video Playa'),(3,3,'2010-11-10',500,'/home/mitexto.txt',9,'Documento 1'),(4,4,'2011-01-10',20,'/home/video2.mp4',2,'Video Cena'),(5,4,'2013-01-10',20,'/home/foto3.jpg',1,'Foto Familia'),(6,4,'2014-01-10',20,'/home/video2.mp4',0,'Video Tutorial'),(7,4,'2014-01-10',35,'/home/foto4.jpg',6,'Foto montaña'),(8,4,'2014-01-10',12,'/home/otrafoto.jpg',4,'Foto trabajo'),(9,2,'2010-10-10',10,'/home/video.mp4',3,'Video Casa'),(10,2,'2013-10-23',10,'/home/video.mp4',3,'Video2'),(11,3,'2020-07-15',3,'/home/mivideo.mp4',5,'General');
/*!40000 ALTER TABLE `contenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nombre_usuario` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contraseña_usuario` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ciudad_residencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'u1@gmail.com','Luis','','Madrid'),(2,'u2@gmail.com','Felipe','','Barcelona'),(3,'u3@gmail.com','Carlos','','Lugo'),(4,'u4@gmail.com','Ana','','Madrid'),(5,'u5@gmail.com','Maria','','Soria'),(6,'u6@gmail.com','Monica','','Madrid');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `vista1`
--

DROP TABLE IF EXISTS `vista1`;
/*!50001 DROP VIEW IF EXISTS `vista1`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `vista1` (
  `id_user_coment` tinyint NOT NULL,
  `ncoments` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `voto_comment`
--

DROP TABLE IF EXISTS `voto_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `voto_comment` (
  `id_voto_comment` int(11) NOT NULL AUTO_INCREMENT,
  `id_usu_voto_comment` int(11) DEFAULT NULL,
  `id_com_voto_comment` int(11) DEFAULT NULL,
  `valor_voto_comment` int(11) DEFAULT NULL,
  `fecha_voto_commet` date DEFAULT NULL,
  PRIMARY KEY (`id_voto_comment`),
  UNIQUE KEY `Voto_Comment_UN` (`id_usu_voto_comment`,`id_com_voto_comment`),
  KEY `Voto_Comment_FK` (`id_com_voto_comment`),
  CONSTRAINT `Voto_Comment_FK` FOREIGN KEY (`id_com_voto_comment`) REFERENCES `comentario` (`id_comentario`),
  CONSTRAINT `Voto_Comment_FK_1` FOREIGN KEY (`id_usu_voto_comment`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voto_comment`
--

LOCK TABLES `voto_comment` WRITE;
/*!40000 ALTER TABLE `voto_comment` DISABLE KEYS */;
INSERT INTO `voto_comment` VALUES (1,4,3,1,'2020-07-02'),(2,1,2,0,'2019-01-01'),(4,3,4,1,'2019-01-05'),(5,4,2,0,'2021-10-07'),(6,2,1,0,'2020-12-03');
/*!40000 ALTER TABLE `voto_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voto_contenido`
--

DROP TABLE IF EXISTS `voto_contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `voto_contenido` (
  `id_voto_cont` int(11) NOT NULL AUTO_INCREMENT,
  `id_usu_voto_cont` int(11) DEFAULT NULL,
  `id_cont_voto_cont` int(11) DEFAULT NULL,
  `valor_voto_cont` int(11) DEFAULT NULL,
  `fecha_voto_cont` date DEFAULT NULL,
  PRIMARY KEY (`id_voto_cont`),
  UNIQUE KEY `voto_contenido_un` (`id_usu_voto_cont`,`id_cont_voto_cont`),
  KEY `Voto_Contenido_FK` (`id_usu_voto_cont`),
  KEY `Voto_Contenido_FK_1` (`id_cont_voto_cont`),
  CONSTRAINT `Voto_Contenido_FK` FOREIGN KEY (`id_usu_voto_cont`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `Voto_Contenido_FK_1` FOREIGN KEY (`id_cont_voto_cont`) REFERENCES `contenido` (`id_contenido`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voto_contenido`
--

LOCK TABLES `voto_contenido` WRITE;
/*!40000 ALTER TABLE `voto_contenido` DISABLE KEYS */;
INSERT INTO `voto_contenido` VALUES (1,3,4,1,'2021-02-02'),(2,4,4,-1,'2019-07-05'),(4,2,3,1,'2021-11-04'),(6,1,3,-1,'2020-05-05'),(7,2,2,1,'2019-12-01'),(8,4,5,1,'2021-07-03'),(9,2,6,1,'2020-01-04'),(11,4,6,-1,'2021-03-15');
/*!40000 ALTER TABLE `voto_contenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'yiutube'
--

--
-- Final view structure for view `vista1`
--

/*!50001 DROP TABLE IF EXISTS `vista1`*/;
/*!50001 DROP VIEW IF EXISTS `vista1`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista1` AS (select `c`.`id_user_coment` AS `id_user_coment`,count(`c`.`id_user_coment`) AS `ncoments` from `comentario` `c` group by `c`.`id_user_coment`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-13  0:36:02
