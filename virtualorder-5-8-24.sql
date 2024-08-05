-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-08-2024 a las 00:30:44
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

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
-- Estructura de tabla para la tabla `articulos`
--

CREATE TABLE `articulos` (
  `CARTICULO` int(100) NOT NULL,
  `NOMBRE` varchar(255) NOT NULL,
  `DESCRIPCION` varchar(255) NOT NULL,
  `CMARCA` varchar(255) NOT NULL,
  `CRUBRO` int(6) NOT NULL,
  `CTIPO` int(6) NOT NULL,
  `VIGENTE` int(11) NOT NULL DEFAULT 1,
  `PRECIO_UNIT` varchar(255) NOT NULL,
  `IMG_PATH` text CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `FALTA` varchar(50) NOT NULL,
  `FMODI` varchar(50) NOT NULL,
  `FH_AJUSTE` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `articulos`
--

INSERT INTO `articulos` (`CARTICULO`, `NOMBRE`, `DESCRIPCION`, `CMARCA`, `CRUBRO`, `CTIPO`, `VIGENTE`, `PRECIO_UNIT`, `IMG_PATH`, `FALTA`, `FMODI`, `FH_AJUSTE`) VALUES
(0, 'VARIOS', 'VARIOS', '1', 1, 2, 1, '100', 'NULL', '', '2024-08-05 17:43:29.022247', ''),
(15, 'Cerveza Brahma', 'Cerveza Brahma', '1', 3, 1, 1, '1948', 'static/img/articles\\15.jpg', '', '', ''),
(16, 'Pulled Pork', 'Burger', '1', 7, 1, 1, '3000', 'static/img/articles\\16.jpg', '', '', ''),
(17, 'Cerveza Quilmes', 'Quilmes', '1', 3, 1, 1, '1600', 'static/img/articles\\17.jpg', '', '', ''),
(18, 'Vegetariana', 'Burger', '1', 7, 1, 1, '2300', 'static/img/articles\\18.jpg', '', '', ''),
(19, 'Cardiff ', ' Anheuser-Busch InBev', '1', 3, 1, 1, '2600', 'static/img/articles\\19.jpg', '', '', ''),
(20, 'Cheese Bacon', 'Burger', '1', 7, 1, 1, '3050', 'static/img/articles\\20.jpg', '', '', ''),
(21, 'Rucula', 'Hamburguesa ', '1', 7, 1, 1, '2600', 'static/img/articles\\21.jpg', '', '', ''),
(22, 'Cheese', 'Burger', '1', 7, 1, 1, '2200', 'static/img/articles\\22.jpg', '', '', ''),
(23, 'Papas Rusticas', 'Papas', '1', 9, 1, 1, '1800', 'static/img/articles\\23.jpg', '', '', ''),
(24, 'Alistas de Pollo', 'Alistas de Pollo', '1', 9, 1, 1, '2300', 'static/img/articles\\24.jpg', '', '', ''),
(25, 'Empanadas', 'Empanadas', '1', 8, 1, 1, '800', 'static/img/articles\\25.jpg', '', '', ''),
(26, 'Pizzas', 'Pizzas', '1', 8, 1, 1, '2100', 'static/img/articles\\26.jpg', '', '', ''),
(27, 'Carne a la chapa', 'Carne a la chapa', '1', 7, 1, 1, '2100', 'static/img/articles\\27.jpg', '', '', ''),
(28, 'Cerveza Mar del Plata', 'Mar del plata', '1', 3, 1, 1, '2100', 'static/img/articles\\28.jpg', '', '', ''),
(29, 'Cerveza Blest', 'Cerveza Blest', '1', 3, 1, 1, '2100', 'static/img/articles\\29.jpg', '', '', ''),
(30, 'Cerveza Kunstmann', 'Cerveza Kunstmann', '1', 3, 1, 1, '2100', 'static/img/articles\\30.jpg', '', '', ''),
(31, 'Gaseosa Coca Cola', 'Coca Cola', '1', 2, 1, 1, '2200', 'static/img/articles\\31.jpg', '', '', '2024-08-05 17:51:54.468019'),
(32, 'Gaseosa Sprite', 'Sprite', '1', 2, 1, 1, '2200', 'static/img/articles\\32.jpg', '', '', '2024-08-05 17:51:54.468019'),
(33, 'Energizante Speed', 'Speed', '1', 2, 1, 0, '2200', 'speed.jpg', '', '', '2024-08-05 17:51:54.468019'),
(34, 'Cerveza Budweiser', 'Budweiser', '1', 3, 1, 1, '2100', 'static/img/articles\\34.jpg', '', '', ''),
(35, 'Pulled Pork x2  + Papas Cheddar x1 + Cerveza Brahma x2 ', 'Combo', '1', 1, 2, 1, '18199', '', '', '', ''),
(37, 'var', 'var', '1', 1, 1, 0, '1', 'static/img/articles\\var.png', '', '', ''),
(38, 'imgtest', 'imgtest', '1', 1, 1, 0, '1', 'static/img/articles\\38.png', '', '', ''),
(39, 'testimg2', 'testimg2', '1', 3, 1, 0, '10000', 'static/img/articles\\39.jpg', '', '', ''),
(40, 'testimg3', 'testimg3', '1', 3, 1, 0, '10000', 'static/img/articles\\40.jpg', '', '', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `codigos_qr`
--

CREATE TABLE `codigos_qr` (
  `CQR` int(100) NOT NULL,
  `CODIGO_QR` varchar(255) NOT NULL,
  `CMESA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `codigos_qr`
--

INSERT INTO `codigos_qr` (`CQR`, `CODIGO_QR`, `CMESA`) VALUES
(11, 'static\\qr_mesa_1.png', 8),
(12, 'static/qrcodes/qr_mesa_2.png', 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_empresa`
--

CREATE TABLE `datos_empresa` (
  `CDATOS` int(11) NOT NULL,
  `RAZ_SOCIAL` varchar(50) DEFAULT NULL,
  `NOMBRE_FANTASIA` varchar(50) DEFAULT NULL,
  `CUIT` int(12) DEFAULT NULL,
  `TITULAR` varchar(50) DEFAULT NULL,
  `EMAIL` varchar(50) DEFAULT NULL,
  `LOCALIDAD` varchar(50) NOT NULL,
  `LOGO_PATH` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `datos_empresa`
--

INSERT INTO `datos_empresa` (`CDATOS`, `RAZ_SOCIAL`, `NOMBRE_FANTASIA`, `CUIT`, `TITULAR`, `EMAIL`, `LOCALIDAD`, `LOGO_PATH`) VALUES
(1, 'B&R VIRTUAL ORDER', 'B&R VIRTUAL ORDER', 123456789, 'KEVIN IVAN MANTULAK', 'b&rvirtualorder@gmail.com', 'OBERÁ MISIONES ARGENTINA', 'static/img/system/logo_empresa.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marcas`
--

CREATE TABLE `marcas` (
  `CMARCA` int(11) NOT NULL,
  `DESCRIPCION` varchar(100) NOT NULL,
  `VIGENTE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marcas`
--

INSERT INTO `marcas` (`CMARCA`, `DESCRIPCION`, `VIGENTE`) VALUES
(1, 'GENERAL', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `CMODULO` int(6) NOT NULL,
  `MODULO` varchar(30) NOT NULL,
  `VIGENTE` int(6) NOT NULL,
  `FMODI` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modulos`
--

INSERT INTO `modulos` (`CMODULO`, `MODULO`, `VIGENTE`, `FMODI`) VALUES
(1, 'PLATOS PRINCIPALES', 1, NULL),
(2, 'ENTRADAS', 0, NULL),
(3, 'GUARNICIONES', 1, NULL),
(4, 'POSTRES', 0, NULL),
(5, 'BEBIDAS', 1, NULL),
(6, 'COMBOS', 1, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenes`
--

CREATE TABLE `ordenes` (
  `CORDEN` int(100) NOT NULL,
  `CMESA` int(100) NOT NULL,
  `ESTADO_ORDEN` int(6) NOT NULL,
  `PROPINAS` int(100) NOT NULL DEFAULT 0,
  `PRECIO_TOTAL` int(100) NOT NULL,
  `FECHA_HORA` varchar(100) NOT NULL,
  `GENERADO_POR` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ordenes`
--

INSERT INTO `ordenes` (`CORDEN`, `CMESA`, `ESTADO_ORDEN`, `PROPINAS`, `PRECIO_TOTAL`, `FECHA_HORA`, `GENERADO_POR`) VALUES
(7, 8, 0, 0, 17053, '2024-02-02 09:18:59', 0),
(8, 10, 0, 0, 10500, '2024-02-02 11:30:21', 0),
(9, 8, 0, 0, 20600, '2024-02-06 09:54:09', 0),
(10, 8, 0, 0, 21260, '2024-02-07 13:24:07', 0),
(11, 8, 0, 0, 1500, '2024-02-08 08:37:43', 0),
(12, 8, 0, 0, 7500, '2024-02-09 11:02:31', 0),
(13, 8, 0, 0, 5300, '2024-02-15 17:49:30', 0),
(14, 8, 0, 0, 9500, '2024-02-15 17:53:39', 0),
(15, 9, 0, 0, 4550, '2024-02-16 10:34:09', 0),
(16, 8, 0, 0, 7500, '2024-02-16 10:55:30', 0),
(18, 8, 0, 0, 1500, '2024-02-22 10:41:20', 0),
(19, 9, 0, 1000, 4680, '2024-02-24 13:15:18', 0),
(20, 8, 0, 500, 12400, '2024-02-24 13:29:02', 0),
(21, 10, 0, 500, 4500, '2024-02-24 13:37:10', 0),
(22, 9, 0, 0, 4400, '2024-02-24 16:01:38', 0),
(23, 11, 0, 1000, 8000, '2024-02-29 10:30:01', 0),
(24, 8, 0, 1500, 2300, '2024-03-06 09:09:29', 0),
(25, 9, 0, 0, 15000, '2024-03-06 10:15:33', 0),
(27, 8, 2, 0, 0, '2024-03-13 10:40:24', 0),
(28, 8, 0, 1000, 10000, '2024-03-13 11:14:18', 0),
(29, 8, 0, 1500, 4200, '2024-03-14 09:29:45', 0),
(30, 8, 0, 100, 7960, '2024-03-15 08:11:52', 0),
(31, 8, 2, 0, 0, '2024-03-15 08:31:32', 0),
(32, 8, 2, 0, 0, '2024-03-15 08:33:26', 0),
(33, 8, 0, 0, 13680, '2024-03-15 09:01:19', 0),
(34, 8, 0, 0, 12360, '2024-03-15 09:08:41', 0),
(35, 8, 0, 1000, 9000, '2024-03-15 10:21:59', 0),
(36, 8, 0, 100, 5748, '2024-03-26 10:21:41', 0),
(37, 8, 2, 0, 0, '2024-03-26 11:27:41', 0),
(38, 8, 0, 0, 11848, '2024-08-02 15:46:52', 1),
(39, 9, 1, 0, 0, '2024-08-02 15:54:11', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenes_det`
--

CREATE TABLE `ordenes_det` (
  `CDETALLE_ORDEN` int(100) NOT NULL,
  `CORDEN` int(100) NOT NULL,
  `CARTICULO` int(100) NOT NULL,
  `CANTIDAD` int(100) NOT NULL,
  `ESTADO_DETALLE` int(10) NOT NULL,
  `PRECIO_ORDEN` int(100) NOT NULL,
  `GENERADO_POR` int(6) NOT NULL,
  `ENTREGADO` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ordenes_det`
--

INSERT INTO `ordenes_det` (`CDETALLE_ORDEN`, `CORDEN`, `CARTICULO`, `CANTIDAD`, `ESTADO_DETALLE`, `PRECIO_ORDEN`, `GENERADO_POR`, `ENTREGADO`) VALUES
(3, 7, 16, 1, 1, 3000, 0, 0),
(4, 7, 20, 1, 1, 3050, 0, 0),
(5, 7, 15, 2, 1, 3000, 0, 0),
(6, 7, 19, 2, 1, 5000, 0, 0),
(7, 7, 15, 2, 1, 3000, 0, 0),
(8, 7, 17, 3, 1, 3, 0, 0),
(9, 8, 15, 5, 1, 7500, 0, 0),
(10, 8, 16, 1, 1, 3000, 0, 0),
(11, 9, 16, 1, 1, 3000, 0, 0),
(12, 9, 19, 1, 1, 2500, 0, 0),
(13, 9, 15, 2, 1, 3000, 0, 0),
(14, 9, 22, 1, 1, 2200, 0, 0),
(17, 9, 24, 3, 1, 9900, 0, 0),
(22, 10, 15, 2, 1, 3000, 0, 0),
(23, 10, 19, 3, 1, 7500, 0, 0),
(25, 10, 18, 3, 1, 6900, 0, 0),
(27, 10, 18, 1, 1, 2300, 0, 0),
(29, 10, 25, 1, 1, 1560, 0, 0),
(30, 11, 15, 1, 1, 1500, 0, 0),
(32, 12, 16, 1, 1, 3000, 0, 0),
(33, 12, 15, 1, 1, 1500, 0, 0),
(34, 12, 16, 1, 1, 3000, 0, 0),
(35, 13, 16, 1, 1, 3000, 0, 0),
(36, 13, 18, 1, 1, 2300, 0, 0),
(37, 14, 15, 1, 1, 1500, 0, 0),
(38, 14, 32, 2, 1, 4000, 0, 0),
(39, 14, 33, 2, 1, 4000, 0, 0),
(40, 16, 16, 1, 1, 3000, 0, 0),
(41, 16, 15, 1, 1, 1500, 0, 0),
(42, 16, 16, 1, 1, 3000, 0, 0),
(43, 18, 15, 1, 1, 1500, 0, 0),
(44, 15, 20, 1, 1, 3050, 0, 0),
(45, 15, 17, 1, 1, 1500, 0, 0),
(46, 19, 16, 1, 1, 3000, 0, 0),
(47, 19, 15, 1, 1, 1680, 0, 0),
(48, 20, 22, 2, 1, 4400, 0, 0),
(49, 20, 34, 4, 1, 8000, 0, 0),
(50, 21, 21, 1, 1, 2500, 0, 0),
(51, 21, 31, 1, 1, 2000, 0, 0),
(54, 22, 22, 2, 1, 4400, 0, 0),
(56, 23, 31, 1, 1, 2000, 0, 0),
(57, 23, 16, 2, 1, 6000, 0, 0),
(58, 24, 18, 1, 1, 2300, 0, 0),
(59, 25, 19, 6, 1, 15000, 0, 0),
(61, 28, 30, 5, 1, 10000, 0, 0),
(62, 29, 25, 6, 1, 4200, 0, 0),
(63, 30, 18, 2, 1, 4600, 0, 0),
(64, 30, 15, 2, 1, 3360, 0, 0),
(70, 33, 15, 1, 1, 1680, 0, 0),
(71, 33, 24, 6, 1, 12000, 0, 0),
(72, 34, 23, 2, 1, 3000, 0, 0),
(73, 34, 15, 2, 1, 3360, 0, 0),
(74, 34, 16, 2, 1, 6000, 0, 0),
(75, 35, 35, 1, 1, 9000, 0, 0),
(76, 36, 15, 1, 1, 1948, 0, 0),
(77, 36, 16, 1, 1, 3000, 0, 0),
(79, 36, 25, 1, 1, 800, 0, 0),
(82, 38, 15, 1, 1, 1948, 1, 1),
(83, 38, 16, 1, 1, 3000, 1, 1),
(84, 39, 20, 2, 1, 6100, 1, 1),
(85, 39, 31, 1, 1, 2100, 1, 1),
(86, 39, 17, 1, 1, 1600, 1, 1),
(87, 38, 18, 3, 1, 6900, 1, 0),
(88, 39, 15, 1, 1, 1948, 1, 1),
(89, 39, 17, 1, 1, 1600, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `qrmesas`
--

CREATE TABLE `qrmesas` (
  `CMESA` int(100) NOT NULL,
  `NUM_MESA` varchar(255) NOT NULL,
  `DESCRIPCION` varchar(100) DEFAULT NULL,
  `VIGENTE` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `qrmesas`
--

INSERT INTO `qrmesas` (`CMESA`, `NUM_MESA`, `DESCRIPCION`, `VIGENTE`) VALUES
(8, '1', '', 1),
(9, '2', '', 1),
(10, '3', '', 1),
(11, '4', '', 1),
(12, '5', '', 1),
(13, '7', '', 1),
(14, '15', '', 1),
(15, '16', '', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rubros`
--

CREATE TABLE `rubros` (
  `CRUBRO` int(11) NOT NULL,
  `NOMBRE_RUBRO` varchar(100) NOT NULL,
  `SUB_RUBRO` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rubros`
--

INSERT INTO `rubros` (`CRUBRO`, `NOMBRE_RUBRO`, `SUB_RUBRO`) VALUES
(1, 'GENERAL', 'GENERAL'),
(2, 'BEBIDAS', 'GASEOSAS'),
(3, 'BEBIDAS', 'CERVEZAS'),
(4, 'BEBIDAS', 'VINOS'),
(5, 'BEBIDAS', 'LICORES'),
(6, 'BEBIDAS', 'DESTILADOS'),
(7, 'COMIDAS', 'PLATOS PRINCIPALES'),
(8, 'COMIDAS', 'ENTRADAS'),
(9, 'COMIDAS', 'GUARNICIONES'),
(10, 'COMIDAS', 'POSTRES');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_articulos`
--

CREATE TABLE `tipos_articulos` (
  `CTIPO` int(6) NOT NULL,
  `TIPO` varchar(30) NOT NULL,
  `VIGENTE` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos_articulos`
--

INSERT INTO `tipos_articulos` (`CTIPO`, `TIPO`, `VIGENTE`) VALUES
(1, 'SIMPLE', 1),
(2, 'COMBO', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`CARTICULO`);

--
-- Indices de la tabla `codigos_qr`
--
ALTER TABLE `codigos_qr`
  ADD PRIMARY KEY (`CQR`);

--
-- Indices de la tabla `datos_empresa`
--
ALTER TABLE `datos_empresa`
  ADD PRIMARY KEY (`CDATOS`);

--
-- Indices de la tabla `marcas`
--
ALTER TABLE `marcas`
  ADD PRIMARY KEY (`CMARCA`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`CMODULO`);

--
-- Indices de la tabla `ordenes`
--
ALTER TABLE `ordenes`
  ADD PRIMARY KEY (`CORDEN`);

--
-- Indices de la tabla `ordenes_det`
--
ALTER TABLE `ordenes_det`
  ADD PRIMARY KEY (`CDETALLE_ORDEN`);

--
-- Indices de la tabla `qrmesas`
--
ALTER TABLE `qrmesas`
  ADD PRIMARY KEY (`CMESA`);

--
-- Indices de la tabla `rubros`
--
ALTER TABLE `rubros`
  ADD PRIMARY KEY (`CRUBRO`);

--
-- Indices de la tabla `tipos_articulos`
--
ALTER TABLE `tipos_articulos`
  ADD PRIMARY KEY (`CTIPO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articulos`
--
ALTER TABLE `articulos`
  MODIFY `CARTICULO` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `codigos_qr`
--
ALTER TABLE `codigos_qr`
  MODIFY `CQR` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `datos_empresa`
--
ALTER TABLE `datos_empresa`
  MODIFY `CDATOS` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `marcas`
--
ALTER TABLE `marcas`
  MODIFY `CMARCA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `CMODULO` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ordenes`
--
ALTER TABLE `ordenes`
  MODIFY `CORDEN` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT de la tabla `ordenes_det`
--
ALTER TABLE `ordenes_det`
  MODIFY `CDETALLE_ORDEN` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;

--
-- AUTO_INCREMENT de la tabla `qrmesas`
--
ALTER TABLE `qrmesas`
  MODIFY `CMESA` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `rubros`
--
ALTER TABLE `rubros`
  MODIFY `CRUBRO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `tipos_articulos`
--
ALTER TABLE `tipos_articulos`
  MODIFY `CTIPO` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
