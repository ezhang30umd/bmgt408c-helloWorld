from app import app, db
from models import Major, User, Student
from werkzeug.security import generate_password_hash
import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Aerospace Engineering', 'Biology', 'Civil Engineering', 'Computer Science',
              'Electrical Engineering', 'Finance', 'Information Systems', 'Marketing',
              'Mechanical Engineering']
    for each_major in majors:
        print(f'{each_major} inserted into major')
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of users
    users = [
        {'username': 'ezhang30', 'email': 'ezhang30@terpmail.umd.edu', 'first_name':'Ethan', 'last_name':'Zhang',
            'password': generate_password_hash('ezhang30@terpmail.umd.edu', method='pbkdf2:sha256'), 'role':'STUDENT'},
        {'username': 'manager', 'email': 'manager@umd.edu', 'first_name':'Joe', 'last_name':'King',
            'password': generate_password_hash('managerpw', method='pbkdf2:sha256'), 'role':'MANAGER'},
        {'username': 'admin', 'email': 'admin@umd.edu', 'first_name':'Crystal', 'last_name':'Ball',
            'password': generate_password_hash('adminpw', method='pbkdf2:sha256'), 'role':'ADMIN'}
    ]

    for each_user in users:
        print(f'{each_user["username"]} inserted into user')
        a_user = User(username=each_user["username"], email=each_user["email"], first_name=each_user["first_name"],
                      last_name=each_user["last_name"], password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()

    # Initial loading of students first_name, last_name, email, major_id, birth_date, is_honors
    students = [
        {'student_id': '1', 'first_name': 'Ethan', 'last_name':'Zhang', 'email':'ezhang30@terpmail.umd.edu',
            'major_id':4, 'birth_date': dt.datetime(2005, 5, 10), 'is_honors':1}
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            email=each_student["email"], major_id=each_student["major_id"],
                            birth_date=each_student["birth_date"], is_honors=each_student["is_honors"])
        db.session.add(a_student)
        db.session.commit()
