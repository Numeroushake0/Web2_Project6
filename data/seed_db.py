import random
from faker import Faker
from datetime import datetime
from data.db_connection import create_connection

fake = Faker()

GROUPS = ["Group A", "Group B", "Group C"]
SUBJECTS = ["Math", "Physics", "History", "Biology", "Programming", "Literature", "Chemistry", "Philosophy"]

def seed_groups(cur):
    for group in GROUPS:
        cur.execute("INSERT INTO groups (name) VALUES (?)", (group,))

def seed_teachers(cur, num_teachers=5):
    teacher_ids = []
    for _ in range(num_teachers):
        cur.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))
        teacher_ids.append(cur.lastrowid)
    return teacher_ids

def seed_subjects(cur, teacher_ids):
    for subject in SUBJECTS:
        teacher_id = random.choice(teacher_ids)
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

def seed_students(cur, num_students=40):
    student_ids = []
    group_ids = [1, 2, 3]
    for _ in range(num_students):
        name = fake.name()
        group_id = random.choice(group_ids)
        cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
        student_ids.append(cur.lastrowid)
    return student_ids

def seed_grades(cur, student_ids):
    subject_ids = list(range(1, len(SUBJECTS) + 1))
    for student_id in student_ids:
        for _ in range(random.randint(15, 20)):
            subject_id = random.choice(subject_ids)
            grade = random.randint(60, 100)
            date_of = fake.date_between(start_date='-1y', end_date='today')
            cur.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)",
                (student_id, subject_id, grade, date_of)
            )

def seed():
    conn = create_connection()
    cur = conn.cursor()

    seed_groups(cur)
    teacher_ids = seed_teachers(cur)
    seed_subjects(cur, teacher_ids)
    student_ids = seed_students(cur)
    seed_grades(cur, student_ids)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
