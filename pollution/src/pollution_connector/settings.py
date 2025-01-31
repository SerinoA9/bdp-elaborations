import os

import dateutil.parser
import pytz

# Celery
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL")
CELERY_RESULT_EXPIRATION_SECONDS = int(os.getenv("CELERY_RESULT_EXPIRATION_SECONDS", 604800))

# Pollution task
POLLUTION_TASK_SCHEDULING_MINUTE = os.getenv("POLLUTION_TASK_SCHEDULING_MINUTE", "*/10")
POLLUTION_TASK_SCHEDULING_HOUR = os.getenv("POLLUTION_TASK_SCHEDULING_HOUR", "*")

# Sentry
SENTRY_SAMPLE_RATE = float(os.getenv("SENTRY_SAMPLE_RATE", 1.0))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_LEVEL_LIBS = os.getenv("LOG_LEVEL_LIBS", "DEBUG")
LOGS_DIR = os.getenv("LOGS_DIR", "")

# Open Data Hub
ODH_BASE_READER_URL = os.getenv("ODH_BASE_READER_URL")
ODH_BASE_WRITER_URL = os.getenv("ODH_BASE_WRITER_URL")
ODH_AUTHENTICATION_URL = os.getenv("ODH_AUTHENTICATION_URL")
ODH_USERNAME = os.getenv("ODH_USERNAME")
ODH_PASSWORD = os.getenv("ODH_PASSWORD")
ODH_CLIENT_ID = os.getenv("ODH_CLIENT_ID")
ODH_CLIENT_SECRET = os.getenv("ODH_CLIENT_SECRET")
ODH_GRANT_TYPE = os.getenv("ODH_GRANT_TYPE", "password").split(";")
ODH_PAGINATION_SIZE = int(os.getenv("ODH_PAGINATION_SIZE", 200))
ODH_MAX_POST_BATCH_SIZE = int(os.getenv("ODH_MAX_POST_BATCH_SIZE")) if os.getenv("ODH_MAX_POST_BATCH_SIZE") else None
ODH_COMPUTATION_BATCH_SIZE = int(os.getenv("ODH_COMPUTATION_BATCH_SIZE", 30))
ODH_MINIMUM_STARTING_DATE = dateutil.parser.parse(os.getenv("ODH_MINIMUM_STARTING_DATE", "2018-01-01"))

# General
DEFAULT_TIMEZONE = pytz.timezone(os.getenv("DEFAULT_TIMEZONE", "Europe/Rome"))

# Requests management
REQUESTS_TIMEOUT = float(os.getenv("REQUESTS_TIMEOUT", 300))
REQUESTS_MAX_RETRIES = int(os.getenv("REQUESTS_MAX_RETRIES", 1))
REQUESTS_SLEEP_TIME = float(os.getenv("REQUESTS_SLEEP_TIME", 0))
REQUESTS_RETRY_SLEEP_TIME = float(os.getenv("REQUESTS_RETRY_SLEEP_TIME", 30))

# Provenance
PROVENANCE_ID = os.getenv("PROVENANCE_ID")
PROVENANCE_LINEAGE = os.getenv("PROVENANCE_LINEAGE", "u-hopper")
PROVENANCE_NAME = os.getenv("PROVENANCE_NAME", "a22-pollutant-elaboration")
PROVENANCE_VERSION = os.getenv("PROVENANCE_VERSION", "0.1.0")

COMPUTATION_CHECKPOINT_REDIS_HOST = os.getenv("COMPUTATION_CHECKPOINT_REDIS_HOST", None)
COMPUTATION_CHECKPOINT_REDIS_PORT = int(os.getenv("COMPUTATION_CHECKPOINT_REDIS_PORT", 6379))
COMPUTATION_CHECKPOINT_REDIS_DB = int(os.getenv("COMPUTATION_CHECKPOINT_REDIS_DB", 0))
