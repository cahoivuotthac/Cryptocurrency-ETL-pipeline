from dagster import repository
from jobs import extract_latest_data_job
from schedules import fifteen_minute_extract_latest_data_schedule

@repository
def my_repository():
    return [extract_latest_data_job, fifteen_minute_extract_latest_data_schedule]