--CREATE TABLE dogs (
--    name TEXT,
--    bread TEXT,
--    age INTEGER
--);
--
--CREATE TABLE cats(
--name TEXT,
--bread TEXT,
--age INTEGER
--);
--
--INSERT INTO dogs (name, bread, age) VALUES ("Champ", "Husky", 4);
--INSERT INTO dogs (name, bread, age) VALUES ("Rose", "Chihuahua", 11);
--INSERT INTO dogs (name, bread, age) VALUES ("Moose", "Lab", 5);
--INSERT INTO dogs (name, bread, age) VALUES ("Piggy", "Corgi", 9);
--INSERT INTO dogs (name, bread, age) VALUES ("Maggie", "Terrier", 4);
--INSERT INTO dogs (name, bread, age) VALUES ("River", "Husky", 7);
--INSERT INTO dogs (name, bread, age) VALUES ("Archer", "Pitbull", 8);
--INSERT INTO dogs (name, bread, age) VALUES ("Pam", "Pug", 2);

--SELECT * FROM dogs WHERE name IS "Piggy";

--SELECT * FROM dogs WHERE bread IS "Husky"
--SELECT name FROM dogs WHERE bread IS "Husky"

--SELECT * FROM dogs WHERE bread IS NOT "Chihuahua"
--SELECT * FROM dogs WHERE bread IS NOT "Chihuahua" AND bread IS NOT "Pug"

--SELECT * FROM dogs WHERE age >= 8

SELECT * FROM dogs WHERE name like "%gg%";