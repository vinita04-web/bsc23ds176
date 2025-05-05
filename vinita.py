import pandas as pd
import streamlit as st
from datetime import datetime

# Initialize a DataFrame to store the ledger
columns = ['Patient Name', 'Doctor Name', 'Appointment Date', 'Appointment Time', 'Contact Info']
appointments_df = pd.DataFrame(columns=columns)

# Function to display current appointments
def display_appointments():
    if appointments_df.empty:
        st.write("No appointments booked yet.")
    else:
        st.dataframe(appointments_df)

# Function to add a new appointment
def add_appointment(patient_name, doctor_name, appointment_date, appointment_time, contact_info):
    global appointments_df
    new_appointment = {
        'Patient Name': patient_name,
        'Doctor Name': doctor_name,
        'Appointment Date': appointment_date,
        'Appointment Time': appointment_time,
        'Contact Info': contact_info
    }
    
    # Append the new appointment to the DataFrame
    appointments_df = appointments_df.append(new_appointment, ignore_index=True)
    st.success("Appointment added successfully.")

# Function to save the appointments ledger to a CSV file
def save_appointments(filename="appointments_ledger.csv"):
    appointments_df.to_csv(filename, index=False)
    st.success(f"Appointments saved to {filename}")

# Function to load appointments from a CSV file
def load_appointments(filename="appointments_ledger.csv"):
    global appointments_df
    try:
        appointments_df = pd.read_csv(filename)
        st.success(f"Appointments loaded from {filename}")
    except FileNotFoundError:
        st.warning("No saved appointment ledger found. Starting fresh.")

# Load appointments if the file exists
load_appointments()

# Streamlit UI
st.title('Doctor Appointment Booking Ledger')

# Display options for the user
st.sidebar.title('Actions')
option = st.sidebar.selectbox("Choose an action", ['View Appointments', 'Add New Appointment', 'Save Appointments'])

if option == 'View Appointments':
    display_appointments()

elif option == 'Add New Appointment':
    st.subheader("Add New Appointment")
    patient_name = st.text_input("Patient Name")
    doctor_name = st.text_input("Doctor Name")
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    contact_info = st.text_input("Contact Info")
    
    if st.button('Add Appointment'):
        add_appointment(patient_name, doctor_name, str(appointment_date), str(appointment_time), contact_info)

elif option == 'Save Appointments':
    if st.button('Save Appointments to CSV'):
        save_appointments()

# Footer
st.sidebar.text('Developed by OpenAI GPT-4')

