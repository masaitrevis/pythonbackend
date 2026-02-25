-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 12:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `simba-sokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(50) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_description` mediumtext NOT NULL,
  `product_cost` int(50) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `photo`) VALUES
(1, 'iphone', 'high end phone', 100000, 'iphone.webp'),
(2, 'Samsung galaxy S25 ultra', 'Flagship Android with top-tier performance', 122000, 'samsunggalaxys25.webp'),
(3, 'Google pixel 10', 'Android flagship with a 6.8-inch display, Google Tensor G5 chip, and advanced AI photo editing tools.', 122000, 'googlepixel10a.avif'),
(4, 'One plus', ' High-performance flagship known for fast charging, AI features, and exceptional battery life.', 94000, 'oneplus.avif'),
(5, 'Xiaomi', 'Features premium camera hardware for high-end photography.', 110000, 'xiaomi.avif'),
(6, 'CMF phone', 'A stylish budget phone offering high value for money.', 150000, 'cmf.webp'),
(7, 'Google Pixel 10a', ' A mid-range, cost-effective alternative to the Pixel 10 with AI features.\n', 130000, 'googlepixel10a.avif'),
(8, 'Tecno phantom', ' A premium, foldable device featuring AI integration.', 143000, 'tecnophantom.avif'),
(9, 'Realme C67', ' A budget-friendly, entry-level smartphone focused on battery and daily usage.', 156000, 'Realme.webp'),
(10, 'Vivo V70 ELITE', 'Mid-range smartphone focusing on high-quality imaging and performance.', 133000, 'vivo v70.jpg'),
(11, 'Motorola Razr Ultra', 'A top-tier flip-style foldable phone.', 88000, 'motorolla.avif'),
(12, 'Infinix Note 60 Pro 5G', 'A competitive, high-performance mid-range device in emerging markets.', 97500, 'infinite.jpg'),
(13, 'Nothing phone', 'A mid-range phone with a unique, transparent design and clean software.', 99000, 'nothing.webp'),
(14, 'Samsung S26 ultra', 'this flagship is rumored to feature a new \"Privacy Display\" that hides specific on-screen notifications from bystanders and is powered by the Snapdragon 8 Gen 5.', 125000, 'samsung26ultra.jpg'),
(15, 'Apple iphone 17 air', 'A revolutionary \"ultra-slim\" model measuring only 5.6mm thin. It features a titanium frame, the A19 Pro chip, and a 6.6-inch ProMotion display.', 250000, 'Apple17.jpg'),
(16, 'VIVO VX 300', 'Anticipated as a mobile photography powerhouse, it is expected to be the first to feature two 200MP sensors—one for the main camera and another for a periscope telephoto lens.', 70000, 'vivo vx300.jpg'),
(17, 'Samsung Galaxy Z Trifold', 'A futuristic device that folds twice to expand into a mini-tablet. It was unveiled in late 2025 and launched in early 2026 with a large 7.6-inch OLED inner screen. ', 300000, 'trifold.jpg'),
(18, 'Tecno Spark 40', 'A popular entry-level model in emerging markets, offering 5G connectivity and a high-refresh-rate display at a very competitive price point. \nPhone Place Kenya\nPhone Place Kenya\n +8', 42000, 'spark.webp'),
(19, 'One Plus 13R', 'A \"flagship killer\" that packs near-premium specs, including the Snapdragon 8 Elite chipset and a massive 6,000mAh battery, into a more affordable frame.\n', 25700, 'oneplus13r.jpg'),
(20, 'Xiaomi Redmi 15C 4G', ' A budget-friendly choice featuring a large 50MP rear camera and reliable daily performance for cost-conscious buyers.', 12500, 'xredmi.webp');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(50) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` int(50) NOT NULL,
  `phone` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `password`, `phone`) VALUES
(1, 'trevis', 'masatrevis@gmail.com', 1234768654, 745673656),
(2, 'mdt', 'ma@gmail.com', 25467, 745673565);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

