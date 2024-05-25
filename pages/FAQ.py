import streamlit as st
import smtplib
import tempfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(email, phone, description, image):
    # Set up SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = "rajeshk@gmail.com"
    msg['Subject'] = "Complaint from Payment App User"

    # Add email body text
    body = f"Email: {email}\nPhone: {phone}\nDescription: {description}"
    msg.attach(MIMEText(body, 'plain'))

    # Save uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(image.getvalue())
        temp_file_path = temp_file.name

    # Add image attachment
    with open(temp_file_path, 'rb') as file:
        img = MIMEImage(file.read())
    img.add_header('Content-Disposition', 'attachment', filename="proof_image.png")
    msg.attach(img)

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Function to handle payment-related issues
def handle_payment_issues():
    st.write("Please provide the following details for your complaint:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone Number:")
    description = st.text_area("Complaint Description:")
    image = st.file_uploader("Upload Proof Image:", type=["png", "jpg", "jpeg"])

    if st.button("Submit Complaint"):
        # If submit button clicked, send complaint details via email
        if email and phone and description and image:
            send_email(email, phone, description, image)
            st.success("Complaint submitted successfully!")
        else:
            st.error("Please fill in all fields and upload a proof image.")

# Streamlit app
def main():
    st.title("FAQ's")
    st.write("Select a query from the options below:")
    
    
    issue_option = st.selectbox("Select Issue:", ["How to Use App", "Payment-Related Issue","Contact Support","Transfer Funds","Change Password","Transaction History","Account Balance"])
    
    if issue_option == "How to Use App":
        # Display user manual text
        # a = st.button("instructions")
        # st.divider()
        # z = st.button("ins2")
        # st.divider()
        # p = st.button("ins3")
        # st.divider()
        # q = st.button("ins4")
        # if a:
        #     st.divider()
        #     # st.divider()
        #     st.write("these are the instructions to use the app")
        # elif q:
        #     st.divider()
        #     st.write("dummy")
        # elif z:
        #     st.divider()
        #     st.write("dummy tree")
        # elif p:
        #     st.divider()
        #     st.write("gain tree")
        st.write("Here is the user manual for the payment app:")
        st.write("1. Step 1...")
        st.write("2. Step 2...")
        st.write("3. Step 3...")
    elif issue_option == "Payment-Related Issue":
        # Handle payment-related issues
        handle_payment_issues()
    elif issue_option =="Contact Support":
        st.write("For assistance, please contact our support team at support@example.com.")
    elif issue_option =="Transfer Funds":
        st.write("To transfer funds, go to the 'Transfer' section in the app and follow the instructions.")
    elif issue_option=="Transaction History":
        st.write("You can view your transaction history in the 'Activity' section of the app.")
    elif issue_option =="Change Password":
        st.write("To change your password, go to 'Settings' > 'Security' > 'Change Password'")
    else:
        st.write("Your current account balance is $500.")
    #         "Account Balance": "Your current account balance is $500.",
    # "Transfer Funds": "To transfer funds, go to the 'Transfer' section in the app and follow the instructions.",
    # "Transaction History": "You can view your transaction history in the 'Activity' section of the app.",
    # "Change Password": "To change your password, go to 'Settings' > 'Security' > 'Change Password'.",
    # "Contact Support": "For assistance, please contact our support team at support@example.com."
        

if __name__ == "__main__":
    main()

