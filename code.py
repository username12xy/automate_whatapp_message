import pywhatkit as kit

# Replace 'phone_number' with the recipient's phone number including the country code (e.g., +1 for the US).
phone_number = '+181406545301'

# Message you want to send
message = "Hello, this is a test message sent using Python!"

# Specify the time (24-hour format) at which you want to send the message
# For example, to send it at 12:30 PM, use the following format: sendwhatmsg(phone_number, message, 12, 30)
kit.sendwhatmsg(phone_number, message, 12, 30)  # Adjust the time as needed

# Wait for a few seconds before sending the enter key
time.sleep(5)  # Adjust the sleep time as needed

# Send an enter keypress to send the message
kit.sendwhatmsg(phone_number, '\n', 12, 30)  # Adjust the time as needed

# Note: You will need to scan the QR code with your phone to authenticate the session the first time you run this code.
