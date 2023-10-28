--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `attempts` INTEGER
);

--
-- Table structure for table `message_network`
--

DROP TABLE IF EXISTS `message_network`;

CREATE TABLE `message_network` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `protocol_id` INTEGER NOT NULL,
  `name` TEXT NOT NULL
);

--
-- Table structure for table `object_network`
--

DROP TABLE IF EXISTS `object_network`;

CREATE TABLE `object_network` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `protocol_id` INTEGER NOT NULL,
  `name` TEXT NOT NULL
);

--
-- Table structure for table `rune`
--

DROP TABLE IF EXISTS `rune`;

CREATE TABLE `rune` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `rune_id` INTEGER,
  `rune_name` TEXT NOT NULL,
  `reliquat_weight` INTEGER,
  `object_network_id` INTEGER,
  FOREIGN KEY(object_network_id) REFERENCES object_network(id)
);

--
-- Table structure for table `target_line`
--

DROP TABLE IF EXISTS `target_line`;

CREATE TABLE `target_line` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `value` INTEGER NOT NULL,
  `item_id` INTEGER NOT NULL,
  `rune_id` INTEGER NOT NULL,
  `line` INTEGER NOT NULL,
  `column` INTEGER NOT NULL,
  FOREIGN KEY(item_id) REFERENCES item(id),
  FOREIGN KEY(rune_id) REFERENCES rune(id)
);

--
-- Table structure for table `info_file`
--

DROP TABLE IF EXISTS `info_file`;

CREATE TABLE `info_file` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `file_path` TEXT NOT NULL UNIQUE,
  `last_modified_date` DATE NOT NULL
);