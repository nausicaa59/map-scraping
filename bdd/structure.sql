-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mar 14 Février 2017 à 14:44
-- Version du serveur :  5.5.54-0+deb8u1
-- Version de PHP :  5.6.29-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `packing`
--


-- --------------------------------------------------------

--
-- Structure de la table `auteurs`
--

CREATE TABLE IF NOT EXISTS `auteurs` (
`id` int(11) NOT NULL,
  `pseudo` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `cheked_profil` int(11) NOT NULL DEFAULT '0',
  `pays` varchar(100) NOT NULL DEFAULT 'inconnu',
  `nb_messages` int(11) NOT NULL DEFAULT '0',
  `img_lien` varchar(250) NOT NULL DEFAULT 'http://image.jeuxvideo.com/avatar-md/default.jpg',
  `nb_relation` int(11) NOT NULL DEFAULT '0',
  `banni` tinyint(4) NOT NULL DEFAULT '0',
  `date_inscription` date NOT NULL DEFAULT '0000-00-00',
  `coord_X` double NOT NULL DEFAULT '0',
  `coord_Y` double NOT NULL DEFAULT '0'
) ENGINE=InnoDB AUTO_INCREMENT=168363 DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `auteurs`
--
ALTER TABLE `auteurs`
 ADD PRIMARY KEY (`id`), ADD KEY `pseudo` (`pseudo`), ADD KEY `pseudo_2` (`pseudo`), ADD KEY `pseudo_3` (`pseudo`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `auteurs`
--
ALTER TABLE `auteurs`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=0;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
