import logging
from typing import Any

from utils.email import EmailService
from utils.logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)


def handle_email_request(post_data: dict[str, Any]) -> dict[str, Any]:
    """
    Handle POST request data for email generation and sending.

    Input:
        `post_data`: Dictionary containing POST request data with email details

    Returns:
        Dictionary with success status and message

    Expected POST data structure:
        {
            "recipient": "user@example.com",
            "subject": "Email Subject",
            "body": "Email content text",
        }
    """
    try:
        validation_error_msg = {
            "success": False,
            "message": "Missing required field",
            "error": "VALIDATION_ERROR",
        }

        recipient = post_data.get("recipient")
        subject = post_data.get("subject")
        body = post_data.get("body")
        
        if not (recipient and subject and body):
            return validation_error_msg         

        succes_msg = {"success": True, "message": "Email sent successfully", "recipient": recipient, "subject": subject}
        send_fail_msg = {
            "success": False,
            "message": "Failed to send email",
            "recipient": recipient,
            "error": "SEND_FAILURE",
        }
        internal_err_msg = {"success": False, "message": "Internal server error", "error": "INTERNAL_ERROR"}


        email_service = EmailService()
        success = email_service.send_email(recipient, subject, body)

        if success:
            logger.info(f"Email processing completed for {recipient}")
            return succes_msg
        else:
            logger.error(f"Email sending failed for {recipient}")
            return send_fail_msg

    except Exception as e:
        logger.error(f"Unexpected error in handle_email_request: {e}")
        return internal_err_msg
