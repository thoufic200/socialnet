-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 28, 2024 at 11:51 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2socialnetpyemo`
--

-- --------------------------------------------------------

--
-- Table structure for table `comtb`
--

CREATE TABLE `comtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `uname` varchar(250) NOT NULL,
  `frname` varchar(250) NOT NULL,
  `comment` varchar(250) NOT NULL,
  `Ccount` bigint(250) NOT NULL,
  `shareid` varchar(250) NOT NULL,
  `smile1` int(20) NOT NULL,
  `smile2` int(20) NOT NULL,
  `smile3` int(20) NOT NULL,
  `smile4` int(20) NOT NULL,
  `smile5` int(20) NOT NULL,
  `smile6` int(20) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `comtb`
--

INSERT INTO `comtb` (`id`, `uname`, `frname`, `comment`, `Ccount`, `shareid`, `smile1`, `smile2`, `smile3`, `smile4`, `smile5`, `smile6`) VALUES
(1, 'san1', 'san1', 'good', 0, '1', 0, 0, 0, 0, 0, 0),
(2, 'san1', 'san1', 'bad', 1, '1', 0, 0, 0, 0, 0, 1),
(3, 'san1', 'san1', 'bad', 1, '1', 0, 0, 0, 0, 0, 1),
(4, 'san1', 'san1', 'bad', 1, '1', 0, 0, 0, 0, 0, 1),
(5, 'san1', 'san1', 'bad', 1, '1', 0, 0, 0, 0, 0, 1),
(6, 'san1', 'san2', 'good', 0, '2', 0, 0, 0, 0, 0, 0),
(7, 'san1', 'san2', 'bad ', 1, '2', 0, 0, 0, 0, 0, 1),
(8, 'san1', 'san2', 'bad', 1, '2', 0, 0, 0, 0, 0, 1),
(9, 'san1', 'san2', 'bad', 1, '2', 0, 0, 0, 0, 0, 1),
(10, 'san1', 'san2', 'bad', 1, '2', 0, 0, 0, 0, 0, 1),
(11, 'san1', 'san2', 'bad', 0, '2', 0, 0, 0, 0, 0, 1),
(12, 'san3', 'san1', 'bad', 1, '6699', 0, 0, 0, 1, 0, 0),
(13, 'san3', 'san1', 'good', 0, '6699', 1, 0, 0, 0, 0, 0),
(14, 'paws', 'san2', 'good', 0, '1363', 1, 0, 0, 0, 0, 0),
(15, 'naga', 'san2', 'bad', 1, '7844', 0, 0, 0, 0, 0, 1),
(16, 'naga', 'san2', 'bad', 1, '7844', 0, 0, 0, 0, 0, 1),
(17, 'naga', 'san2', 'bad', 1, '7844', 0, 0, 0, 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `frlist`
--

CREATE TABLE `frlist` (
  `id` bigint(250) NOT NULL auto_increment,
  `uname` varchar(250) NOT NULL,
  `Frname` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=63 ;

--
-- Dumping data for table `frlist`
--

INSERT INTO `frlist` (`id`, `uname`, `Frname`, `Status`) VALUES
(1, 'san2', 'san1', 'Blocked'),
(2, 'san1', 'san2', 'Blocked'),
(3, 'san3', 'san1', 'Accept'),
(4, 'san1', 'san3', 'Accept'),
(5, 'san3', 'san2', 'waiting'),
(6, 'san2', 'san3', '0'),
(7, 'paws', 'san1', 'waiting'),
(8, 'san1', 'paws', '0'),
(9, 'san2', 'san1', '0'),
(10, 'san1', 'san2', '0'),
(11, 'san2', 'paws', 'Accept'),
(12, 'paws', 'san2', 'Accept'),
(13, 'san35', 'sangeeth Kumar', '0'),
(14, 'sangeeth Kumar', 'san35', '0'),
(15, 'san35', 'paws', '0'),
(16, 'paws', 'san35', '0'),
(17, 'san35', 'san2', 'waiting'),
(18, 'san2', 'san35', '0'),
(19, 'sabn', 'san1', '0'),
(20, 'san1', 'sabn', '0'),
(21, 'sabn', 'paws', '0'),
(22, 'paws', 'sabn', '0'),
(23, 'sabn', 'san2', '0'),
(24, 'san2', 'sabn', '0'),
(25, 'sabn', 'san35', '0'),
(26, 'san35', 'sabn', '0'),
(27, 'san', 'san1', '0'),
(28, 'san1', 'san', '0'),
(29, 'san', 'paws', '0'),
(30, 'paws', 'san', '0'),
(31, 'san', 'san2', '0'),
(32, 'san2', 'san', '0'),
(33, 'san', 'san35', '0'),
(34, 'san35', 'san', '0'),
(35, 'san', 'sabn', '0'),
(36, 'sabn', 'san', '0'),
(37, 'karthi', 'san1', '0'),
(38, 'san1', 'karthi', '0'),
(39, 'karthi', 'paws', '0'),
(40, 'paws', 'karthi', '0'),
(41, 'karthi', 'san2', '0'),
(42, 'san2', 'karthi', '0'),
(43, 'karthi', 'san35', '0'),
(44, 'san35', 'karthi', '0'),
(45, 'karthi', 'sabn', '0'),
(46, 'sabn', 'karthi', '0'),
(47, 'karthi', 'san', 'Accept'),
(48, 'san', 'karthi', 'Accept'),
(49, 'naga', 'san1', 'Accept'),
(50, 'san1', 'naga', 'Accept'),
(51, 'naga', 'paws', '0'),
(52, 'paws', 'naga', '0'),
(53, 'naga', 'san2', 'Blocked'),
(54, 'san2', 'naga', 'Blocked'),
(55, 'naga', 'san35', '0'),
(56, 'san35', 'naga', '0'),
(57, 'naga', 'sabn', '0'),
(58, 'sabn', 'naga', '0'),
(59, 'naga', 'san', '0'),
(60, 'san', 'naga', '0'),
(61, 'naga', 'karthi', '0'),
(62, 'karthi', 'naga', '0');

-- --------------------------------------------------------

--
-- Table structure for table `negtb`
--

CREATE TABLE `negtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `words` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `negtb`
--


-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pnumber` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `Gender`, `Age`, `address`, `email`, `pnumber`, `uname`, `password`, `image`, `Status`) VALUES
(1, 'sangeeth Kumar', 'male', '40', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '09486365535', 'san1', 'san1', 'lungaca7.jpeg', 'Active'),
(2, 'paws', 'female', '20', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '9486365535', 'paws', 'paws', '1.jpg', 'Blocked'),
(3, 'san2', 'male', '20', 'No 16 samnath plaza, melapudur  trichy', 'sangeeth5535@gmail.com', '7904902206', 'san2', 'san2', '1.jpg', 'Active'),
(4, 'san35', 'male', '20', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '09486365535', 'san35', 'san35', '76.jpg', 'Active'),
(5, 'sabn', 'male', '40', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '9486365535', 'sabn', 'name', '76.jpg', 'Active'),
(6, 'san', 'male', '20', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '9486365535', 'san', 'san', '76.jpg', 'Active'),
(7, 'karthi', 'male', '20', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '9486365535', 'karthi', 'karthi', 'image_1.jpg', 'Active'),
(8, 'naga', 'male', '20', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhu', 'sangeeth5535@gmail.com', '9486365535', 'naga', 'naga', '_4_5317326.jpg', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `sharetb`
--

CREATE TABLE `sharetb` (
  `id` bigint(20) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `ImageInfo` varchar(500) NOT NULL,
  `Image` varchar(250) NOT NULL,
  `FrName` varchar(250) NOT NULL,
  `Ccount` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sharetb`
--

INSERT INTO `sharetb` (`id`, `UserName`, `ImageInfo`, `Image`, `FrName`, `Ccount`) VALUES
(5626, 'san1', 'my', '001_F_BC1.png', 'san1', 0),
(5626, 'san1', 'my', '001_F_BC1.png', 'san3', 0),
(1595, 'san1', 'my', '003_F_BC1.png', 'san1', 0),
(1595, 'san1', 'my', '003_F_BC1.png', 'san3', 1),
(9142, 'san1', 'my', '003_F_CR3.png', 'san1', 0),
(9142, 'san1', 'my', '003_F_CR3.png', 'san3', 1),
(4811, 'san1', 'my', '003_F_CR3.png', 'san1', 0),
(4811, 'san1', 'my', '003_F_CR3.png', 'san3', 1),
(9453, 'paws', 'nautral', 'image_1.jpg', 'paws', 0),
(9453, 'paws', 'nautral', 'image_1.jpg', 'san2', 1),
(2861, 'paws', 'social', '701Test.jpg', 'paws', 0),
(2861, 'paws', 'social', '701Test.jpg', 'san2', 1),
(9616, 'paws', 'nautral', '206image_1.jpg', 'paws', 0),
(9616, 'paws', 'nautral', '206image_1.jpg', 'san2', 0),
(8350, 'paws', 'natural', '445image_1.jpg', 'paws', 0),
(8350, 'paws', 'natural', '445image_1.jpg', 'san2', 0),
(1363, 'paws', 'natural', '879Test.jpg', 'paws', 0),
(1363, 'paws', 'natural', '879Test.jpg', 'san2', 1),
(9355, 'san2', 'natural', '003_F_CR1.png', 'san2', 0),
(9355, 'san2', 'natural', '003_F_CR1.png', 'paws', 1),
(7423, 'san2', '', '003_F_CR1.png', 'san2', 0),
(7423, 'san2', '', '003_F_CR1.png', 'paws', 1),
(6760, 'san2', 'natural', '003_F_CR1.png', 'san2', 0),
(6760, 'san2', 'natural', '003_F_CR1.png', 'paws', 1),
(1525, 'san', 'natural', '364image_18.jpg', 'san', 0),
(4233, 'karthi', 'nay', '239image_18.jpg', 'karthi', 0),
(4233, 'karthi', 'nay', '239image_18.jpg', 'san', 1),
(3678, 'karthi', 'af', '218image_1.jpg', 'karthi', 0),
(3678, 'karthi', 'af', '218image_1.jpg', 'san', 0),
(7844, 'naga', 'natu', '952image_1.jpg', 'naga', 0),
(7844, 'naga', 'natu', '952image_1.jpg', 'san1', 0),
(7844, 'naga', 'natu', '952image_1.jpg', 'san2', 0),
(8620, 'naga', 'no', '274image_18.jpg', 'naga', 0),
(8620, 'naga', 'no', '274image_18.jpg', 'san1', 1),
(5978, 'naga', 'natural', '782image_18.jpg', 'naga', 0),
(5978, 'naga', 'natural', '782image_18.jpg', 'san1', 1),
(1505, 'naga', 'sdgds', '928image_18.jpg', 'naga', 0),
(1505, 'naga', 'sdgds', '928image_18.jpg', 'san1', 1);
