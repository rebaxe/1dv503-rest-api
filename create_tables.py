from pymysql import MySQLError

def create_table_students(cursor):
  # Define query for creating planets table.
    create_students = "CREATE TABLE `students` (" \
                      "  `student_id` int(50) NOT NULL AUTO_INCREMENT," \
                      "  `name` varchar(255)," \
                      "  `house` varchar(255)," \
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