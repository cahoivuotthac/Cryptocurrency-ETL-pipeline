from dagster import Backoff, Jitter, RetryPolicy, job, op
import subprocess

@op(
    retry_policy=RetryPolicy(
        max_retries=2,
        delay=0.2, #200ms
        backoff=Backoff.EXPONENTIAL,
        jitter=Jitter.PLUS_MINUS,
    )
)
def run_extract_latest_data():
    subprocess.run(["python3", "../src/extract_latest_data.py"], check=True)

@job
def extract_latest_data_job():
    run_extract_latest_data()
    
