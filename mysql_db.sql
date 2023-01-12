-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        5.7.28-log - MySQL Community Server (GPL)
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- payhere 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `payhere` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `payhere`;

-- 테이블 payhere.accountbook_accountbook 구조 내보내기
CREATE TABLE IF NOT EXISTS `accountbook_accountbook` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(100) NOT NULL,
  `memo` varchar(300) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accountbook_accountbook_user_id_2c6a7ef6_fk_user_user_id` (`user_id`),
  CONSTRAINT `accountbook_accountbook_user_id_2c6a7ef6_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- 테이블 데이터 payhere.accountbook_accountbook:~0 rows (대략적) 내보내기
DELETE FROM `accountbook_accountbook`;


-- 테이블 payhere.django_migrations 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

-- 테이블 payhere.django_session 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 테이블 payhere.user_user 구조 내보내기
CREATE TABLE IF NOT EXISTS `user_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- 테이블 데이터 payhere.user_user:~3 rows (대략적) 내보내기
DELETE FROM `user_user`;
INSERT INTO `user_user` (`id`, `last_login`, `username`, `password`, `is_active`, `is_admin`) VALUES
	(1, NULL, 'ABC@gmail.com', 'pbkdf2_sha256$320000$xMkKYwrkq28t6iE0yPCsnn$Iwyw1RTpD82yZ75sJ5xiWavbTrFm1ViNRvJhzesa4gc=', 1, 0),
	(2, NULL, 'abc1212@gmail.com', 'pbkdf2_sha256$320000$NuqFdoKOwsVz507AU52od5$mgMJZH/KzOXeZch3hvfc/+cg1D9OVt/PSy6VlqEAeHI=', 1, 0),

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
