import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# File to store credentials
CREDENTIALS_FILE = 'credentials.txt'

def save_credentials(username, password):
    with open(CREDENTIALS_FILE, 'w') as f:
        f.write(f"{username}\n{password}")

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as f:
            return f.read().strip().split('\n')
    return None, None

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Save credentials
    save_credentials(username, password)

    # Set up the WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

    try:
        # Open Instagram login page
        driver.get('https://www.instagram.com/accounts/login/')

        # Wait for the page to load
        time.sleep(3)

        # Find the username and password fields and enter your credentials
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        # Wait for the login to complete
        time.sleep(8)

        # Navigate to the Reels section
        driver.get('https://www.instagram.com/reels/')

        # Wait for the Reels page to load
        time.sleep(5)

        # Scroll through the Reels
        for _ in range(10):  # Adjust the range for more or fewer scrolls
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)  # Wait for the new content to load

    finally:
        # Close the browser after scrolling
        driver.quit()

# Load existing credentials
username, password = load_credentials()

# Create the GUI
root = tk.Tk()
root.title("Instagram Login")
root.geometry("400x600")  # Set the window size
root.configure(bg="#FFFFFF")  # Set background color

# Instagram logo
logo = tk.Label(root, text="Instagram", font=("Helvetica", 32, "bold"), bg="#FFFFFF", fg="#3897F0")
logo.pack(pady=20)

# Username field
username_label = tk.Label(root, text="Username", font=("Helvetica", 12), bg="#FFFFFF")
username_label.pack(pady=(10, 0))
username_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
username_entry.pack(pady=(0, 10))
username_entry.insert(0, username if username else "")

# Password field
password_label = tk.Label(root, text="Password", font=("Helvetica", 12), bg="#FFFFFF")
password_label.pack(pady=(10, 0))
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
password_entry.pack(pady=(0, 20))
password_entry.insert(0, password if password else "")

# Login button
login_button = tk.Button(root, text="Log In", command=login, bg="#3897F0", fg="white", font=("Helvetica", 12, "bold"), width=30)
login_button.pack(pady=(10, 10))

# Forgot password link
forgot_password = tk.Label(root, text="Forgot password?", font=("Helvetica", 10), bg="#FFFFFF", fg="#3897F0")
forgot_password.pack(pady=(10, 0))

# Run the application
root.mainloop()
