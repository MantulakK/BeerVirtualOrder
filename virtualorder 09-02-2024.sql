-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-02-2024 a las 15:35:46
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `virtualorder`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articles`
--

CREATE TABLE `articles` (
  `id_article` int(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `article_type` int(6) NOT NULL,
  `single_price` varchar(255) NOT NULL,
  `url` text CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `articles`
--

INSERT INTO `articles` (`id_article`, `name`, `brand`, `description`, `article_type`, `single_price`, `url`) VALUES
(15, 'Brahma', 'AmBev', 'Brahma Schop con espuma', 2, '1500', 'http://localhost:5000/static/img/h7.jpg'),
(16, 'Pulled Pork', 'Burger', 'Cerdo ahumado desmechado, coleslaw, pepinillos, salsa BBQ', 1, '3000', 'http://localhost:5000/static/img/h1.jpg'),
(17, 'Test', 'MarcaTest', 'DescTest', 2, '1', 'http://localhost:5000/static/img/h7.jpg'),
(18, 'Vegetariana', 'Burger', 'Rúcula, medallón veggie, mozzarella, tomate, orégano, zucchini en conserva', 1, '2300', 'http://localhost:5000/static/img/h3.jpg'),
(19, 'Corona', ' Anheuser-Busch InBev', 'Cerveza Corona', 2, '2500', 'http://localhost:5000/static/img/h9.jpg'),
(20, 'Cheese Bacon', 'Burger', 'Pepinillo, panceta, queso cheddar, doble blend ternera 160gr', 1, '3050', 'http://localhost:5000/static/img/papas.jpg'),
(21, 'asd', 'dsa', 'qwerty', 1, '1', 'http://localhost:5000/static/img/h1.jpg'),
(22, 'Cheese', 'Burger', 'Queso cheddar, ketchup, blend ternera 160gr', 1, '2200', ''),
(23, 'Mandioca Frita', 'Mandioca Frita', 'Mandioca Frita', 1, '1500', ''),
(24, 'Papas Almacén', 'Papas Almacén', 'Papas Almacén', 1, '3300', ''),
(25, 'Papas Rústicas', 'Papas Rústicas', 'Papas Rústicas', 1, '1560', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `order`
--

CREATE TABLE `order` (
  `id_order` int(100) NOT NULL,
  `id_table` int(100) NOT NULL,
  `order_state` varchar(100) NOT NULL,
  `total_price` int(100) NOT NULL,
  `order_datetime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `order`
--

INSERT INTO `order` (`id_order`, `id_table`, `order_state`, `total_price`, `order_datetime`) VALUES
(7, 8, 'CERRADO', 17053, '2024-02-02 09:18:59'),
(8, 10, 'CERRADO', 10500, '2024-02-02 11:30:21'),
(9, 8, 'CERRADO', 20600, '2024-02-06 09:54:09'),
(10, 8, 'CERRADO', 21260, '2024-02-07 13:24:07'),
(11, 8, 'CERRADO', 1500, '2024-02-08 08:37:43'),
(12, 8, 'ABIERTO', 0, '2024-02-09 11:02:31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `order_det`
--

CREATE TABLE `order_det` (
  `id_detail` int(100) NOT NULL,
  `id_order` int(100) NOT NULL,
  `id_article` int(100) NOT NULL,
  `amount` int(100) NOT NULL,
  `detail_state` int(10) NOT NULL,
  `order_price` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `order_det`
--

INSERT INTO `order_det` (`id_detail`, `id_order`, `id_article`, `amount`, `detail_state`, `order_price`) VALUES
(3, 7, 16, 1, 1, 3000),
(4, 7, 20, 1, 1, 3050),
(5, 7, 15, 2, 1, 3000),
(6, 7, 19, 2, 1, 5000),
(7, 7, 15, 2, 1, 3000),
(8, 7, 17, 3, 1, 3),
(9, 8, 15, 5, 1, 7500),
(10, 8, 16, 1, 1, 3000),
(11, 9, 16, 1, 1, 3000),
(12, 9, 19, 1, 1, 2500),
(13, 9, 15, 2, 1, 3000),
(14, 9, 22, 1, 1, 2200),
(17, 9, 24, 3, 1, 9900),
(22, 10, 15, 2, 1, 3000),
(23, 10, 19, 3, 1, 7500),
(25, 10, 18, 3, 1, 6900),
(27, 10, 18, 1, 1, 2300),
(29, 10, 25, 1, 1, 1560),
(30, 11, 15, 1, 1, 1500),
(32, 12, 16, 1, 0, 3000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `qr`
--

CREATE TABLE `qr` (
  `id_qr` int(100) NOT NULL,
  `qr_code` varchar(255) NOT NULL,
  `id_table` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `qrtable`
--

CREATE TABLE `qrtable` (
  `id_table` int(100) NOT NULL,
  `table_num` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `qrtable`
--

INSERT INTO `qrtable` (`id_table`, `table_num`) VALUES
(8, '001'),
(9, '002'),
(10, '003');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id_article`);

--
-- Indices de la tabla `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id_order`);

--
-- Indices de la tabla `order_det`
--
ALTER TABLE `order_det`
  ADD PRIMARY KEY (`id_detail`);

--
-- Indices de la tabla `qr`
--
ALTER TABLE `qr`
  ADD PRIMARY KEY (`id_qr`);

--
-- Indices de la tabla `qrtable`
--
ALTER TABLE `qrtable`
  ADD PRIMARY KEY (`id_table`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articles`
--
ALTER TABLE `articles`
  MODIFY `id_article` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `order`
--
ALTER TABLE `order`
  MODIFY `id_order` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `order_det`
--
ALTER TABLE `order_det`
  MODIFY `id_detail` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `qr`
--
ALTER TABLE `qr`
  MODIFY `id_qr` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `qrtable`
--
ALTER TABLE `qrtable`
  MODIFY `id_table` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
