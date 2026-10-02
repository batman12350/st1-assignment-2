from __future__ import annotations
from datetime import date, time, datetime
from enum import Enum

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
        
        #Name field validation
        if len(self.name) == 0:
             print("The current field is empty. ")
        elif len(self.name) <= 2 and len(self.name) >= 25:
            print("Please ensure your name is between 3 and 25 characters long")
        else:
            pass 
        
        


# Appointment class

#AI generated appointment class




class AppointmentStatus(Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"


class Appointment:
    def __init__(
        self,
        appointment_id: int,
        date_time: datetime,
        status: AppointmentStatus = AppointmentStatus.BOOKED,
    ) -> None:
        self.appointment_id = appointment_id
        self.date_time = date_time
        self._status = status

    @property
    def status(self) -> AppointmentStatus:
        """Return the current appointment status."""
        return self._status

    def book_appointment(self) -> None:
        """
        Book this appointment.

        A cancelled appointment cannot be booked again. This protects
        the status transition rather than allowing arbitrary mutation.
        """
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "A cancelled appointment cannot be booked again."
            )

        self._status = AppointmentStatus.BOOKED

    def cancel_appointment(self) -> None:
        """
        Cancel the appointment while retaining the Appointment object.
        """
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")

        self._status = AppointmentStatus.CANCELLED

    def validate_appointment_time(self) -> bool:
        """Return True when the appointment is scheduled in the future."""
        return self.date_time > datetime.now(tz=self.date_time.tzinfo)

    def check_double_booking(
        self,
        other_appointments: list[Appointment],
    ) -> bool:
        """
        Return True if another active appointment has the same date/time.

        Cancelled appointments do not occupy a booking slot.
        """
        return any(
            other is not self
            and other.status != AppointmentStatus.CANCELLED
            and other.date_time == self.date_time
            for other in other_appointments
        )

# class Appointment:

#     def __init__(self, appointment_id: int, patient_id: int, practitioner_id: int, Date: datetime, Time: datetime , status: str):
        
#         self.appointment = appointment_id
#         self.patient = patient_id
#         self.practitioner_id = practitioner_id
#         self.date = Date
#         self.time = Time
#         self.status = status

#     def book_appointment(self, appointment_date, appointment_time):

#         #Update values if required

#         if appointment_date is not None:
#             self.appointment_date = appointment_date
#         if appointment_time is not None:
#             self.time = appointment_time

#         # Validate new updated date and time values
#         self.validate_appointment()

#         # Update domain state upon successful validation
#         self.status = "SCHEDULED"
        

#     def validate_appointment_time(self):

#         #Date validation

#         if isinstance(self.date, str):
#             try:
#                 # Tries to parse the string into a date object
#                 self.date = datetime.strptime(self.date, "%d/%m/%Y").date()
#             except ValueError:
#                 # Executes if the format is wrong or if it's an impossible date (e.g., 31/02/2026)
#                 raise ValueError(f"Invalid date format: '{self.date}'. Expected DD/MM/YYYY.")
#         else:
#              self.date = self.date


#         if self.date > date.today():
#             raise ValueError("Cannot book an appointment for a past date.")
        

#         #Time validation
#         if isinstance(self.time, str):
#             try:
#                 # Converts "14:30" string to a datetime.time(14, 30) object
#                 self.time_slot = datetime.strptime(self.time.strip(), "%H:%M").time()
#             except ValueError:
#                 raise ValueError(f"Invalid time format: '{self.time}'. Expected HH:MM (e.g. '09:30', '14:00').")
        
#         # 2. Check if it's already a datetime.time object
#         elif not isinstance(self.time_slot, time):
#             raise ValueError("time_slot must be a string 'HH:MM' or a datetime.time object.")

#         #Status validation
#         if self.status not in ["Scheduled", "Completed", "Cancelled"]:
#             raise ValueError(f"Invalid appointment status: '{self.status}'")
#     def check_double_booking(self):
#         pass

# Patient class

class Patient:

    def __init__(self, patient_id: int, Name: str, Email: str, Phone_number: str, Date_of_birth: datetime):
        self.patient = patient_id
        self.full_name = Name
        self.email = Email
        self.phone_number = Phone_number
        self.date_of_birth = Date_of_birth

    def search_patient(self):
        pass

    def validate_patient(self):

    #Name field validation
        if len(self.full_name) == 0:
            print("The current field is empty. ")
        elif len(self.full_name) <= 2 and len(self.full_name) >= 25:
            print("Please ensure your name is between 3 and 25 characters long")
        else:
            pass 

    #Email validation
        if '@' not in self.email: 
            print("Ensure your email includes '@' symbol")
        else:
            pass

    #DOB validation
        if isinstance(self.date_of_birth, str):
            try:
                # Tries to parse the string into a date object
                self.date_of_birth = datetime.strptime(self.date_of_birth, "%d/%m/%Y").date()
            except ValueError:
                # Executes if the format is wrong or if it's an impossible date (e.g., 31/02/2026)
                raise ValueError(f"Invalid date format: '{self.date_of_birth}'. Expected DD/MM/YYYY.")
        else:
            self.date_of_birth = self.date_of_birth

        if self.date_of_birth > date.today():
            raise ValueError("Date of birth cannot be in the future.")

    def update_patient(self, Name, Email, Phone_Number, DOB):
        #Store old values just in case updated values are wrong

        old_name = self.full_name
        old_email = self.email
        old_phone = self.phone_number
        old_DOB = self.date_of_birth

        try: 
            if Name is not None:
                self.full_name = Name.strip()
            if Phone_Number is not None:
                self.phone_number = Phone_Number.strip()
            if Email is not None:
                self.email = Email
            if DOB is not None:
                self.date_of_birth = DOB

            self.validate_patient()
        except ValueError as e:
            # Rollback to valid state if new inputs fail checks
             
             old_name = self.full_name
             old_email = self.email
             old_phone = self.phone_number
             old_DOB = self.date_of_birth
             raise ValueError(f"Update failed: {e}")




    def view_appointment_history(self):
        pass



def main():
    #Patient class testing
    # Patient1 = Patient(1, "Muthu", "email@mm", "01234567", "17/10/2020")
    # print(vars(Patient1))
    # Patient1.update_patient(Name = "Steve", DOB = "17/101/2024", Email="jane.doe@newdomain.com", Phone_Number="0498765432")
    # print(vars(Patient1))

    #Appointment class testing
    Appt1 = Appointment(1, datetime(2025, 10, 21, 17, 30), "CANCELLED")
    Appt1.validate_appointment_time()
    Appt1.book_appointment()
    print(vars(Appt1))

    Appt2 = Appointment(1, datetime(2025, 10, 21, 17, 30), "CANCELLED")
    Appt2.check_double_booking("CANCELLED")
    Appt2.validate_appointment_time()
    Appt2.book_appointment()

main()