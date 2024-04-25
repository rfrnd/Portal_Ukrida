class Learning:
    def __init__(self, course_id, room=None, lecture_notes=None, grade_records=None):
        self.course_id = course_id
        self.room = room
        self.lecture_notes = lecture_notes if lecture_notes else []
        self.grade_records = grade_records if grade_records else {}

    def viewCourseMaterials(self):
        print("=== Materi Pembelajaran ===")
        if self.lecture_notes:
            for note in self.lecture_notes:
                print(note)
        else:
            print("Belum ada materi pembelajaran untuk kursus ini.")

    def downloadCourseMaterials(self, material):
        if material in self.lecture_notes:
            print(f"Mendownload {material}...")
            # Implementasi untuk proses mengunduh materi
        else:
            print(f"{material} tidak ditemukan dalam materi pembelajaran.")

    def accessGrades(self):
        print("=== Catatan Nilai ===")
        if self.grade_records:
            for student, grade in self.grade_records.items():
                print(f"{student}: {grade}")
        else:
            print("Belum ada catatan nilai untuk kursus ini.")
