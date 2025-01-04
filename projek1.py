import streamlit as st

import streamlit as st
from pyrebase import pyrebase

# Konfigurasi Firebase
firebaseConfig = {
    "apiKey": "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
    "authDomain": "percobaan-pertama-ae4ff.firebaseapp.com",
    "databaseURL": "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
    "projectId": "percobaan-pertama-ae4ff",
    "storageBucket": "percobaan-pertama-ae4ff.firebasestorage.app",
    "messagingSenderId": "298037230291",
    "appId": "1:298037230291:web:73839320cd74cc9dba3226",
    "measurementId": "G-BSVCLVBYX6"
}

# Inisialisasi Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Menambahkan data ke Realtime Database
def add_data_realtime(name, age):
    db.child("users").push({"name": name, "age": age})

# Mendapatkan data dari Realtime Database
def get_data_realtime():
    users = db.child("users").get()
    return users.val()

# Streamlit UI
st.title("Firebase Realtime Database with Streamlit")

name = st.text_input("Nama:")
age = st.number_input("Umur:", min_value=0, step=1)

if st.button("Tambah Data"):
    add_data_realtime(name, age)
    st.success("Data berhasil ditambahkan!")

if st.button("Lihat Data"):
    data = get_data_realtime()
    st.table(data)
