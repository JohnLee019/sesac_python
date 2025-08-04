import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # TLS
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")        # yourname@gmail.com
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")  # 앱 비밀번호(16자리)

RECIPIENT_MAIL = GMAIL_EMAIL  # 테스트용으로 자기 자신

subject = 'Gmail SMTP 테스트'
body = '이 메일은 파이썬으로 보냈습니다.'

message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = GMAIL_EMAIL
message['to'] = RECIPIENT_MAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()
    smtp.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
    smtp.sendmail(GMAIL_EMAIL, RECIPIENT_MAIL, message.as_string())
    print("메일이 성공적으로 발송되었습니다.")
except Exception as e:
    print(f"메일 전송 중 오류: {e}")
finally:
    smtp.quit()
