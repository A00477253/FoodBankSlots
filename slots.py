import requests
import os
import yagmail

def check_and_notify():
    api_url = "https://outlook.office365.com/owa/calendar/SMUCommunityFoodRoom@smuhalifax.onmicrosoft.com/bookings/service.svc/GetStaffBookability"

    # Payload
    payload = {
        "StaffList": ["Epzsyod+DU+2CuNeeh8sTw=="],
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
            print("Slot available")
            send_email()
        else:
            print("No available slots")
    else:
        print(f"API call failed with status code: {response.status_code}")
        print(response.text)

def send_email():
    sender = os.getenv('MY_EMAIL')
    password = os.getenv('MY_PASSWORD')
    receiver = 'malusarepra@gmail.com'
    subject = 'Food Bank Booking Open!'
    body = 'The food bank booking is now open. Visit the site to book.'
    yag = yagmail.SMTP(user=sender, password=password)

    try:
        yag.send(to=receiver, subject=subject, contents=body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

check_and_notify()
