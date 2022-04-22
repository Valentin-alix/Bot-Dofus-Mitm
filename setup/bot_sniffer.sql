-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 21 Avril 2022 à 16:50
-- Version du serveur :  5.7.11
-- Version de PHP :  7.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bot_sniffer`
--

-- --------------------------------------------------------

--
-- Structure de la table `item`
--

CREATE TABLE `item` (
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Structure de la table `message_network`
--

CREATE TABLE `message_network` (
  `id_message` int(11) DEFAULT NULL,
  `name_message` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Structure de la table `rune`
--

CREATE TABLE `rune` (
  `name` varchar(255) NOT NULL,
  `dofus_id` int(11) NOT NULL,
  `reliquat_weight` float UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `rune`
--

INSERT INTO `rune` (`name`, `dofus_id`, `reliquat_weight`) VALUES
('%Résistance Air', 212, 6),
('%Résistance Eau', 211, 6),
('%Résistance Feu', 213, 6),
('%Résistance Neutre', 214, 6),
('%Résistance Terre', 210, 6),
('-%Critique', 171, 1),
('-%Dommagesauxsorts', 2813, 1),
('-%Dommagesd\'armes', 2809, 1),
('-%Dommagesdistance', 2805, 1),
('-%Dommagesmêlée', 2801, 1),
('-%RésistanceAir', 217, 1),
('-%Résistancedistance', 2806, 1),
('-%RésistanceEau', 216, 1),
('-%RésistanceFeu', 218, 1),
('-%Résistancemêlée', 2802, 1),
('-%RésistanceNeutre', 219, 1),
('-%RésistanceTerre', 215, 1),
('-Agilité', 154, 1),
('-Chance', 152, 1),
('-Dommages', 145, 1),
('-DommagesAir', 429, 1),
('-DommagesCritiques', 419, 1),
('-DommagesEau', 427, 1),
('-DommagesFeu', 425, 1),
('-DommagesNeutre', 431, 1),
('-DommagesPoussée', 415, 1),
('-DommagesTerre', 423, 1),
('-EsquivePA', 162, 1),
('-EsquivePM', 163, 1),
('-Force', 157, 1),
('-Fuite', 754, 1),
('-Initiative', 175, 1),
('-Intelligence', 155, 1),
('-PA', 168, 1),
('-PM', 169, 1),
('-Pods', 159, 1),
('-Portée', 116, 1),
('-Prospection', 177, 1),
('-Puissance', 186, 1),
('-RésistanceAir', 247, 1),
('-RésistanceCritiques', 421, 1),
('-RésistanceEau', 246, 1),
('-RésistanceFeu', 248, 1),
('-RésistanceNeutre', 249, 1),
('-RésistancePoussée', 417, 1),
('-RésistanceTerre', 245, 1),
('-RetraitPA', 411, 1),
('-RetraitPM', 413, 1),
('-Sagesse', 156, 1),
('-Soins', 179, 1),
('-Tacle', 755, 1),
('-Vitalité', 153, 0.2),
('Agilité', 119, 1),
('Arme de chasse', 795, 5),
('Chance', 123, 1),
('Critiques', 115, 10),
('Dommages', 112, 20),
('Dommages Air', 428, 5),
('Dommages aux sorts', 2812, 5),
('Dommages Critiques', 418, 5),
('Dommages d\'armes', 2808, 15),
('Dommages distance', 2804, 15),
('Dommages Eau', 426, 5),
('Dommages Feu', 424, 5),
('Dommages mêlée', 2800, 15),
('Dommages Neutre', 430, 5),
('Dommages Pièges', 225, 5),
('Dommages Poussée', 414, 5),
('Dommages Terre', 422, 5),
('Esquive PA', 160, 7),
('Esquive PM', 161, 7),
('Force', 118, 1),
('Fuite', 752, 4),
('Initiative', 174, 0.1),
('Intelligence', 126, 1),
('Invocations', 182, 30),
('PA', 111, 100),
('PM', 128, 90),
('Pods', 158, 0.25),
('Portée', 117, 51),
('Prospection', 176, 3),
('Puissance', 138, 2),
('Puissance (pièges)', 226, 2),
('Renvoie  dommages', 220, 10),
('Résistance Air', 242, 2),
('Résistance Critiques', 420, 2),
('Résistance distance', 2807, 15),
('Résistance Eau', 241, 2),
('Résistance Feu', 243, 2),
('Résistance mêlée', 2803, 15),
('Résistance Neutre', 244, 2),
('Résistance Poussée', 416, 2),
('Résistance Terre', 240, 2),
('Retrait PA', 410, 7),
('Retrait PM', 412, 7),
('Sagesse', 124, 3),
('Soins', 178, 10),
('Tacle', 753, 4),
('Vitalité', 125, 0.2);

-- --------------------------------------------------------

--
-- Structure de la table `target_line`
--

CREATE TABLE `target_line` (
  `type_rune` varchar(255) NOT NULL,
  `value_rune` int(11) NOT NULL,
  `line_rune` int(11) NOT NULL,
  `column_rune` int(11) NOT NULL,
  `name_item` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Index pour les tables exportées
--

--
-- Index pour la table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`name`);

--
-- Index pour la table `rune`
--
ALTER TABLE `rune`
  ADD PRIMARY KEY (`name`);

--
-- Index pour la table `target_line`
--
ALTER TABLE `target_line`
  ADD KEY `name_item` (`name_item`),
  ADD KEY `type_rune` (`type_rune`);

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `target_line`
--
ALTER TABLE `target_line`
  ADD CONSTRAINT `target_line_ibfk_1` FOREIGN KEY (`name_item`) REFERENCES `item` (`name`),
  ADD CONSTRAINT `target_line_ibfk_2` FOREIGN KEY (`type_rune`) REFERENCES `rune` (`name`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
