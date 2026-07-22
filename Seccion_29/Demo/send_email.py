from email.mime.text import MIMEText
import smtplib
import os

def send_email(email, height, average_height, count):
    # Get credentials from environment variables
    # Set these environment variables or replace with your app-specific password
    # For Gmail with 2FA: Use App Password (not your regular password)
    # Get it from: https://myaccount.google.com/apppasswords
    from_email = os.getenv("GMAIL_EMAIL", "userTestWeb2303@gmail.com")
    from_password = os.getenv("GMAIL_PASSWORD", "wdgqxxiiqbweqqxe")
    to_email = email                        # The recipient's email address (the one submitted in the form)

    height = round(float(height), 2)
    average_height = round(float(average_height), 2)
    count = int(count or 0)
    difference = round(height - average_height, 2)
    if difference > 0:
      comparison_text = f"Your height is {difference} cm above the current average."
    elif difference < 0:
      comparison_text = f"Your height is {abs(difference)} cm below the current average."
    else:
      comparison_text = "Your height is exactly equal to the current average."

    subject = "Height Survey Results"
    message = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 30px;">
        <div style="max-width: 500px; margin: auto; background-color: #ffffff;
                    border-radius: 8px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
          <h2 style="color: #4CAF50; text-align: center;">Thank you for participating! 🎉</h2>
          <p style="font-size: 16px; color: #333;">
            We have successfully recorded your data in our height survey.
          </p>
          <div style="background-color: #f0f8f0; border-left: 4px solid #4CAF50;
                      padding: 15px; border-radius: 4px; margin: 20px 0;">
            <p style="margin: 0; font-size: 18px; color: #2e7d32;">
              📏 Your recorded height: <strong>{height} cm</strong>
            </p>
            <p style="margin: 10px 0 0 0; font-size: 16px; color: #1b5e20;">
              📊 Current average height: <strong>{average_height} cm</strong>
            </p>
            <p style="margin: 10px 0 0 0; font-size: 16px; color: #0b5d46;">
              👥 Total participants so far: <strong>{count}</strong>
            </p>
            <p style="margin: 10px 0 0 0; font-size: 14px; color: #2f4f2f;">
              {comparison_text}
            </p>
          </div>
          <p style="font-size: 14px; color: #777;">
            We will share population statistics with you once more participants have submitted their data.
          </p>
          <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;" />
          <p style="font-size: 12px; color: #aaa; text-align: center;">
            Your data is securely stored and will never be shared with third parties.
          </p>
        </div>
      </body>
    </html>
    """

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
    gmail.quit()