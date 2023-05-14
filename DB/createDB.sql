-- Se crea la Base de Datos
DROP DATABASE IF EXISTS `365_database`;
CREATE DATABASE `365_database`;
USE `365_database`;

-- Table `365_course_info` Table1
DROP TABLE IF EXISTS `365_course_info`;
CREATE TABLE `365_course_info` (
  `course_id` int NOT NULL,
  `course_title` text,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_course_info.csv'
INTO TABLE `365_course_info`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 


-- Table `365_course_ratings` Table2
DROP TABLE IF EXISTS `365_course_ratings`;
CREATE TABLE `365_course_ratings` (
  `course_id` int NOT NULL,
  `student_id` int NOT NULL,
  `course_rating` int DEFAULT NULL,
  `date_rated` date DEFAULT NULL,
  PRIMARY KEY (`student_id`,`course_id`),
  FOREIGN KEY (`course_id`) REFERENCES `365_course_info`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_course_ratings.csv'
INTO TABLE `365_course_ratings`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

-- Table `365_exam_info` Table3
DROP TABLE IF EXISTS `365_exam_info`;
CREATE TABLE `365_exam_info` (
  `exam_id` int NOT NULL,
  `exam_category` int DEFAULT NULL,
  `exam_duration` int DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_exam_info.csv'
INTO TABLE `365_exam_info`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 


-- Table `365_quiz_info` Table4
DROP TABLE IF EXISTS `365_quiz_info`;
CREATE TABLE `365_quiz_info` (
  `quiz_id` int DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer_id` int NOT NULL,
  `answer_correct` text,
  PRIMARY KEY (`answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_quiz_info.csv'
INTO TABLE `365_quiz_info`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 


-- Table `365_student_info` Table5
DROP TABLE IF EXISTS `365_student_info`;
CREATE TABLE `365_student_info` (
  `student_id` int NOT NULL,
  `student_country` text,
  `date_registered` date DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_course_ratings`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS=0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_info.csv'
INTO TABLE `365_student_info`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

-- Table `365_student_engagement` Table6
DROP TABLE IF EXISTS `365_student_engagement`;
CREATE TABLE `365_student_engagement` (
  `engagement_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `engagement_quizzes` int DEFAULT NULL,
  `engagement_exams` int DEFAULT NULL,
  `engagement_lessons` int DEFAULT NULL,
  `date_engaged` date DEFAULT NULL,
  PRIMARY KEY (`engagement_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_engagement.csv'
INTO TABLE `365_student_engagement`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 


-- Table `365_student_exams` Table7
DROP TABLE IF EXISTS `365_student_exams`;
CREATE TABLE `365_student_exams` (
  `exam_attempt_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `exam_result` int DEFAULT NULL,
  `exam_completion_time` double DEFAULT NULL,
  `date_exam_completed` date DEFAULT NULL,
  PRIMARY KEY (`exam_attempt_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`),
  FOREIGN KEY (`exam_id`) REFERENCES `365_exam_info`(`exam_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_exams.csv'
INTO TABLE `365_student_exams`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 


-- Table  `365_student_quizzes` Table8
DROP TABLE IF EXISTS `365_student_quizzes`;
CREATE TABLE `365_student_quizzes` (
  `student_id` int DEFAULT NULL,
  `quiz_id` int DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer_id` int DEFAULT NULL,
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`),
  FOREIGN KEY (`answer_id`) REFERENCES `365_quiz_info`(`answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_quizzes.csv'
INTO TABLE `365_student_quizzes`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 



-- Table `365_student_hub_questions` Table9
DROP TABLE IF EXISTS `365_student_hub_questions`;
CREATE TABLE `365_student_hub_questions` (
  `hub_question_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `date_question_asked` date DEFAULT NULL,
  PRIMARY KEY (`hub_question_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_hub_questions.csv'
INTO TABLE `365_student_hub_questions`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- Table `365_student_learning` Table10
DROP TABLE IF EXISTS `365_student_learning`;
CREATE TABLE `365_student_learning` (
  `student_id` int DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  `minutes_watched` double DEFAULT NULL,
  `date_watched` date DEFAULT NULL,
FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_learning.csv'
INTO TABLE `365_student_learning`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- Table  `365_student_purchases` Table11
DROP TABLE IF EXISTS `365_student_purchases`;
CREATE TABLE `365_student_purchases` (
  `purchase_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `purchase_type` text,
  `date_purchased` date DEFAULT NULL,
  PRIMARY KEY (`purchase_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\365_student_purchases.csv'
INTO TABLE `365_student_purchases`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SET FOREIGN_KEY_CHECKS=1;