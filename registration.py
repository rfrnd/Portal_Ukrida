class Registration:
    def __init__(self, user_id, selected_courses=None):
        self.user_id = user_id
        self.selected_courses = selected_courses if selected_courses else []

    def selectCourses(self, courses):
        for course in courses:
            if course not in self.selected_courses:
                self.selected_courses.append(course)
                print(f"Berhasil memilih kursus: {course}")
            else:
                print(f"Anda sudah memilih kursus: {course}")

    def registerCourses(self):
        print("=== Registrasi KRS ===")
        # Implementasi untuk proses registrasi KRS
