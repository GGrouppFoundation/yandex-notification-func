import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)


class EmailService:
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        msg = MIMEMultipart()
        msg["From"] = os.environ.get("EMAIL_FROM", "")
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.yandex.ru", 465) as server:
                server.login(os.environ.get("SMTP_USER", ""), os.environ.get("SMTP_PASSWORD", ""))
                server.ehlo()
                server.send_message(msg)
                logger.info(f"Successfully sent email to {recipient} with subject '{subject}'")
                return True
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
            return False
        except Exception as e:
            logger.error(f"An unexpected error occurred while sending email to {recipient}: {e}")
            return False
