-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 06, 2020 at 07:48 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `acses`
--

-- --------------------------------------------------------

--
-- Table structure for table `attended_emails`
--

CREATE TABLE `attended_emails` (
  `id` int(11) NOT NULL,
  `from_email` varchar(50) NOT NULL,
  `subject` varchar(1000) DEFAULT NULL,
  `body` varchar(10000) NOT NULL,
  `intent` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attended_emails`
--

INSERT INTO `attended_emails` (`id`, `from_email`, `subject`, `body`, `intent`) VALUES
(13, 'Shreyas S <s.shreyas.blr@gmail.com>', 'Message from shreyas', 'I need to know my order details\r\n', 'order_status');

-- --------------------------------------------------------

--
-- Table structure for table `forwarded_emails`
--

CREATE TABLE `forwarded_emails` (
  `id` int(11) NOT NULL,
  `from_email` varchar(50) NOT NULL,
  `subject` varchar(1000) NOT NULL,
  `body` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `intent_response`
--

CREATE TABLE `intent_response` (
  `id` int(11) NOT NULL,
  `intent` varchar(100) NOT NULL,
  `response` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `intent_response`
--

INSERT INTO `intent_response` (`id`, `intent`, `response`) VALUES
(1, 'order_status', 'This is a response for order status.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attended_emails`
--
ALTER TABLE `attended_emails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `forwarded_emails`
--
ALTER TABLE `forwarded_emails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `intent_response`
--
ALTER TABLE `intent_response`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attended_emails`
--
ALTER TABLE `attended_emails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `forwarded_emails`
--
ALTER TABLE `forwarded_emails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `intent_response`
--
ALTER TABLE `intent_response`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
