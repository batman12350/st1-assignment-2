# Practitioner Class

class Practitioner:

    def __init__(self, practitioner_id: int, patient_id: int, name: str, specialty: str):
        self.practitioner_id = practitioner_id
        self.patient = patient_id
        self.name = name
        self.specialty = specialty

    def view_schedule(self):
        pass

    def validate_gp_info(self):
        pass


# Appointment class

class Appointment:

    def __init__(self, appointment_id: int, patient_id: int, practitioner_id: int, Date_time: str , status: str):
        
        self.appointment = appointment_id
        self.patient = patient_id
        self.practitioner_id = practitioner_id
        self.date_time = Date_time
        self.status = status

    def book_appointment(self):
        pass

    def validate_appointment_time(self):
        pass

    def check_double_booking(self):
        pass

# Patient class

class Patient:

    def __init__(self, patient_id: int, Name: str, Email: str, Phone_number: str, Date_of_birth: str):
        self.patient = patient_id
        self.full_name = Name
        self.email = Email
        self.phone_number = Phone_number
        self.date_of_birth = Date_of_birth

    def search_patient(self):
        pass

    def validate_patient(self):
        pass

    def update_records(self):
        pass

    def view_appointment_history(self):
        pass
