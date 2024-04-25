class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self, password):
        if password == self.password:
            self.logged_in = True
            print("Berhasil masuk.")
            return True
        else:
            print("Gagal masuk. Email atau kata sandi salah.")
            return False

    def logout(self):
        self.logged_in = False
        print("Berhasil keluar.")

class Student(User):
    def __init__(self, email, password, student_id, courses_registered=None, grades=None):
        super().__init__(email, password)
        self.student_id = student_id
        self.courses_registered = courses_registered if courses_registered else []
        self.grades = grades if grades else {}

    def viewProfile(self):
        print("=== Profil Mahasiswa ===")
        print(f"Email: {self.email}")
        print(f"ID Mahasiswa: {self.student_id}")
        print("Mata Kuliah yang Terdaftar:")
        for course in self.courses_registered:
            print(f"- {course}")
        print("Nilai Mata Kuliah:")
        for course, grade in self.grades.items():
            print(f"- {course}: {grade}")

    def registerCourses(self, course):
        if course not in self.courses_registered:
            self.courses_registered.append(course)
            print(f"Berhasil mendaftar kursus: {course}")
        else:
            print(f"Anda sudah terdaftar dalam kursus: {course}")

    def accessSchedule(self):
        print("=== Jadwal Mata Kuliah ===")
        # Implementasi untuk mengakses jadwal mata kuliah

    def checkGrades(self, course):
        if course in self.grades:
            print(f"Nilai untuk mata kuliah {course}: {self.grades[course]}")
        else:
            print(f"Anda belum menerima nilai untuk mata kuliah {course}")

    def calculateGPA(self):
        if self.grades:
            total_grade_points = sum(self.grades.values())
            gpa = total_grade_points / len(self.grades)
            print(f"IPK Anda: {gpa:.2f}")
        else:
            print("Belum ada nilai yang tersedia untuk menghitung IPK.")

class Lecturer(User):
    def __init__(self, email, password, employee_id, courses_taught=None, attendance_records=None):
        super().__init__(email, password)
        self.employee_id = employee_id
        self.courses_taught = courses_taught if courses_taught else []
        self.attendance_records = attendance_records if attendance_records else {}

    def gradeStudents(self, student_id, course, grade):
        if course in self.courses_taught:
            if student_id in self.attendance_records.get(course, []):
                self.attendance_records[course][student_id] = grade
                print(f"Berhasil memberikan nilai {grade} untuk mahasiswa dengan ID {student_id} pada mata kuliah {course}")
            else:
                print(f"Mahasiswa dengan ID {student_id} tidak terdaftar dalam mata kuliah {course}")
        else:
            print(f"Anda tidak mengajar mata kuliah {course}")

    def takeAttendance(self, course, student_id):
        if course in self.courses_taught:
            if course not in self.attendance_records:
                self.attendance_records[course] = {}
            self.attendance_records[course][student_id] = "Hadir"
            print(f"Mahasiswa dengan ID {student_id} hadir pada mata kuliah {course}")
        else:
            print(f"Anda tidak mengajar mata kuliah {course}")

    def viewStudentList(self, course):
        if course in self.courses_taught:
            print(f"Daftar mahasiswa pada mata kuliah {course}:")
            for student_id in self.attendance_records.get(course, {}):
                print(f"- {student_id}")
        else:
            print(f"Anda tidak mengajar mata kuliah {course}")

    def uploadExamQuestions(self, course, questions):
        if course in self.courses_taught:
            print(f"Unggah soal ujian untuk mata kuliah {course}")
            # Implementasi untuk mengunggah soal ujian
        else:
            print(f"Anda tidak mengajar mata kuliah {course}")

class AcademicAdministrator(User):
    def __init__(self, email, password, employee_id):
        super().__init__(email, password)
        self.employee_id = employee_id

    def uploadSchedule(self, schedule):
        print("Mengunggah jadwal...")
        # Implementasi untuk mengunggah jadwal

    def uploadCourseRegistrations(self, course_registrations):
        print("Mengunggah KRS/Registrasi KRS...")
        # Implementasi untuk mengunggah KRS/Registrasi KRS

    def uploadStudentGPA(self, student_id, gpa):
        print(f"Mengunggah IPK mahasiswa {student_id} dengan nilai {gpa}...")
        # Implementasi untuk mengunggah IPK mahasiswa

class Operator(User):
    def __init__(self, email, password, employee_id):
        super().__init__(email, password)
        self.employee_id = employee_id

    def supportLecturer(self, lecturer_id, support_type):
        print(f"Mendukung dosen dengan ID {lecturer_id}: {support_type}")
        # Implementasi untuk mendukung dosen

    def provideTechnicalSupport(self, issue):
        print(f"Memberikan dukungan teknis untuk isu: {issue}")
        # Implementasi untuk memberikan dukungan teknis
