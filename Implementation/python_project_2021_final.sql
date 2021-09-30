-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Φιλοξενητής: 127.0.0.1
-- Χρόνος δημιουργίας: 12 Ιουν 2021 στις 19:50:01
-- Έκδοση διακομιστή: 10.4.17-MariaDB
-- Έκδοση PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `python_project_2021`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `arrivals`
--

CREATE TABLE `arrivals` (
  `id` int(11) NOT NULL COMMENT 'ID',
  `country` varchar(50) NOT NULL COMMENT 'Country',
  `year` year(4) NOT NULL COMMENT 'Year',
  `arrivals` int(11) NOT NULL COMMENT 'Arrivals of residents at tourist accommodation establishments'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `arrivals`
--

INSERT INTO `arrivals` (`id`, `country`, `year`, `arrivals`) VALUES
(1, 'Greece', 2016, 8080042),
(2, 'Greece', 2017, 8142571),
(3, 'Greece', 2018, 9264746),
(4, 'Greece', 2019, 9163555),
(5, 'Sweden', 2016, 22524467),
(6, 'Sweden', 2017, 23033004),
(7, 'Sweden', 2018, 23519609),
(8, 'Sweden', 2019, 24490475);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `arrivals_non_residents`
--

CREATE TABLE `arrivals_non_residents` (
  `id` int(11) NOT NULL COMMENT 'ID',
  `country` varchar(11) NOT NULL COMMENT 'Country',
  `year` year(4) NOT NULL COMMENT 'Year',
  `arrivals` int(11) NOT NULL COMMENT 'Arrivals of non-residents at tourist accommodation establishments'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `arrivals_non_residents`
--

INSERT INTO `arrivals_non_residents` (`id`, `country`, `year`, `arrivals`) VALUES
(1, 'Greece', 2016, 16915996),
(2, 'Greece', 2017, 19068697),
(3, 'Greece', 2018, 24320893),
(4, 'Greece', 2019, 25038498),
(5, 'Sweden', 2016, 6550337),
(6, 'Sweden', 2017, 6840963),
(7, 'Sweden', 2018, 7217241),
(8, 'Sweden', 2019, 7407227);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `nights_spent`
--

CREATE TABLE `nights_spent` (
  `id` int(11) NOT NULL COMMENT 'ID',
  `country` varchar(50) NOT NULL COMMENT 'Country',
  `year` year(4) NOT NULL COMMENT 'Year',
  `nights_spent` int(11) NOT NULL COMMENT 'Nights spent at tourist accommodation establishments by residents'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `nights_spent`
--

INSERT INTO `nights_spent` (`id`, `country`, `year`, `nights_spent`) VALUES
(1, 'Greece', 2016, 22107192),
(2, 'Greece', 2017, 21974593),
(3, 'Greece', 2018, 24064088),
(4, 'Greece', 2019, 23623077),
(5, 'Sweden', 2016, 43236883),
(6, 'Sweden', 2017, 44044499),
(7, 'Sweden', 2018, 45171193),
(8, 'Sweden', 2019, 47195047);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `nights_spent_non_residents`
--

CREATE TABLE `nights_spent_non_residents` (
  `id` int(11) NOT NULL COMMENT 'ID',
  `country` varchar(50) NOT NULL COMMENT 'Country',
  `year` year(4) NOT NULL COMMENT 'Year',
  `nights_spent` int(11) NOT NULL COMMENT 'Nights spent at tourist accommodation establishments by non residents'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `nights_spent_non_residents`
--

INSERT INTO `nights_spent_non_residents` (`id`, `country`, `year`, `nights_spent`) VALUES
(1, 'Greece', 2016, 87912850),
(2, 'Greece', 2017, 97034421),
(3, 'Greece', 2018, 118876323),
(4, 'Greece', 2019, 119971390),
(5, 'Sweden', 2016, 13997265),
(6, 'Sweden', 2017, 14638702),
(7, 'Sweden', 2018, 15685681),
(8, 'Sweden', 2019, 15980234);

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `arrivals`
--
ALTER TABLE `arrivals`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `arrivals_non_residents`
--
ALTER TABLE `arrivals_non_residents`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Ευρετήρια για πίνακα `nights_spent`
--
ALTER TABLE `nights_spent`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `nights_spent_non_residents`
--
ALTER TABLE `nights_spent_non_residents`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `arrivals`
--
ALTER TABLE `arrivals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID', AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT για πίνακα `arrivals_non_residents`
--
ALTER TABLE `arrivals_non_residents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID', AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT για πίνακα `nights_spent`
--
ALTER TABLE `nights_spent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID', AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT για πίνακα `nights_spent_non_residents`
--
ALTER TABLE `nights_spent_non_residents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID', AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
