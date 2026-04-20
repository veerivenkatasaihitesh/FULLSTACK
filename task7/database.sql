-- Active: 1773651049755@@127.0.0.1@3306@demo
CREATE DATABASE university_db;
USE university_db;
CREATE TABLE students(
    id INT PRIMARY KEY,
    name VARCHAR(180)
)

CREATE TABLE IF NOT EXISTS marks(
    student_id INT,
    subject VARCHAR(50),
    marks INT
)

SELECT * FROM students;

DROP TABLE marks;