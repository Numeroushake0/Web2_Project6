from data.db_connection import create_connection

def create_tables():
    sql_create_groups = """
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """

    sql_create_students = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id)
    );
    """

    sql_create_teachers = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """

    sql_create_subjects = """
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
    """

    sql_create_grades = """
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_of DATE,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    );
    """

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql_create_groups)
    cur.execute(sql_create_students)
    cur.execute(sql_create_teachers)
    cur.execute(sql_create_subjects)
    cur.execute(sql_create_grades)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
