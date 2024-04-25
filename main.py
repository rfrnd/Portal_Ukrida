from user import Student, Lecturer, AcademicAdministrator, Operator
from profil import Profile
from registration import Registration
from learning import Learning

def menu_login():
    print("=== Menu Masuk ===")
    email = input("Masukkan email: ")
    password = input("Masukkan kata sandi: ")

    if email in database_users:
        user = database_users[email]
        if user.login(password):
            if isinstance(user, Student):
                menu_student(user)
            elif isinstance(user, Lecturer):
                menu_lecturer(user)
            elif isinstance(user, AcademicAdministrator):
                menu_administrator(user)
            elif isinstance(user, Operator):
                menu_operator(user)
        else:
            print("Email atau kata sandi salah. Gagal masuk ke sistem.")
    else:
        print("Email atau kata sandi salah. Gagal masuk ke sistem.")


def menu_student(student):
    print("=== Menu Mahasiswa ===")
    print("1. Lihat Profil")
    print("2. Mendaftar KRS")
    print("3. Akses Jadwal Mata Kuliah")
    print("4. Periksa Nilai Mata Kuliah")
    print("5. Cek IPK/IPS")
    choice = input("Pilih opsi (1-5): ")

    if choice == "1":
        student.viewProfile()
    elif choice == "2":
        course = input("Masukkan kursus yang ingin didaftarkan: ")
        student.registerCourses(course)
    elif choice == "3":
        student.accessSchedule()
    elif choice == "4":
        course = input("Masukkan kursus yang ingin diperiksa nilai: ")
        student.checkGrades(course)
    elif choice == "5":
        student.calculateGPA()
    else:
        print("Pilihan tidak valid.")

def menu_lecturer(lecturer):
    print("=== Menu Dosen ===")
    print("1. Memberikan Penilaian")
    print("2. Mengambil Absen Mahasiswa")
    print("3. Lihat Daftar Mahasiswa di Kelas")
    print("4. Unggah Soal Ujian")
    choice = input("Pilih opsi (1-4): ")

    if choice == "1":
        student_id = input("Masukkan ID Mahasiswa: ")
        course = input("Masukkan kursus: ")
        grade = input("Masukkan nilai: ")
        lecturer.gradeStudents(student_id, course, grade)
    elif choice == "2":
        course = input("Masukkan kursus: ")
        student_id = input("Masukkan ID Mahasiswa: ")
        lecturer.takeAttendance(course, student_id)
    elif choice == "3":
        course = input("Masukkan kursus: ")
        lecturer.viewStudentList(course)
    elif choice == "4":
        course = input("Masukkan kursus: ")
        questions = input("Masukkan soal ujian: ")
        lecturer.uploadExamQuestions(course, questions)
    else:
        print("Pilihan tidak valid.")

def menu_administrator(administrator):
    print("=== Menu Administrator ===")
    print("1. Unggah Jadwal")
    print("2. Unggah KRS/Registrasi KRS")
    print("3. Unggah IPK Mahasiswa")
    choice = input("Pilih opsi (1-3): ")

    if choice == "1":
        schedule = input("Masukkan jadwal: ")
        administrator.uploadSchedule(schedule)
    elif choice == "2":
        course_registrations = input("Masukkan data KRS/Registrasi KRS: ")
        administrator.uploadCourseRegistrations(course_registrations)
    elif choice == "3":
        student_id = input("Masukkan ID Mahasiswa: ")
        gpa = input("Masukkan IPK Mahasiswa: ")
        administrator.uploadStudentGPA(student_id, gpa)
    else:
        print("Pilihan tidak valid.")

def menu_operator(operator):
    print("=== Menu Operator ===")
    print("1. Mendukung Dosen")
    print("2. Dukungan Teknis")
    choice = input("Pilih opsi (1-2): ")

    if choice == "1":
        lecturer_id = input("Masukkan ID Dosen: ")
        support_type = input("Jenis dukungan (e.g., administratif, akademik): ")
        operator.supportLecturer(lecturer_id, support_type)
    elif choice == "2":
        issue = input("Masukkan permasalahan teknis: ")
        operator.provideTechnicalSupport(issue)
    else:
        print("Pilihan tidak valid.")

# Database pengguna
database_users = {
    "mahasiswa": Student("mahasiswa", "mahasiswa1", "12345"),
    "dosen": Lecturer("dosen", "dosen1", "67890"),
    "admin": AcademicAdministrator("admin", "admin1", "54321"),
    "operator": Operator("operator", "operator1", "98765")
}

if __name__ == "__main__":
    menu_login()
