from pymysql import MySQLError

def create_table_students(cursor):
  # Define query for creating planets table.
    create_students = "CREATE TABLE `students` (" \
                      "  `student_id` int(50) NOT NULL AUTO_INCREMENT," \
                      "  `name` varchar(255)," \
                      "  `house` varchar(255)," \
                      "  `species` varchar(255)," \
                      "  `gender` varchar(255)," \
                      "  `patronus` varchar(255)," \
                      "  `wizard` varchar(255)," \
                      "  `image` varchar(255)," \
                      "  PRIMARY KEY (`student_id`)" \
                      ")"

    try:
        print("Creating table students: ")
        # Create table with query.
        cursor.execute(create_students)
    except MySQLError as err:
        # Catch error if the table already existed. 
        print(err)
    else:
        print("Successfully create table: students.")

def create_table_staff(cursor):
  # Define query for creating planets table.
    create_staff = "CREATE TABLE `staff` (" \
                      "  `staff_id` int(50) NOT NULL AUTO_INCREMENT," \
                      "  `name` varchar(255)," \
                      "  `house` varchar(255)," \
                      "  `species` varchar(255)," \
                      "  `gender` varchar(255)," \
                      "  `patronus` varchar(255)," \
                      "  `wizard` varchar(255)," \
                      "  `image` varchar(255)," \
                      "  PRIMARY KEY (`staff_id`)" \
                      ")"

    try:
        print("Creating table staff: ")
        # Create table with query.
        cursor.execute(create_staff)
    except MySQLError as err:
        # Catch error if the table already existed. 
        print(err)
    else:
        print("Successfully create table: staff.")