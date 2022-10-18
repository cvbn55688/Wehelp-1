-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: website
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
-- Table structure for table `likecount`
--

DROP TABLE IF EXISTS `likecount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likecount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mess_id` bigint NOT NULL,
  `who_like` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mess_id` (`mess_id`),
  CONSTRAINT `likecount_ibfk_1` FOREIGN KEY (`mess_id`) REFERENCES `message` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likecount`
--

LOCK TABLES `likecount` WRITE;
/*!40000 ALTER TABLE `likecount` DISABLE KEYS */;
INSERT INTO `likecount` VALUES (1,1,'Zhi_Han'),(2,2,'Zhi_Han'),(3,3,'Zhi_Han'),(4,4,'Zhi_Han'),(5,6,'Zhi_Han'),(6,7,'Zhi_Han'),(7,1,'name1'),(8,2,'name1'),(9,3,'name1'),(10,4,'name1'),(12,6,'name1'),(13,7,'name1'),(14,1,'name2'),(15,2,'name2'),(16,3,'name2'),(17,4,'name2'),(18,6,'name2'),(19,1,'name3'),(20,2,'name3'),(21,3,'name3'),(22,4,'name3'),(23,1,'name4'),(24,2,'name4'),(25,3,'name4'),(26,1,'name6'),(27,2,'name6'),(28,1,'name7'),(33,3,'name6'),(34,6,'name6');
/*!40000 ALTER TABLE `likecount` ENABLE KEYS */;
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
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'Zhi_Han','test','test',500,'2022-10-17 14:47:50'),(2,'name2','test2','test2',345,'2022-10-17 14:57:39'),(3,'name3','test3','test3',345,'2022-10-17 14:57:45'),(4,'name4','test4','test4',567,'2022-10-17 14:57:52'),(5,'name5','test5','test5',567,'2022-10-17 14:57:58'),(6,'name6','test6','test6',567,'2022-10-17 14:58:12');
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
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'我真的很想睡覺',6,'2022-10-17 16:08:11'),(2,4,'這次我一定要去跑步',5,'2022-10-17 16:08:52'),(3,2,'我要去看中醫',4,'2022-10-17 16:11:34'),(4,1,'Hello World',3,'2022-10-17 16:24:10'),(6,1,'資料結構，從入門到放棄',2,'2022-10-17 16:25:06'),(7,1,'冬天就是要吃火鍋',1,'2022-10-17 16:25:51');
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

-- Dump completed on 2022-10-18 22:27:27
