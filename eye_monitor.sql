-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 22, 2020 at 07:56 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `eye_monitor`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `mobile`) VALUES
('admin', 'admin', 9976570006);

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `id` int(11) NOT NULL default '0',
  `carno` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `location` varchar(30) NOT NULL,
  `dtime` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`id`, `carno`, `name`, `location`, `dtime`) VALUES
(1, '1', 'Arun', '10.83187613847706, 78.69445187', '2020-01-11 19:14:57'),
(2, '1122', '', ', ', '2020-01-18 19:11:25'),
(3, '1122', '', ', ', '2020-01-18 19:11:41'),
(4, '1122', 'Arun', '10.831701065491272, 78.6945494', '2020-01-18 19:11:57'),
(5, '1122', 'Arun', '10.831647628333762, 78.6944106', '2020-01-18 19:12:42'),
(6, '1122', 'Arun', '10.831574937251673, 78.6941672', '2020-01-18 19:12:58'),
(7, '1122', 'Arun', '10.831694134132901, 78.6942883', '2020-01-18 19:13:15'),
(8, '1122', 'Arun', '10.83171133244155, 78.69448334', '2020-01-18 19:13:31'),
(9, '1122', 'Arun', '10.831522119350897, 78.6943735', '2020-01-18 19:13:46'),
(10, '1122', 'Arun', '10.831741151558184, 78.6944973', '2020-01-18 19:14:01'),
(11, '1122', '', ', ', '2020-01-18 19:15:08'),
(12, '1122', '', ', ', '2020-01-18 19:15:28'),
(13, '1122', '', ', ', '2020-01-18 19:15:47'),
(14, '1122', 'Arun', '10.831736825588806, 78.6945388', '2020-01-18 19:17:53'),
(15, '1122', 'Arun', '10.831717204060844, 78.6945898', '2020-01-18 19:20:09'),
(16, '1122', 'Arun', '10.831839043703896, 78.6942609', '2020-01-22 13:17:40');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `carno` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `mobile2` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(50) NOT NULL,
  UNIQUE KEY `carno` (`carno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`carno`, `name`, `mobile`, `mobile2`, `email`, `address`) VALUES
('1122', 'Arun', 9976570006, 9976570006, 'arun@gmail.com', '22,chatram'),
('1133', 'cherry', 9976570006, 9789676560, 'cherry@gmail.com', '11,trichy');
