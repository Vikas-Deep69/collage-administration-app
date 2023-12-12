-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2023 at 06:34 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recodir`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_assignment`
--

CREATE TABLE `add_assignment` (
  `id` int(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `number` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_assignment`
--

INSERT INTO `add_assignment` (`id`, `course`, `department`, `subject`, `number`) VALUES
(4, 'CSE', 'CSE/IT', 'CN', 2),
(5, 'BCA', 'CSE/IT', 'OS', 3);

-- --------------------------------------------------------

--
-- Table structure for table `add_course`
--

CREATE TABLE `add_course` (
  `id` int(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Duration` varchar(50) NOT NULL,
  `Cost` bigint(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_course`
--

INSERT INTO `add_course` (`id`, `Name`, `Duration`, `Cost`) VALUES
(12, 'CSE', '4 YEARS', 400000),
(13, 'CSE/IOT', '4 YEARS', 400000),
(14, 'BCA', '3 YEARS', 320000);

-- --------------------------------------------------------

--
-- Table structure for table `add_material`
--

CREATE TABLE `add_material` (
  `id` int(11) NOT NULL,
  `course` varchar(50) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Subject` varchar(50) NOT NULL,
  `Topic` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_material`
--

INSERT INTO `add_material` (`id`, `course`, `Department`, `Subject`, `Topic`) VALUES
(5, 'CSE', 'CSE/IT', 'CN', 'TCP/IP'),
(6, 'CSE', 'CSE/IT', 'OS', 'Paging'),
(7, 'CSE', 'CSE/IT', '{Advance Data Structure}', 'queue'),
(8, 'BCA', 'CSE/IT', 'python', 'operators');

-- --------------------------------------------------------

--
-- Table structure for table `add_subject`
--

CREATE TABLE `add_subject` (
  `id` int(50) NOT NULL,
  `Degree` varchar(50) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_subject`
--

INSERT INTO `add_subject` (`id`, `Degree`, `Course`, `Name`) VALUES
(1, 'Btech', 'CSE', 'DAA'),
(2, 'Btech', 'CSE', 'FLAT'),
(3, 'Btech', 'BCA', 'python'),
(4, 'Mtech', 'CSE', 'Advance Data Structure');

-- --------------------------------------------------------

--
-- Table structure for table `add_teacher`
--

CREATE TABLE `add_teacher` (
  `id` int(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Contact` bigint(11) NOT NULL,
  `Qualification` varchar(50) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Subject` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_teacher`
--

INSERT INTO `add_teacher` (`id`, `Name`, `Contact`, `Qualification`, `Username`, `Password`, `Subject`) VALUES
(16, 'Vikas', 8506045632, 'Btech', 'vikas', '123', 'DAA'),
(17, 'jatin', 7894561256, 'Btech', 'jatin123', '321', 'FLAT'),
(18, 'Akarshak', 4561597538, 'PhD', 'akarshak', '123', '{Advance Data Structure}');

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL DEFAULT 'admin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`id`, `username`, `password`, `usertype`) VALUES
(1, 'admin', 'Hello@123', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `btech`
--

CREATE TABLE `btech` (
  `id` int(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `btech`
--

INSERT INTO `btech` (`id`, `name`, `username`, `password`) VALUES
(2, 'vikas', 'vikasdeep', '123'),
(3, 'nikhil', 'nikhil1', '12345'),
(6, 'sahil', 'sahil786', '456'),
(8, 'deepak', 'deep', '696'),
(10, 'hello', 'hi', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_assignment`
--
ALTER TABLE `add_assignment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `add_course`
--
ALTER TABLE `add_course`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `add_material`
--
ALTER TABLE `add_material`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `add_subject`
--
ALTER TABLE `add_subject`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `add_teacher`
--
ALTER TABLE `add_teacher`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `btech`
--
ALTER TABLE `btech`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_assignment`
--
ALTER TABLE `add_assignment`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `add_course`
--
ALTER TABLE `add_course`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `add_material`
--
ALTER TABLE `add_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `add_subject`
--
ALTER TABLE `add_subject`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `add_teacher`
--
ALTER TABLE `add_teacher`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `admin_login`
--
ALTER TABLE `admin_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `btech`
--
ALTER TABLE `btech`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
