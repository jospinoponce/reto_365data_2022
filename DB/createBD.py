import pymysql
import csv

# Conexión a base de datos
connection = pymysql.connect(host="localhost",user="***",password="***") #ingresar credenciales de usuario y contraseña
# Creación de la base de datos
with connection.cursor() as cursor:
  cursor.execute("DROP DATABASE IF EXISTS `365_database`")
  cursor.execute("CREATE DATABASE `365_database`")
  cursor.execute("USE `365_database`")



# Tabla `365_course_info` #Table 1
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_course_info`")
  cursor.execute("""
  CREATE TABLE `365_course_info`(
  `course_id` int NOT NULL,
  `course_title` text,
  PRIMARY KEY (`course_id`))
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci """)
# 365_course_info datos
with open('data/365_course_info.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), row[1]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_course_info` (`course_id`, `course_title`) VALUES (%s, %s)", data)


# Tabla `365_course_ratings` #Table 2
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_course_ratings`")
  cursor.execute("""
  CREATE TABLE `365_course_ratings` (
  `course_id` int NOT NULL,
  `student_id` int NOT NULL,
  `course_rating` int DEFAULT NULL,
  `date_rated` date DEFAULT NULL,
  PRIMARY KEY (`student_id`,`course_id`),
  FOREIGN KEY (`course_id`) REFERENCES `365_course_info`(`course_id`))
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_course_ratings datos
with open('data/365_course_ratings.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader)
  data = [(int(row[0]), int(row[1]), int(row[2]), row[3]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_course_ratings` (`course_id`, `student_id`, `course_rating`, `date_rated`) VALUES (%s, %s, %s, %s)", data)


# Tabla `365_exam_info` #Table 3
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_exam_info`")
  cursor.execute("""
  CREATE TABLE `365_exam_info` (
  `exam_id` int NOT NULL,
  `exam_category` int DEFAULT NULL,
  `exam_duration` int DEFAULT NULL,
  PRIMARY KEY (`exam_id`))
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_exam_info datos
with open('data/365_exam_info.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), int(row[2])) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_exam_info` (`exam_id`, `exam_category`, `exam_duration`) VALUES (%s, %s, %s)", data)


# Tabla `365_quiz_info` #Table 4
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_quiz_info`")
  cursor.execute("""
  CREATE TABLE `365_quiz_info` (
  `quiz_id` int DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer_id` int NOT NULL,
  `answer_correct` text,
  PRIMARY KEY (`answer_id`))
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_quiz_info datos
with open('data/365_quiz_info.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), int(row[2]), row[3]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_quiz_info` (`quiz_id`, `question_id`, `answer_id`, `answer_correct`) VALUES (%s, %s, %s, %s)", data)


# Tabla `365_student_info` #Table 5
with connection.cursor() as cursor:
  cursor.execute("SET FOREIGN_KEY_CHECKS=0;") # Desactivar restricciones
  cursor.execute("DROP TABLE IF EXISTS `365_student_info`;")
  cursor.execute("""
  CREATE TABLE `365_student_info` (
  `student_id` int NOT NULL,
  `student_country` text,
  `date_registered` date DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_course_ratings`(`student_id`))
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_info datos
with open('data/365_student_info.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), row[1], row[2]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_info` (`student_id`, `student_country`, `date_registered`) VALUES (%s, %s, %s)", data)





# Tabla `365_student_engagement` #Table 6
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_student_engagement`")
  cursor.execute("""
  CREATE TABLE `365_student_engagement` (
  `engagement_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `engagement_quizzes` int DEFAULT NULL,
  `engagement_exams` int DEFAULT NULL,
  `engagement_lessons` int DEFAULT NULL,
  `date_engaged` date DEFAULT NULL,
  PRIMARY KEY (`engagement_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_engagement datos
with open('data/365_student_engagement.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), int(row[2]),  int(row[3]), int(row[4]),row[5]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_engagement` (`engagement_id`, `student_id`,`engagement_quizzes`, `engagement_exams`,`engagement_lessons`,`date_engaged`) VALUES (%s, %s, %s, %s,%s,%s)", data)


# Tabla `365_student_exams` #Table 7
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_student_exams`")
  cursor.execute("""
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_exams datos
with open('data/365_student_exams.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), int(row[2]),  int(row[3]), row[4],row[5]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_exams` (`exam_attempt_id`,`student_id`, `exam_id`,`exam_result`,`exam_completion_time`,`date_exam_completed`) VALUES (%s, %s, %s, %s,%s,%s)", data)


# Tabla `365_student_quizzes` #Table 8
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_student_quizzes`")
  cursor.execute("""
  CREATE TABLE `365_student_quizzes` (
  `student_id` int DEFAULT NULL,
  `quiz_id` int DEFAULT NULL,
  `question_id` int DEFAULT NULL,
  `answer_id` int DEFAULT NULL,
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`),
  FOREIGN KEY (`answer_id`) REFERENCES `365_quiz_info`(`answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_quizzes datos
with open('data/365_student_quizzes.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = []
  for row in reader:
    # Verificamos si el valor es 'NULL' y lo convertimos a None
    student_id = int(row[0]) if row[0] != 'NULL' else None
    quiz_id = int(row[1]) if row[1] != 'NULL' else None
    question_id = int(row[2]) if row[2] != 'NULL' else None
    answer_id = int(row[3]) if row[3] != 'NULL' else None
    
    data.append((student_id, quiz_id, question_id, answer_id))
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_quizzes`(`student_id`, `quiz_id`, `question_id`, `answer_id`) VALUES (%s, %s, %s, %s)", data)


# Tabla `365_student_hub_questions` #Table 9
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_student_hub_questions`")
  cursor.execute("""
  CREATE TABLE `365_student_hub_questions` (
  `hub_question_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `date_question_asked` date DEFAULT NULL,
  PRIMARY KEY (`hub_question_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_hub_questions datos
with open('data/365_student_hub_questions.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), row[2]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_hub_questions` (`hub_question_id`,`student_id`, `date_question_asked`) VALUES (%s, %s, %s)", data)



# Tabla `365_student_learning` #Table 10
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_student_learning`")
  cursor.execute("""
  CREATE TABLE `365_student_learning` (
  `student_id` int DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  `minutes_watched` double DEFAULT NULL,
  `date_watched` date DEFAULT NULL,
FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_learning datos
with open('data/365_student_learning.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), row[2], row[3]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_learning` (`student_id`, `course_id`, `minutes_watched`,`date_watched`) VALUES (%s, %s, %s, %s)", data)



# Tabla `365_student_purchases` #Table 11
with connection.cursor() as cursor:
  cursor.execute("DROP TABLE IF EXISTS `365_student_purchases`")
  cursor.execute("""
  CREATE TABLE `365_student_purchases` (
  `purchase_id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `purchase_type` text,
  `date_purchased` date DEFAULT NULL,
  PRIMARY KEY (`purchase_id`),
  FOREIGN KEY (`student_id`) REFERENCES `365_student_info`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""") 
# 365_student_purchases datos
with open('data/365_student_purchases.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader) 
  data = [(int(row[0]), int(row[1]), row[2], row[3]) for row in reader]
with connection.cursor() as cursor:
  cursor.executemany("INSERT INTO `365_student_purchases` (`purchase_id`, `student_id`, `purchase_type`, `date_purchased`) VALUES (%s, %s, %s, %s)", data)



# Guardar los cambios
connection.commit()
# Cerrar la conexión
connection.close()
