-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: norman
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `argentbet`
--

DROP TABLE IF EXISTS `argentbet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `argentbet` (
  `idbet` int(255) NOT NULL,
  `amountbet` int(255) DEFAULT NULL,
  PRIMARY KEY (`idbet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `argentbet`
--

LOCK TABLES `argentbet` WRITE;
/*!40000 ALTER TABLE `argentbet` DISABLE KEYS */;
INSERT INTO `argentbet` VALUES (1,810);
/*!40000 ALTER TABLE `argentbet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historique_killing`
--

DROP TABLE IF EXISTS `historique_killing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `historique_killing` (
  `id` varchar(255) DEFAULT NULL,
  `temps` datetime DEFAULT CURRENT_TIMESTAMP,
  `target` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historique_killing`
--

LOCK TABLES `historique_killing` WRITE;
/*!40000 ALTER TABLE `historique_killing` DISABLE KEYS */;
/*!40000 ALTER TABLE `historique_killing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historique_mining`
--

DROP TABLE IF EXISTS `historique_mining`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `historique_mining` (
  `id` varchar(255) DEFAULT NULL,
  `temps` datetime DEFAULT CURRENT_TIMESTAMP,
  `type_action` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historique_mining`
--

LOCK TABLES `historique_mining` WRITE;
/*!40000 ALTER TABLE `historique_mining` DISABLE KEYS */;
/*!40000 ALTER TABLE `historique_mining` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uti`
--

DROP TABLE IF EXISTS `uti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `uti` (
  `id` varchar(255) DEFAULT NULL,
  `score` bigint(255) DEFAULT NULL,
  `pick` int(255) DEFAULT '1',
  `idweapon` int(11) DEFAULT '0',
  `health` int(255) DEFAULT '20',
  `armor` int(255) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uti`
--

LOCK TABLES `uti` WRITE;
/*!40000 ALTER TABLE `uti` DISABLE KEYS */;
/*!40000 ALTER TABLE `uti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utiweapon`
--

DROP TABLE IF EXISTS `utiweapon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `utiweapon` (
  `iduser` varchar(255) NOT NULL,
  `idweapon` varchar(255) NOT NULL,
  PRIMARY KEY (`iduser`,`idweapon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utiweapon`
--

LOCK TABLES `utiweapon` WRITE;
/*!40000 ALTER TABLE `utiweapon` DISABLE KEYS */;
/*!40000 ALTER TABLE `utiweapon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weaponlist`
--

DROP TABLE IF EXISTS `weaponlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `weaponlist` (
  `id` int(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `damage` int(11) DEFAULT NULL,
  `speed` int(11) DEFAULT NULL,
  `hitChance` double DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `dps` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weaponlist`
--

LOCK TABLES `weaponlist` WRITE;
/*!40000 ALTER TABLE `weaponlist` DISABLE KEYS */;
INSERT INTO `weaponlist` VALUES (1,'Knife',1,2,90,100,0.5),(2,'Dagger',1,2,90,400,0.5),(3,'Hatchet',3,4,80,2700,0.75),(4,'Felling Axe',6,10,80,9600,0.6),(5,'Hand Scythe',5,5,70,12500,1),(6,'Small Hammer',3,3,90,10800,1),(7,'Spike Hammer',9,8,60,44100,1.125),(8,'Great Axe',22,11,30,140800,2),(9,'Scimitar',10,8,70,81000,1.25),(10,'Bastard Sword',11,8,40,110000,1.375),(11,'Large Scythe',13,13,50,157300,1),(12,'Spear',6,4,80,86400,1.5),(13,'Long Sword',9,6,90,152100,1.5),(14,'Great Sword',16,10,60,313600,1.6),(15,'Cutlass',9,5,80,202500,1.8),(16,'Morning Star',11,11,30,281600,1),(17,'Sabre',6,3,70,173400,2),(18,'Whip',6,3,30,194400,2),(19,'Rapier',6,2,60,216600,3),(0,'Fist',1,1,20,0,1);
/*!40000 ALTER TABLE `weaponlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-14 16:41:18
