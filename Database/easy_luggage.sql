-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2023 at 02:26 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `easy_luggage`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(5) NOT NULL,
  `admin_name` varchar(40) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_name`, `phone`, `email`, `password`, `created_at`) VALUES
(1, 'admin', '9898989898', 'admin@gmail.com', 'AdminPass', '2023-11-28 16:48:35');

-- --------------------------------------------------------

--
-- Table structure for table `branch_details`
--

CREATE TABLE `branch_details` (
  `branch_id` int(11) NOT NULL,
  `branch_name` varchar(40) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `address1` varchar(40) NOT NULL,
  `address2` varchar(40) NOT NULL,
  `district` varchar(40) NOT NULL,
  `state` varchar(40) NOT NULL,
  `zip` varchar(40) NOT NULL,
  `manager_name` varchar(20) NOT NULL,
  `manager_mail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branch_details`
--

INSERT INTO `branch_details` (`branch_id`, `branch_name`, `phone`, `email`, `address1`, `address2`, `district`, `state`, `zip`, `manager_name`, `manager_mail`) VALUES
(1, 'Tiruchchirappalli', '', '', '', '', '', '', '', '', 'prithivirajk2503@gmail.com'),
(2, 'Chennai', '', '', '', '', '', '', '', '', 'prithivirajk2503@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `cust_query`
--

CREATE TABLE `cust_query` (
  `query_id` int(5) NOT NULL,
  `user_id` varchar(5) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `query` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cust_query`
--

INSERT INTO `cust_query` (`query_id`, `user_id`, `subject`, `query`, `created_at`) VALUES
(1, '5', 'Feedback', 'I don\'t like the service., its too late', '2023-12-03 07:28:00'),
(2, '5', 'Query?', 'I really love the process', '2023-12-03 07:29:08'),
(3, '5', 'Feed', 'It\'s ok but better if improve the delivery time', '2023-12-03 07:30:46');

-- --------------------------------------------------------

--
-- Table structure for table `goods_receiving`
--

CREATE TABLE `goods_receiving` (
  `gr_id` int(5) NOT NULL,
  `from_branch` varchar(40) NOT NULL,
  `to_branch` varchar(40) NOT NULL,
  `luggage_id` varchar(40) NOT NULL,
  `actual` varchar(5) NOT NULL,
  `received` varchar(5) NOT NULL,
  `missed` varchar(5) NOT NULL,
  `comments` varchar(255) NOT NULL,
  `admin_id` varchar(5) NOT NULL,
  `received_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `goods_receiving`
--

INSERT INTO `goods_receiving` (`gr_id`, `from_branch`, `to_branch`, `luggage_id`, `actual`, `received`, `missed`, `comments`, `admin_id`, `received_at`) VALUES
(1, '1', '2', '1', '5', '3', '2', 'Yes', '1', '2023-12-03 18:22:07'),
(2, '1', '2', '1', '5', '3', '2', 'Yes', '1', '2023-12-03 18:22:44'),
(3, '1', '2', '1', '5', '4', '', '', '1', '2023-12-03 18:23:00'),
(4, '1', '1', '1', '5', '4', '3', 'Ok', '1', '2023-12-03 18:39:53'),
(5, '1', '1', '1', '5', '3', '1', 'iwu', '1', '2023-12-03 18:40:40');

-- --------------------------------------------------------

--
-- Table structure for table `indian_cities_database`
--

CREATE TABLE `indian_cities_database` (
  `cityid` int(11) NOT NULL,
  `city` varchar(18) DEFAULT NULL,
  `lat` varchar(8) DEFAULT NULL,
  `longt` varchar(8) DEFAULT NULL,
  `country` varchar(7) DEFAULT NULL,
  `iso2` varchar(4) DEFAULT NULL,
  `state` varchar(27) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `indian_cities_database`
--

INSERT INTO `indian_cities_database` (`cityid`, `city`, `lat`, `longt`, `country`, `iso2`, `state`) VALUES
(2, 'Abohar', '30.14453', '74.19552', 'India', 'IN', 'Punjab'),
(3, 'Adilabad', '19.4', '78.31', 'India', 'IN', 'Telangana'),
(4, 'Agartala', '23.83604', '91.27938', 'India', 'IN', 'Tripura'),
(5, 'Agra', '27.18793', '78.00394', 'India', 'IN', 'Uttar Pradesh'),
(6, 'Ahmadnagar', '19.09457', '74.73843', 'India', 'IN', 'Maharashtra'),
(7, 'Ahmedabad', '23.02579', '72.58726', 'India', 'IN', 'Gujarat'),
(8, 'Aizawl  ', '23.73670', '92.71459', 'India', 'IN', 'Mizoram'),
(9, 'Ajmer', '26.45210', '74.63866', 'India', 'IN', 'Rajasthan'),
(10, 'Akola', '20.70956', '76.99810', 'India', 'IN', 'Maharashtra'),
(11, 'Alappuzha', '9.494647', '76.33110', 'India', 'IN', 'Kerala'),
(12, 'Aligarh', '27.88145', '78.07464', 'India', 'IN', 'Uttar Pradesh'),
(13, 'Alipurduar', '26.4835', '89.52285', 'India', 'IN', 'West Bengal'),
(14, 'Allahabad', '25.44478', '81.84321', 'India', 'IN', 'Uttar Pradesh'),
(15, 'Alwar', '27.56629', '76.61020', 'India', 'IN', 'Rajasthan'),
(16, 'Ambala', '30.36099', '76.79781', 'India', 'IN', 'Haryana'),
(17, 'Amaravati', '20.93327', '77.75152', 'India', 'IN', 'Maharashtra'),
(18, 'Amritsar', '31.62233', '74.87533', 'India', 'IN', 'Punjab'),
(19, 'Asansol', '23.68333', '86.98333', 'India', 'IN', 'West Bengal'),
(20, 'Aurangabad', '19.88094', '75.34673', 'India', 'IN', 'Maharashtra'),
(21, 'Aurangabad', '24.75203', '84.37420', 'India', 'IN', 'Bihar'),
(22, 'Bakshpur', '25.89428', '80.79210', 'India', 'IN', 'Uttar Pradesh'),
(23, 'Bamanpuri', '28.80449', '79.04030', 'India', 'IN', 'Uttar Pradesh'),
(24, 'Baramula', '34.20900', '74.34285', 'India', 'IN', 'Jammu and Kashmir'),
(25, 'Barddhaman', '23.25571', '87.85690', 'India', 'IN', 'West Bengal'),
(26, 'Bareilly', '28.34702', '79.42193', 'India', 'IN', 'Uttar Pradesh'),
(27, 'Belgaum', '15.86264', '74.50853', 'India', 'IN', 'Karnataka'),
(28, 'Bellary', '15.14204', '76.92398', 'India', 'IN', 'Karnataka'),
(29, 'Bengaluru', '12.97706', '77.58710', 'India', 'IN', 'Karnataka'),
(30, 'Bhagalpur', '25.24446', '86.97183', 'India', 'IN', 'Bihar'),
(31, 'Bharatpur', '27.21525', '77.49278', 'India', 'IN', 'Rajasthan'),
(32, 'Bharauri', '27.59820', '81.69470', 'India', 'IN', 'Uttar Pradesh'),
(33, 'Bhatpara', '22.86643', '88.40112', 'India', 'IN', 'West Bengal'),
(34, 'Bhavnagar', '21.77445', '72.15249', 'India', 'IN', 'Gujarat'),
(35, 'Bhilai', '21.20918', '81.42849', 'India', 'IN', 'Chhattisgarh'),
(36, 'Bhilwara', '25.34707', '74.64081', 'India', 'IN', 'Rajasthan'),
(37, 'Bhiwandi', '19.30022', '73.05881', 'India', 'IN', 'Maharashtra'),
(38, 'Bhiwani', '28.79304', '76.13968', 'India', 'IN', 'Haryana'),
(39, 'Bhopal ', '23.25468', '77.40289', 'India', 'IN', 'Madhya Pradesh'),
(40, 'Bhubaneshwar', '20.27241', '85.83385', 'India', 'IN', 'Odisha'),
(41, 'Bhuj', '23.25397', '69.66928', 'India', 'IN', 'Gujarat'),
(42, 'Bhusaval', '21.04364', '75.78505', 'India', 'IN', 'Maharashtra'),
(43, 'Bidar', '17.91330', '77.53010', 'India', 'IN', 'Karnataka'),
(44, 'Bijapur', '16.82771', '75.71898', 'India', 'IN', 'Karnataka'),
(45, 'Bikaner', '28.01762', '73.31495', 'India', 'IN', 'Rajasthan'),
(46, 'Bilaspur', '22.08004', '82.15543', 'India', 'IN', 'Chhattisgarh'),
(47, 'Brahmapur', '19.31151', '84.79290', 'India', 'IN', 'Odisha'),
(48, 'Budaun', '28.03811', '79.12667', 'India', 'IN', 'Uttar Pradesh'),
(49, 'Bulandshahr', '28.40392', '77.85773', 'India', 'IN', 'Uttar Pradesh'),
(50, 'Calicut', '11.24801', '75.78040', 'India', 'IN', 'Kerala'),
(51, 'Chanda', '19.95075', '79.29522', 'India', 'IN', 'Maharashtra'),
(52, 'Chandigarh ', '30.73629', '76.78839', 'India', 'IN', 'Chandigarh'),
(53, 'Chennai', '13.08462', '80.24835', 'India', 'IN', 'Tamil Nadu '),
(54, 'Chikka Mandya', '12.54560', '76.89507', 'India', 'IN', 'Karnataka'),
(55, 'Chirala', '15.82384', '80.35218', 'India', 'IN', 'Andhra Pradesh'),
(56, 'Coimbatore', '11.00554', '76.96612', 'India', 'IN', 'Tamil Nadu '),
(57, 'Cuddalore', '11.74628', '79.76436', 'India', 'IN', 'Tamil Nadu '),
(58, 'Cuttack', '20.52292', '85.78813', 'India', 'IN', 'Odisha'),
(59, 'Daman', '20.41431', '72.83236', 'India', 'IN', 'Daman and Diu'),
(60, 'Davangere', '14.46923', '75.92375', 'India', 'IN', 'Karnataka'),
(61, 'DehraDun', '30.32442', '78.03392', 'India', 'IN', 'Uttarakhand'),
(62, 'Delhi', '28.65195', '77.23149', 'India', 'IN', 'Delhi'),
(63, 'Dhanbad', '23.80198', '86.44324', 'India', 'IN', 'Jharkhand'),
(64, 'Dibrugarh', '27.47988', '94.90837', 'India', 'IN', 'Assam'),
(65, 'Dindigul', '10.36285', '77.97582', 'India', 'IN', 'Tamil Nadu '),
(66, 'Dispur', '26.13563', '91.80068', 'India', 'IN', 'Assam'),
(67, 'Diu', '20.71511', '70.98795', 'India', 'IN', 'Daman and Diu'),
(68, 'Faridabad', '28.41123', '77.31316', 'India', 'IN', 'Haryana'),
(69, 'Firozabad', '27.15091', '78.39780', 'India', 'IN', 'Uttar Pradesh'),
(70, 'Fyzabad', '26.77548', '82.15018', 'India', 'IN', 'Uttar Pradesh'),
(71, 'Gangtok', '27.32573', '88.61215', 'India', 'IN', 'Sikkim'),
(72, 'Gaya', '24.79685', '85.00385', 'India', 'IN', 'Bihar'),
(73, 'Ghandinagar', '23.21666', '72.68333', 'India', 'IN', 'Gujarat'),
(74, 'Ghaziabad', '28.66535', '77.43914', 'India', 'IN', 'Uttar Pradesh'),
(75, 'Gopalpur', '26.73538', '83.38064', 'India', 'IN', 'Uttar Pradesh'),
(76, 'Gulbarga', '17.33582', '76.83757', 'India', 'IN', 'Karnataka'),
(77, 'Guntur', '16.29973', '80.45729', 'India', 'IN', 'Andhra Pradesh'),
(78, 'Gurugram', '28.46010', '77.02635', 'India', 'IN', 'Haryana'),
(79, 'Guwahati', '26.17607', '91.76293', 'India', 'IN', 'Assam'),
(80, 'Gwalior', '26.22982', '78.17336', 'India', 'IN', 'Madhya Pradesh'),
(81, 'Haldia', '22.02527', '88.05833', 'India', 'IN', 'West Bengal'),
(82, 'Haora', '22.57688', '88.31856', 'India', 'IN', 'West Bengal'),
(83, 'Hapur', '28.72984', '77.78068', 'India', 'IN', 'Uttar Pradesh'),
(84, 'Haripur', '31.46321', '75.98641', 'India', 'IN', 'Punjab'),
(85, 'Hata', '27.59269', '78.01384', 'India', 'IN', 'Uttar Pradesh'),
(86, 'Hindupur', '13.82806', '77.49142', 'India', 'IN', 'Andhra Pradesh'),
(87, 'Hisar', '29.15393', '75.72294', 'India', 'IN', 'Haryana'),
(88, 'Hospet', '15.26953', '76.38710', 'India', 'IN', 'Karnataka'),
(89, 'Hubli', '15.34995', '75.13861', 'India', 'IN', 'Karnataka'),
(90, 'Hyderabad', '17.38405', '78.45635', 'India', 'IN', 'Telangana'),
(91, 'Imphal', '24.80805', '93.94420', 'India', 'IN', 'Manipur'),
(92, 'Indore', '22.71773', '75.85859', 'India', 'IN', 'Madhya Pradesh'),
(93, 'Itanagar', '27.10234', '93.69204', 'India', 'IN', 'Arunachal Pradesh'),
(94, 'Jabalpur', '23.17449', '79.93590', 'India', 'IN', 'Madhya Pradesh'),
(95, 'Jaipur', '26.91331', '75.78787', 'India', 'IN', 'Rajasthan'),
(96, 'Jammu', '32.73568', '74.86911', 'India', 'IN', 'Jammu and Kashmir'),
(97, 'Jamshedpur', '22.80277', '86.18544', 'India', 'IN', 'Jharkhand'),
(98, 'Jhansi', '25.45887', '78.57994', 'India', 'IN', 'Uttar Pradesh'),
(99, 'Jodhpur', '26.26841', '73.00594', 'India', 'IN', 'Rajasthan'),
(100, 'Jorhat', '26.75750', '94.20305', 'India', 'IN', 'Assam'),
(101, 'Kagaznagar', '19.33158', '79.46605', 'India', 'IN', 'Andhra Pradesh'),
(102, 'Kakinada', '16.96036', '82.23808', 'India', 'IN', 'Andhra Pradesh'),
(103, 'Kalyan', '19.24370', '73.13553', 'India', 'IN', 'Maharashtra'),
(104, 'Karimnagar', '18.43673', '79.13222', 'India', 'IN', 'Telangana'),
(105, 'Karnal', '29.69197', '76.98448', 'India', 'IN', 'Haryana'),
(106, 'Karur', '10.96027', '78.07675', 'India', 'IN', 'Tamil Nadu '),
(107, 'Kavaratti', '10.56666', '72.61666', 'India', 'IN', 'Lakshadweep'),
(108, 'Khammam', '17.24767', '80.14368', 'India', 'IN', 'Telangana'),
(109, 'Khanapur', '21.27371', '76.11737', 'India', 'IN', 'Maharashtra'),
(110, 'Kochi', '9.947743', '76.25380', 'India', 'IN', 'Kerala'),
(111, 'Kohima', '25.67467', '94.11098', 'India', 'IN', 'Nagaland'),
(112, 'Kolar', '13.13767', '78.12998', 'India', 'IN', 'Karnataka'),
(113, 'Kolhapur', '16.69563', '74.23166', 'India', 'IN', 'Maharashtra'),
(114, 'Kolkata ', '22.56262', '88.36304', 'India', 'IN', 'West Bengal'),
(115, 'Kollam', '8.881131', '76.58469', 'India', 'IN', 'Kerala'),
(116, 'Kota', '25.18254', '75.83906', 'India', 'IN', 'Rajasthan'),
(117, 'Krishnanagar', '23.40576', '88.49073', 'India', 'IN', 'West Bengal'),
(118, 'Krishnapuram', '12.86961', '79.71946', 'India', 'IN', 'Tamil Nadu '),
(119, 'Kumbakonam', '10.95978', '79.37747', 'India', 'IN', 'Tamil Nadu '),
(120, 'Kurnool', '15.82886', '78.03602', 'India', 'IN', 'Andhra Pradesh'),
(121, 'Latur', '18.39948', '76.58425', 'India', 'IN', 'Maharashtra'),
(122, 'Lucknow', '26.83928', '80.92313', 'India', 'IN', 'Uttar Pradesh'),
(123, 'Ludhiana', '30.91204', '75.85378', 'India', 'IN', 'Punjab'),
(124, 'Machilipatnam', '16.18746', '81.13888', 'India', 'IN', 'Andhra Pradesh'),
(125, 'Madurai', '9.917347', '78.11962', 'India', 'IN', 'Tamil Nadu '),
(126, 'Mahabubnagar', '16.75', '78', 'India', 'IN', 'Telangana'),
(127, 'Malegaon Camp', '20.56997', '74.51541', 'India', 'IN', 'Maharashtra'),
(128, 'Mangalore', '12.86537', '74.84243', 'India', 'IN', 'Karnataka'),
(129, 'Mathura', '27.50350', '77.67214', 'India', 'IN', 'Uttar Pradesh'),
(130, 'Meerut', '28.98001', '77.70635', 'India', 'IN', 'Uttar Pradesh'),
(131, 'Mirzapur', '25.14490', '82.56533', 'India', 'IN', 'Uttar Pradesh'),
(132, 'Moradabad', '28.83893', '78.77683', 'India', 'IN', 'Uttar Pradesh'),
(133, 'Mumbai', '18.98780', '72.83644', 'India', 'IN', 'Maharashtra'),
(134, 'Muzaffarnagar', '29.47091', '77.70332', 'India', 'IN', 'Uttar Pradesh'),
(135, 'Muzaffarpur', '26.12259', '85.39055', 'India', 'IN', 'Bihar'),
(136, 'Mysore', '12.29266', '76.63854', 'India', 'IN', 'Karnataka'),
(137, 'Nagercoil', '8.177313', '77.43437', 'India', 'IN', 'Tamil Nadu '),
(138, 'Nalgonda', '17.05', '79.27', 'India', 'IN', 'Telangana'),
(139, 'Nanded', '19.16022', '77.31497', 'India', 'IN', 'Maharashtra'),
(140, 'Nandyal', '15.47799', '78.48360', 'India', 'IN', 'Andhra Pradesh'),
(141, 'Nasik', '19.99996', '73.77688', 'India', 'IN', 'Maharashtra'),
(142, 'Navsari', '20.85', '72.91666', 'India', 'IN', 'Gujarat'),
(143, 'Nellore', '14.44991', '79.98696', 'India', 'IN', 'Andhra Pradesh'),
(144, 'New Delhi', '28.6', '77.2', 'India', 'IN', 'Delhi'),
(145, 'Nizamabad', '18.67315', '78.10008', 'India', 'IN', 'Telangana'),
(146, 'Ongole', '15.50356', '80.04454', 'India', 'IN', 'Andhra Pradesh'),
(147, 'Pali', '25.77512', '73.32061', 'India', 'IN', 'Rajasthan'),
(148, 'Panaji', '15.49828', '73.82454', 'India', 'IN', 'Goa'),
(149, 'Panchkula', '30.69151', '76.85373', 'India', 'IN', 'Haryana'),
(150, 'Panipat', '29.38747', '76.96824', 'India', 'IN', 'Haryana'),
(151, 'Parbhani', '19.26855', '76.77080', 'India', 'IN', 'Maharashtra'),
(152, 'Pathankot', '32.27484', '75.65286', 'India', 'IN', 'Punjab'),
(153, 'Patiala', '30.33624', '76.39219', 'India', 'IN', 'Punjab'),
(154, 'Patna', '25.61537', '85.10102', 'India', 'IN', 'Bihar'),
(155, 'Pilibhit', '28.63124', '79.80436', 'India', 'IN', 'Uttar Pradesh'),
(156, 'Porbandar', '21.64134', '69.60086', 'India', 'IN', 'Gujarat'),
(157, 'Port Blair', '11.66666', '92.75', 'India', 'IN', 'Andaman and Nicobar Islands'),
(158, 'Proddatur', '14.7502', '78.54812', 'India', 'IN', 'Andhra Pradesh'),
(159, 'Puducherry', '11.93381', '79.82979', 'India', 'IN', 'Puducherry'),
(160, 'Pune', '18.51327', '73.84985', 'India', 'IN', 'Maharashtra'),
(161, 'Puri', '19.79825', '85.82493', 'India', 'IN', 'Odisha'),
(162, 'Purnea', '25.77670', '87.47365', 'India', 'IN', 'Bihar'),
(163, 'Raichur', '16.20545', '77.35567', 'India', 'IN', 'Karnataka'),
(164, 'Raipur', '21.23333', '81.63333', 'India', 'IN', 'Chhattisgarh'),
(165, 'Rajahmundry', '17.00517', '81.77783', 'India', 'IN', 'Andhra Pradesh'),
(166, 'Rajapalaiyam', '9.451111', '77.55612', 'India', 'IN', 'Tamil Nadu '),
(167, 'Rajkot', '22.29160', '70.79321', 'India', 'IN', 'Gujarat'),
(168, 'Ramagundam', '18.45', '79.28', 'India', 'IN', 'Telangana'),
(169, 'Rampura', '26.88468', '75.78933', 'India', 'IN', 'Rajasthan'),
(170, 'Ranchi', '23.34776', '85.33856', 'India', 'IN', 'Jharkhand'),
(171, 'Ratlam', '23.33033', '75.04031', 'India', 'IN', 'Madhya Pradesh'),
(172, 'Raurkela', '22.22496', '84.86414', 'India', 'IN', 'Odisha'),
(173, 'Rohtak', '28.89447', '76.58916', 'India', 'IN', 'Haryana'),
(174, 'Saharanpur', '29.96789', '77.54522', 'India', 'IN', 'Uttar Pradesh'),
(175, 'Saidapur', '27.59878', '80.75089', 'India', 'IN', 'Uttar Pradesh'),
(176, 'Saidpur', '34.31817', '74.45709', 'India', 'IN', 'Jammu and Kashmir'),
(177, 'Salem', '11.65116', '78.15867', 'India', 'IN', 'Tamil Nadu '),
(178, 'Samlaipadar', '21.47807', '83.99050', 'India', 'IN', 'Odisha'),
(179, 'Sangli', '16.85677', '74.56919', 'India', 'IN', 'Maharashtra'),
(180, 'Saugor', '23.83876', '78.73873', 'India', 'IN', 'Madhya Pradesh'),
(181, 'Shahbazpur', '27.87411', '79.87932', 'India', 'IN', 'Uttar Pradesh'),
(182, 'Shiliguri', '26.71003', '88.42851', 'India', 'IN', 'West Bengal'),
(183, 'Shillong ', '25.57398', '91.89680', 'India', 'IN', 'Meghalaya'),
(184, 'Shimla', '31.10442', '77.16662', 'India', 'IN', 'Himachal Pradesh'),
(185, 'Shimoga', '13.93242', '75.57255', 'India', 'IN', 'Karnataka'),
(186, 'Sikar', '27.61477', '75.13867', 'India', 'IN', 'Rajasthan'),
(187, 'Silchar', '24.82732', '92.79786', 'India', 'IN', 'Assam'),
(188, 'Silvassa', '20.27385', '72.99672', 'India', 'IN', 'Dadra and Nagar Haveli'),
(189, 'Sirsa', '29.53489', '75.02898', 'India', 'IN', 'Haryana'),
(190, 'Sonipat', '28.99477', '77.01937', 'India', 'IN', 'Haryana'),
(191, 'Srinagar', '34.08565', '74.80555', 'India', 'IN', 'Jammu and Kashmir'),
(192, 'Surat', '21.19594', '72.83023', 'India', 'IN', 'Gujarat'),
(193, 'Tezpur', '26.63333', '92.8', 'India', 'IN', 'Assam'),
(194, 'Thanjavur', '10.78523', '79.13909', 'India', 'IN', 'Tamil Nadu '),
(195, 'Tharati Etawah', '26.75823', '79.01487', 'India', 'IN', 'Uttar Pradesh'),
(196, 'Thiruvananthapuram', '8.485498', '76.94923', 'India', 'IN', 'Kerala'),
(197, 'Tiruchchirappalli', '10.81549', '78.69651', 'India', 'IN', 'Tamil Nadu '),
(198, 'Tirunelveli', '8.725181', '77.68451', 'India', 'IN', 'Tamil Nadu '),
(199, 'Tirupati', '13.63550', '79.41988', 'India', 'IN', 'Andhra Pradesh'),
(200, 'Tiruvannamalai', '12.23020', '79.07295', 'India', 'IN', 'Tamil Nadu '),
(201, 'Tonk', '26.16867', '75.78611', 'India', 'IN', 'Rajasthan'),
(202, 'Tuticorin', '8.805038', '78.15188', 'India', 'IN', 'Tamil Nadu '),
(203, 'Udaipur', '24.57951', '73.69050', 'India', 'IN', 'Rajasthan'),
(204, 'Ujjain', '23.18238', '75.77643', 'India', 'IN', 'Madhya Pradesh'),
(205, 'Vadodara', '22.29940', '73.20811', 'India', 'IN', 'Gujarat'),
(206, 'Valparai', '10.32516', '76.95529', 'India', 'IN', 'Tamil Nadu '),
(207, 'Varanasi', '25.31774', '83.00581', 'India', 'IN', 'Uttar Pradesh'),
(208, 'Vellore', '12.90576', '79.13710', 'India', 'IN', 'Tamil Nadu '),
(209, 'Vishakhapatnam', '17.70405', '83.29766', 'India', 'IN', 'Andhra Pradesh'),
(210, 'Vizianagaram', '18.11329', '83.39774', 'India', 'IN', 'Andhra Pradesh'),
(211, 'Warangal', '17.97842', '79.60020', 'India', 'IN', 'Telangana'),
(212, 'Jorapokhar', '23.7', '86.41267', 'India', 'IN', 'Jharkhand'),
(213, 'Brajrajnagar', '21.82', '83.92', 'India', 'IN', 'Odisha'),
(214, 'Talcher', '20.95', '85.23', 'India', 'IN', 'Odisha'),
(232, 'Nelmangala', '13.0973', '77.3856', 'India', 'IN', 'Karnataka');

-- --------------------------------------------------------

--
-- Table structure for table `luggage`
--

CREATE TABLE `luggage` (
  `luggage_id` int(11) NOT NULL,
  `from_branch` varchar(40) NOT NULL,
  `to_branch` varchar(40) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `send_date` varchar(30) NOT NULL,
  `present_hub` varchar(40) NOT NULL,
  `receive_date` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `luggage`
--

INSERT INTO `luggage` (`luggage_id`, `from_branch`, `to_branch`, `status`, `created_at`, `send_date`, `present_hub`, `receive_date`) VALUES
(1, 'Tiruchchirappalli', 'Chennai', 'open', '2023-10-08 04:06:21', '', 'Tiruchirappalli', ''),
(2, 'Tiruchchirappalli', 'Chennai', 'closed', '2023-10-08 04:06:21', '', 'Tiruchirappalli', '');

-- --------------------------------------------------------

--
-- Table structure for table `parcel`
--

CREATE TABLE `parcel` (
  `parcel_id` int(10) NOT NULL,
  `luggage_id` int(10) NOT NULL,
  `serviceman_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `from_branch` varchar(40) NOT NULL,
  `to_branch` varchar(40) NOT NULL,
  `pay_amount` varchar(40) NOT NULL,
  `present_hub` varchar(20) NOT NULL,
  `received_date` varchar(20) DEFAULT NULL,
  `sentotp` varchar(225) NOT NULL,
  `courier_image` varchar(40) DEFAULT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'open',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `parcel`
--

INSERT INTO `parcel` (`parcel_id`, `luggage_id`, `serviceman_id`, `user_id`, `from_branch`, `to_branch`, `pay_amount`, `present_hub`, `received_date`, `sentotp`, `courier_image`, `status`, `created_at`) VALUES
(1, 1, 1, 1, '1', '1', '2', '1', NULL, 'e88f243bf341ded9b4ced444795c3f17', NULL, 'open', '2023-10-08 08:09:14'),
(2, 1, 1, 1, '1', '1', '1', '1', NULL, 'a6155b0da06d1ad154ad2d039d1fadf4', NULL, 'open', '2023-10-08 11:06:44'),
(3, 1, 1, 1, '1', '1', '2', '1', NULL, '3a24b25a7b092a252166a1641ae953e7', NULL, 'open', '2023-10-08 11:06:49'),
(4, 1, 1, 5, '1', '1', '2', '1', '2023-10-08 13:39:14', 'cdf6581cb7aca4b7e19ef136c6e601a5', NULL, 'delivered', '2023-12-02 11:54:09'),
(5, 1, 1, 5, '1', '2', '1', '2', '2023-10-08 13:39:14', '21e4ef94f2a6b23597efabaec584b504', NULL, 'returned', '2023-12-02 11:54:13');

-- --------------------------------------------------------

--
-- Table structure for table `service_man`
--

CREATE TABLE `service_man` (
  `serviceman_id` int(10) NOT NULL,
  `serviceman_name` varchar(40) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `otp` int(5) NOT NULL,
  `verified` int(10) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_man`
--

INSERT INTO `service_man` (`serviceman_id`, `serviceman_name`, `phone`, `email`, `address`, `password`, `otp`, `verified`, `created_at`) VALUES
(1, 'Sahas', '6381268719', 'thirstolearn@gmail.com', 's', '12', 7426, 1, '2023-12-01 20:30:56');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `user_id` int(5) NOT NULL,
  `user_name` varchar(40) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `otp` int(5) DEFAULT NULL,
  `verified` int(2) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `phone`, `email`, `address`, `password`, `otp`, `verified`, `created_at`) VALUES
(1, 'Prithiviraj', '6381268719', 'thirstolearn@gmail.com', 'Chennai', 'AdminPass', 5752, 0, '2023-12-01 19:48:04'),
(2, 'Ricky', '9876543210', 'thirstolearn@gmail.com', 'Delhi', '12345', 6392, 0, '2023-12-01 20:18:30'),
(3, 'Prithiviraj', '6381268719', 'thirstolearn@gmail.com', 's', '12', 4725, 0, '2023-12-01 20:20:59'),
(4, 'Prithiviraj', '6381268719', 'thirstolearn@gmail.com', 'PKT', '12345', 7274, 0, '2023-12-01 20:22:11'),
(5, 'Prithiviraj', '6381268719', 'thirstolearn@gmail.com', 'PKT', '12345', 6875, 1, '2023-12-01 20:24:57'),
(6, 'Prithiviraj', '6381268718', 'thirstolearn@gmail.com', 's', '12', 1195, 0, '2023-12-01 20:28:04'),
(7, 'Prithiviraj', '6381268718', 'thirstolearn@gmail.com', 's', '12', 2176, 0, '2023-12-01 20:28:14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `branch_details`
--
ALTER TABLE `branch_details`
  ADD PRIMARY KEY (`branch_id`);

--
-- Indexes for table `cust_query`
--
ALTER TABLE `cust_query`
  ADD PRIMARY KEY (`query_id`);

--
-- Indexes for table `goods_receiving`
--
ALTER TABLE `goods_receiving`
  ADD PRIMARY KEY (`gr_id`);

--
-- Indexes for table `indian_cities_database`
--
ALTER TABLE `indian_cities_database`
  ADD PRIMARY KEY (`cityid`);

--
-- Indexes for table `luggage`
--
ALTER TABLE `luggage`
  ADD PRIMARY KEY (`luggage_id`);

--
-- Indexes for table `parcel`
--
ALTER TABLE `parcel`
  ADD PRIMARY KEY (`parcel_id`);

--
-- Indexes for table `service_man`
--
ALTER TABLE `service_man`
  ADD PRIMARY KEY (`serviceman_id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `branch_details`
--
ALTER TABLE `branch_details`
  MODIFY `branch_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cust_query`
--
ALTER TABLE `cust_query`
  MODIFY `query_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `goods_receiving`
--
ALTER TABLE `goods_receiving`
  MODIFY `gr_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `indian_cities_database`
--
ALTER TABLE `indian_cities_database`
  MODIFY `cityid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=234;

--
-- AUTO_INCREMENT for table `luggage`
--
ALTER TABLE `luggage`
  MODIFY `luggage_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `parcel`
--
ALTER TABLE `parcel`
  MODIFY `parcel_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `service_man`
--
ALTER TABLE `service_man`
  MODIFY `serviceman_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `user_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
