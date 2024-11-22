import asyncio
import random
import csv 
import time
from collections.abc import Iterable



def create_mock_send_email(fail_rate=0.2, max_sleep_time=5):
    async def mock_send_email(to_address):
        
        # Simulate random sleep time
        sleep_time = random.uniform(0, max_sleep_time)
        await asyncio.sleep(sleep_time)        # Simulate failure based on the provided fail rate
        if random.random() < fail_rate:
            raise Exception(f"Failed to send email to {to_address}") 


        return f"Email sent to {to_address} successfully after {sleep_time:.2f} seconds"    
    return mock_send_email





async def send_to_semaphore(semaphore, mock_send_email, email, counters):
    async with semaphore:
        try:
            result = await mock_send_email(email)
            print(result)
            counters["ok_count"] += 1
        except Exception as e:
            print(f"Error: {e}")
            counters["err_counters"] += 1
    
    

async def set_values_to_send_emails(rows: Iterable[dict], concurrency: int, send_email_func, fail_rate):
    concurrency = int(concurrency)
    rate= float(fail_rate)
    mock_send_email= send_email_func(fail_rate=fail_rate)
    tasks = []
    semaphore = asyncio.Semaphore(concurrency)
    counters = {"err_count": 0, "ok_count": 0, "time_total": 0}
    try:
        for row in rows:
             tasks.append(asyncio.create_task(send_to_semaphore(semaphore, mock_send_email, row['Email'], counters)))

    except:
        raise

        
    await asyncio.gather(*tasks)
    return counters
    



async def run_csv(path, fail_rate, concurrency): 
    concurrency = int(concurrency)
    rate= float(fail_rate)
    mock_send_email= create_mock_send_email(fail_rate=rate)
    tasks = []
    


    with open(path, newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        semaphore = asyncio.Semaphore(concurrency)
        csvfile.seek(0) 
        next(reader)

        for row in reader:
             tasks.append(asyncio.create_task(set_values_to_send_emails(semaphore, mock_send_email, row['Email'])))
    await asyncio.gather(*tasks)
    time_total = time.perf_counter()
    results = Results(ok_time, ok_count, err_count, err_time, time_total)
    return results


class Results():
    def __init__(self, ok_time, ok_count, err_count, err_time, time_total):
        self.ok_time = ok_time
        self.ok_count = ok_count
        self.err_count = err_count
        self.err_time = err_time
        self.time_total = time_total
        
            



        
        
    