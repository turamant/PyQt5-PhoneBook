-- MariaDB dump 10.19  Distrib 10.6.3-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: phonebook
-- ------------------------------------------------------
-- Server version	10.6.3-MariaDB

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
-- Table structure for table `phonebook`
--

DROP TABLE IF EXISTS `phonebook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phonebook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nomer` char(12) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nomer` (`nomer`),
  UNIQUE KEY `nomer_2` (`nomer`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phonebook`
--

LOCK TABLES `phonebook` WRITE;
/*!40000 ALTER TABLE `phonebook` DISABLE KEYS */;
INSERT INTO `phonebook` VALUES (61,'Петров','8-9001239192','2000-11-11'),(62,'Петров','8-9001239199','2000-11-11'),(67,'Петров','8-9001239197','2000-08-09'),(68,'Сидоров','8-9001237777','2000-11-11'),(69,'Николаев','8-9001234444','2000-08-05'),(70,'Артамонов','8-9001235555','2000-08-07'),(71,'Чехов','8-9001234343','1998-08-11'),(72,'Якобсон','8-9001236789','1991-08-05'),(73,'Циолковский','8-9001231112','1992-08-10'),(74,'Юшкин','8-9001235656','1994-09-01'),(75,'Эманалиев','8-9001235644','1980-09-01'),(76,'Щегловитый','8-9001237878','1992-08-09'),(77,'Федоров','8-9001231122','2002-09-01'),(78,'Харлампиев','8-9001231133','2002-10-01'),(79,'Терещенко','8-9001233322','1972-09-09'),(80,'Усманов','8-9001233321','1972-09-08'),(81,'Рязанов','8-9001237776','2000-11-12'),(82,'Охлобыстин','8-9001239188','1988-08-08'),(83,'Мураев','8-9001234488','2000-08-06'),(84,'Климов','8-9004444444','2000-09-09'),(85,'Лукин','8-9004444777','2000-10-29'),(86,'Жеглов','8-9004444488','2000-11-11'),(87,'Зиновьев','8-9004444555','2004-11-15'),(88,'Иртеньев','8-9004477555','2004-12-15'),(89,'Дмитриев','8-9034444555','2004-11-17'),(90,'Егоров','8-8034444559','2004-11-27'),(91,'Васильев','8-7564444559','2004-09-27'),(92,'Гаврилов','8-7568889090','2004-08-27'),(94,'Rossum','4-2890123456','1956-01-31'),(95,'Beazly','4-9876543212','1964-11-12'),(96,'Lutz','8-8902890123','1941-03-01'),(97,'Зубов','8-9004444557','2004-11-17'),(98,'Кириенко','8-888-888888','1988-01-18'),(99,'Veritas','8-9006007878','1999-09-09'),(100,'Иванидзе','8-2009008989','1999-01-01'),(101,'Баранов','8-2009019090','1991-12-12'),(102,'Цуканов','8-9001234543','0200-00-00'),(104,'Akademik','8-9009018956','1991-12-11'),(105,'Ginzburg','8-8009012310','2000-10-10'),(106,'Кудасов','8-6004566547','2000-01-09'),(108,'Сикорский','8-9009001265','2001-08-29'),(109,'Демшин','8-7776776587','2000-02-23'),(110,'Ялов','8-9128735612','2012-09-12');
/*!40000 ALTER TABLE `phonebook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `save` char(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (22,'admin','1','1','2000-01-01'),(24,'q1','1',NULL,'1990-04-03');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-10 15:12:48
