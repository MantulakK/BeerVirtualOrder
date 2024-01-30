-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-01-2024 a las 00:15:50
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

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
  `single_price` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `articles`
--

INSERT INTO `articles` (`id_article`, `name`, `brand`, `description`, `article_type`, `single_price`) VALUES
(15, 'Brahma', 'AmBev', 'Brahma Schop con espuma', 2, '1500'),
(16, 'Pulled Pork', 'Burguer', 'Cerdo ahumado desmechado, coleslaw, pepinillos, salsa BBQ', 1, '3000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mainorder`
--

CREATE TABLE `mainorder` (
  `id_orderdet` int(100) NOT NULL,
  `id_table` int(100) NOT NULL,
  `id_staff` int(100) NOT NULL,
  `order_num` varchar(255) NOT NULL,
  `iva` varchar(255) NOT NULL,
  `total` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `order_det`
--

CREATE TABLE `order_det` (
  `id_orderdet` int(100) NOT NULL,
  `items` varchar(255) NOT NULL,
  `order_price` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `qrtable`
--

CREATE TABLE `qrtable` (
  `id_table` int(100) NOT NULL,
  `table_num` varchar(255) NOT NULL,
  `available` tinyint(1) NOT NULL,
  `qr` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `qrtable`
--

INSERT INTO `qrtable` (`id_table`, `table_num`, `available`, `qr`) VALUES
(1, '1', 1, 0),
(2, '2', 1, 1),
(3, '3', 1, 121564),
(4, '4', 1, 345151),
(5, '5', 1, 2145151),
(6, '6', 1, 451),
(7, '7', 0, 123456);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `staff`
--

CREATE TABLE `staff` (
  `id_staff` int(100) NOT NULL,
  `buss_name` varchar(255) NOT NULL,
  `cel_num` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `staff`
--

INSERT INTO `staff` (`id_staff`, `buss_name`, `cel_num`) VALUES
(1, 'Rodrigo Mathias', '+543755456923'),
(2, 'Mantulak Kevin', '+543755297187'),
(3, 'Lindeborg Gabriela', '+543755265132');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id_article`);

--
-- Indices de la tabla `mainorder`
--
ALTER TABLE `mainorder`
  ADD PRIMARY KEY (`id_orderdet`);

--
-- Indices de la tabla `order_det`
--
ALTER TABLE `order_det`
  ADD PRIMARY KEY (`id_orderdet`);

--
-- Indices de la tabla `qrtable`
--
ALTER TABLE `qrtable`
  ADD PRIMARY KEY (`id_table`);

--
-- Indices de la tabla `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id_staff`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articles`
--
ALTER TABLE `articles`
  MODIFY `id_article` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `order_det`
--
ALTER TABLE `order_det`
  MODIFY `id_orderdet` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `qrtable`
--
ALTER TABLE `qrtable`
  MODIFY `id_table` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `staff`
--
ALTER TABLE `staff`
  MODIFY `id_staff` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
