class Profile:
    def __init__(self, user_id, billing_information=None, gpa=None):
        self.user_id = user_id
        self.billing_information = billing_information if billing_information else {}
        self.gpa = gpa

    def viewBillingInformation(self):
        print("=== Informasi Tagihan ===")
        if self.billing_information:
            for key, value in self.billing_information.items():
                print(f"{key}: {value}")
        else:
            print("Tidak ada informasi tagihan.")

    def viewGPA(self):
        if self.gpa is not None:
            print(f"IPK/IPS: {self.gpa:.2f}")
        else:
            print("IPK/IPS belum tersedia.")
