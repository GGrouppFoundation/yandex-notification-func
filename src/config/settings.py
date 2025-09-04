import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "prod")

IAM_TOKEN_URL = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
TRACKER_API_BASE = "https://api.tracker.yandex.net/v3"
TRACKER_BASE = "https://tracker.yandex.ru"

CLOUD_ORG_ID = os.environ.get("YANDEX_CLOUD_ORG_ID")

if ENVIRONMENT == "test":
    QUEUE_NAME = "MAATNEW"
    REQUEST_STATUS_NOTIFICATION_DAYS = [0, 10, 15]
    RESOLVED_STATUS_NOTIFICATION_DAY = [0, 1, 2, 3, 4]
    RESOLVED_STATUS_AUTOCLOSE_DAY = 0
else:
    QUEUE_NAME = "MAAT"
    REQUEST_STATUS_NOTIFICATION_DAYS = [5, 10, 15]
    RESOLVED_STATUS_NOTIFICATION_DAY = [5, 6, 7, 8, 9]
    RESOLVED_STATUS_AUTOCLOSE_DAY = 10
