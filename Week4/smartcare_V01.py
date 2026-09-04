#task 1
# Create and run a simple Python file with basic input,output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# # First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

# appointments = []

# def book_appointment(patient_name, practitioner_name, appointment_time):
#     if not patient_name:
#         raise ValueError("Patient name cannot be empty")
#     appointment = {
#         "patient": patient_name,
#         "practitioner": practitioner_name,
#         "time": appointment_time
#     }
#     appointments.append(appointment)

# def display_appointments():
#     if not appointments:
#         print("No appointments recorded.")
#         return
#     for appointment in appointments:
#         print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

# print("Welcome to SmartCare: The Clinical Appointment Booking System!")
# book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
# book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
# display_appointments()


# Here is the AI version:

appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    #One improvement: I added a piece of validation where I check if the practictioner name is not empty
    if patient_name == "" and practitioner_name == "":
        print("Patient and/or practitioner fields cannot be empty.")
        return

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment added successfully.")

def show_appointments():
    if len(appointments) == 0:
        print("No appointments found.")
        return

    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']}, "
            f"Practitioner: {appointment['practitioner']}, "
            f"Time: {appointment['time']}"
        )

# Example usage
add_appointment("Alice Smith", "Dr. John Doe", "10:00 AM")
add_appointment("Bob Johnson", "Dr. Jane Roe", "11:30 AM")

show_appointments()





