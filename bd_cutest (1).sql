-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-07-2025 a las 01:16:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_cutest`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acta`
--

CREATE TABLE `acta` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `fecha` date NOT NULL,
  `ruta_pdf` varchar(255) NOT NULL,
  `id_junta_directiva` int(11) NOT NULL,
  `asistencia_1` tinyint(1) DEFAULT NULL,
  `asistencia_2` tinyint(1) DEFAULT NULL,
  `asistencia_3` tinyint(1) DEFAULT NULL,
  `asistencia_4` tinyint(1) DEFAULT NULL,
  `asistencia_5` tinyint(1) DEFAULT NULL,
  `asistencia_6` tinyint(1) DEFAULT NULL,
  `asistencia_7` tinyint(1) DEFAULT NULL,
  `asistencia_8` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `acta`
--

INSERT INTO `acta` (`id`, `nombre`, `fecha`, `ruta_pdf`, `id_junta_directiva`, `asistencia_1`, `asistencia_2`, `asistencia_3`, `asistencia_4`, `asistencia_5`, `asistencia_6`, `asistencia_7`, `asistencia_8`) VALUES
(28, 'prueba', '2024-08-18', 'web_clubunion\\src\\static\\archivos\\a41f23b36bc54f8bb454b843b977af0b.pdf', 28, 1, 1, 1, 1, 0, 0, 0, 0),
(29, 'prueba2', '2024-08-18', 'web_clubunion\\src\\static\\archivos\\e7662b2a734041dd963d4cb99872400d.pdf', 28, 1, 1, 1, 1, 1, 0, 0, 0),
(30, 'asdasd', '2024-08-18', 'web_clubunion\\src\\static\\archivos\\c27be18fac974d2cbafb70cd704d774c.pdf', 29, 1, 0, 0, 0, 0, 0, 0, 0),
(31, 'asdasd', '2025-06-20', 'src\\static\\archivos\\818f2733bc3a45f881cae3318a437985.pdf', 28, 1, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `actividad`
--

INSERT INTO `actividad` (`id`, `nombre`, `servicio_id`, `departamento_id`, `hora_inicio`, `hora_fin`) VALUES
(6, 'act1', 4, 2, '10:00:00', '12:00:00'),
(7, '213123', 3, 3, '15:00:00', '18:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_doctor_actividad`
--

CREATE TABLE `asignacion_doctor_actividad` (
  `id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `actividad_id` int(11) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id`, `nombre`) VALUES
(2, 'Departamento 13'),
(3, 'Departamentos 132');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `doctor`
--

CREATE TABLE `doctor` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `id_usuario` smallint(3) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `doctor`
--

INSERT INTO `doctor` (`id`, `nombre`, `id_usuario`) VALUES
(2, 'steven', 19),
(3, 'erick', 18),
(4, 'reynaldo', 22),
(5, 'tefa', 18),
(6, 'doctor prueaba', 24);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `junta_directiva`
--

CREATE TABLE `junta_directiva` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `miembro1` varchar(255) DEFAULT NULL,
  `cargo1` varchar(255) DEFAULT NULL,
  `miembro2` varchar(255) DEFAULT NULL,
  `cargo2` varchar(255) DEFAULT NULL,
  `miembro3` varchar(255) DEFAULT NULL,
  `cargo3` varchar(255) DEFAULT NULL,
  `miembro4` varchar(255) DEFAULT NULL,
  `cargo4` varchar(255) DEFAULT NULL,
  `miembro5` varchar(255) DEFAULT NULL,
  `cargo5` varchar(255) DEFAULT NULL,
  `miembro6` varchar(255) DEFAULT NULL,
  `cargo6` varchar(255) DEFAULT NULL,
  `miembro7` varchar(255) DEFAULT NULL,
  `cargo7` varchar(255) DEFAULT NULL,
  `miembro8` varchar(255) DEFAULT NULL,
  `cargo8` varchar(255) DEFAULT NULL,
  `vigencia` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `junta_directiva`
--

INSERT INTO `junta_directiva` (`id`, `nombre`, `fecha_inicio`, `fecha_fin`, `miembro1`, `cargo1`, `miembro2`, `cargo2`, `miembro3`, `cargo3`, `miembro4`, `cargo4`, `miembro5`, `cargo5`, `miembro6`, `cargo6`, `miembro7`, `cargo7`, `miembro8`, `cargo8`, `vigencia`) VALUES
(28, 'junta directiva 2022 - 2023', '2024-01-01', '2024-12-30', 'Manuel Castrosssssss', 'Presidente', 'David Calonge', 'Vice-Presidente', 'Rafael Aelta', 'Director-Gerente', 'Almanzor Aguinaga', 'Director', 'Juan Silva', 'Director', 'Willy  Lozio Calderón', 'Director', 'Antonio Bellodas', 'Director', 'Carlos Labrin', 'Director', 1),
(29, 'nombre1', '2025-01-02', '2025-12-27', 'Manuel Castro', 'Presidente', 'Juan1', 'Presidente', 'Maria1', 'Presidente', 'Jose1', 'Presidente', 'Sam1', 'Presidente', 'Willy  Lozio Calderón', 'Presidente', 'Marco1', 'Presidente', 'Harold1', 'Presidente', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `memoria`
--

CREATE TABLE `memoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `anio` int(11) NOT NULL,
  `ruta_pdf` varchar(255) DEFAULT NULL,
  `id_directiva` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `memoria`
--

INSERT INTO `memoria` (`id`, `nombre`, `anio`, `ruta_pdf`, `id_directiva`) VALUES
(12, 'memoria1', 2024, 'web_clubunion\\src\\static\\archivos\\6fea9152b19f43a7854eee9d2014bf86.pdf', 28);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia`
--

CREATE TABLE `noticia` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `fecha_noticia` date NOT NULL,
  `ruta_foto` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `information` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `noticia`
--

INSERT INTO `noticia` (`id`, `titulo`, `fecha_noticia`, `ruta_foto`, `description`, `information`) VALUES
(12, 'asdasd', '2024-08-17', 'web_clubunion\\src\\static\\archivos\\37b29d37c13a40c2a9f486d0d882d4fe.mp4', 'asdasd', 'asdasdasdasd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE `servicio` (
  `id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicio`
--

INSERT INTO `servicio` (`id`, `departamento_id`, `nombre`) VALUES
(3, 3, 'Departamento 1222323'),
(4, 2, 'asdasd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `departamento_id` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`, `departamento_id`) VALUES
(18, 'user1', '$2b$12$9H1bh7rI8TxzzVqAntanwOg.4VQHUcSLxURiCurQ93YNEXYYHNqOG', 'secretaria1', 2),
(19, 'user3', '$2b$12$iQoa2z9ifqQwNDNFZY8PKOAvf059xjQd9USkxnkIY20fF0H4Dhqiq', 'secretaria3', 2),
(22, 'user2', '$2b$12$WYADoqYUjxcNcbWNExFZn.3CYt2MVrLJ0VHlKfQ.t6PFD1vz6WrKi', 'secretaria2', 3),
(24, 'stheff2001@gmail.com', '$2b$12$LVsCELNhCLvlQoQlrNiRZOkj/u/3YLpp6KpFrf9eWSXTCHp2eH5mC', 'Sthefany Tenorio Calderon', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acta`
--
ALTER TABLE `acta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_junta_directiva` (`id_junta_directiva`);

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `servicio_id` (`servicio_id`),
  ADD KEY `departamento_id` (`departamento_id`);

--
-- Indices de la tabla `asignacion_doctor_actividad`
--
ALTER TABLE `asignacion_doctor_actividad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_id` (`doctor_id`),
  ADD KEY `actividad_id` (`actividad_id`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `junta_directiva`
--
ALTER TABLE `junta_directiva`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `memoria`
--
ALTER TABLE `memoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `fk_id_directiva` (`id_directiva`);

--
-- Indices de la tabla `noticia`
--
ALTER TABLE `noticia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `titulo` (`titulo`);

--
-- Indices de la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `departamento_id` (`departamento_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acta`
--
ALTER TABLE `acta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `actividad`
--
ALTER TABLE `actividad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `asignacion_doctor_actividad`
--
ALTER TABLE `asignacion_doctor_actividad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `junta_directiva`
--
ALTER TABLE `junta_directiva`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `memoria`
--
ALTER TABLE `memoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `noticia`
--
ALTER TABLE `noticia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `servicio`
--
ALTER TABLE `servicio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `acta`
--
ALTER TABLE `acta`
  ADD CONSTRAINT `acta_ibfk_1` FOREIGN KEY (`id_junta_directiva`) REFERENCES `junta_directiva` (`id`);

--
-- Filtros para la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD CONSTRAINT `actividad_ibfk_1` FOREIGN KEY (`servicio_id`) REFERENCES `servicio` (`id`),
  ADD CONSTRAINT `actividad_ibfk_2` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`id`);

--
-- Filtros para la tabla `asignacion_doctor_actividad`
--
ALTER TABLE `asignacion_doctor_actividad`
  ADD CONSTRAINT `asignacion_doctor_actividad_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`id`),
  ADD CONSTRAINT `asignacion_doctor_actividad_ibfk_2` FOREIGN KEY (`actividad_id`) REFERENCES `actividad` (`id`);

--
-- Filtros para la tabla `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `user` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `memoria`
--
ALTER TABLE `memoria`
  ADD CONSTRAINT `fk_id_directiva` FOREIGN KEY (`id_directiva`) REFERENCES `junta_directiva` (`id`);

--
-- Filtros para la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD CONSTRAINT `servicio_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
