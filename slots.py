import requests
import yagmail

# API endpoint
api_url = "https://outlook.office365.com/owa/calendar/SMUCommunityFoodRoom@smuhalifax.onmicrosoft.com/bookings/service.svc/GetStaffBookability"

# Payload
payload = {
    "StaffList": [
        "Epzsyod+DU+2CuNeeh8sTw=="
    ],
    "Start": "2024-03-08T00:00:00",
    "End": "2024-04-02T00:00:00",
    "TimeZone": "America/Halifax",
    "ServiceId": "mI092M_dlUusEzTPyhYB_A2"
}

# Make the API call
response = requests.post(api_url, json=payload)

# Check the response status
if response.status_code == 200:
    # Parse the response JSON
    response_data = response.json()

    # Extract bookable time blocks
    bookable_time_blocks = response_data["StaffBookabilities"][0]["BookableTimeBlocks"]

    # Check if there are any bookable time slots
    if bookable_time_blocks:
        # Send an email
        subject = "Slot Available Notification"
        body = "Slots are available! Book now."

      
        sender_email = "matchthefolks@gmail.com"
        sender_password = "sdvbfj"
        receiver_email = "viggii1963@gmail.com"  

        # Set up yagmail SMTP
        yag = yagmail.SMTP(sender_email, sender_password)

        # Send the email
        yag.send(to=receiver_email, subject=subject, contents=body)

        # Close the connection
        yag.close()
        
        print("Email sent successfully")
    else:
        print("No available slots")
else:
    print(f"API call failed with status code: {response.status_code}")
    print(response.text)
