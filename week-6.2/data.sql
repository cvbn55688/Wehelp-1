-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: website_HW
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `headimg`
--

DROP TABLE IF EXISTS `headimg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `headimg` (
  `user_id` bigint NOT NULL,
  `img_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `headimg_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `headimg`
--

LOCK TABLES `headimg` WRITE;
/*!40000 ALTER TABLE `headimg` DISABLE KEYS */;
INSERT INTO `headimg` VALUES (1,'1666857417'),(2,'1666857417'),(3,'1666857417'),(11,'1666857417'),(12,'1666857417'),(13,'1666857417'),(14,'1666857417'),(15,'1666857417'),(16,'1666857417'),(20,'1666857417'),(22,'1666857417'),(23,'1666857417'),(24,'1666857417'),(25,'1666857417'),(26,'1666857417'),(27,'1666857417');
/*!40000 ALTER TABLE `headimg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `headIMG` varchar(30) DEFAULT '1666857417.png',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'name1','test1','test1','1666870703.jpg'),(2,'name2','test2','test2','1666873222.gif'),(3,'ZH','test','test','1666949444.669684.jpg'),(11,'name3','test3','test3','1666941908.2427313.jpg'),(12,'Zhi_Han','testtest','testtest','1666869459.jpeg'),(13,'芒果','123','123','1666870578.jpg'),(14,'西瓜','456','456','1666857417.png'),(15,'南瓜','789','789','1666857417.png'),(16,'終極測試員','super','super','1666857417.png'),(20,'終極測試員2號','super2','super2','1666857417.png'),(22,'ZHHH','test123','test123','1666857417.png'),(23,'小白Z','123123','123123','1666857417.png'),(24,'超級測試員4號','super4','super4','1666871836.jpg'),(25,'阿肥肚子餓!!','pfg','pfg','1666857417.png'),(26,'超級測試員3號','super3','super3','1666857417.png'),(27,'超級測試員5號','super5','super5','1666878280.jpg'),(31,'qwe','qwe','qwe','1666940095.jpg'),(32,'asd','asd','asd','1666940456.0780187.gif'),(33,'aa','test8','test8','1666951238.733639.png');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userid` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'0.0','2022-10-24 19:51:37'),(2,3,'嗨嗨','2022-10-24 20:52:58'),(3,3,'來測試測試','2022-10-24 21:03:01'),(4,13,'insert測試','2022-10-24 21:22:39'),(5,16,'終極測試v1','2022-10-24 21:40:42'),(6,12,'讚啦終於做完了','2022-10-24 21:47:03'),(10,20,'終極測試v2','2022-10-24 22:05:28'),(11,22,'哈哈','2022-10-24 22:13:32'),(12,3,'0.0','2022-10-24 22:20:48'),(13,3,'=_=','2022-10-24 22:26:43'),(14,24,'終極測試v4','2022-10-24 22:27:45'),(15,25,'肚子好餓!!','2022-10-25 00:44:47'),(16,3,'ss','2022-10-25 16:41:44'),(17,26,'終極測試v3','2022-10-25 16:42:37'),(22,1,'測試頭貼','2022-10-27 19:40:53'),(23,14,'預設頭貼測試','2022-10-27 19:58:30'),(24,15,'我是南瓜','2022-10-27 19:58:45'),(25,2,'GIF測試','2022-10-27 20:20:31'),(26,3,'0.0','2022-10-27 21:43:47'),(27,27,'.','2022-10-27 21:44:44'),(28,11,'ˊˇˋ','2022-10-28 15:25:21'),(29,3,'= =','2022-10-28 16:00:02'),(30,3,'測試pool','2022-10-28 16:10:30'),(31,1,'測試pool2','2022-10-28 16:10:40'),(32,3,'test','2022-10-28 17:22:24'),(33,33,'123123','2022-10-28 18:00:43');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-28 18:03:05
