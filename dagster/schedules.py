from dagster import schedule
from jobs import extract_latest_data_job

@schedule(cron_schedule="*/5 * * * *", job=extract_latest_data_job, execution_timezone="UTC")
def fifteen_minute_extract_latest_data_schedule(_context):
    return {}