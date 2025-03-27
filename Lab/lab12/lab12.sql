.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 19 ORDER BY smallest LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color as color1, b.color as color2 FROM students a, students b WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


CREATE TABLE sevens AS
  SELECT seven FROM students as s, numbers as n WHERE s.time = n.time AND s.number = 7 AND n.'7' = 'True'; 
