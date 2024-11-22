import asyncio
import random
import csv 
import time

time_total = 0
err_count= 0
err_time= 0
ok_count=0
ok_time=0 

stats = {
        "err_count": 0,
        "err_time": 0,
        "ok_count": 0,
        "ok_time": 0,
        "total_time":0
    }

def create_mock_send_email(fail_rate=0.2, max_sleep_time=5):
    async def mock_send_email(to_address):
        # Simulate random sleep time
        sleep_time = random.uniform(0, max_sleep_time)
        await asyncio.sleep(sleep_time)        # Simulate failure based on the provided fail rate
        if random.random() < fail_rate:
            global err_count, err_time
            err_count += 1
            err_time += sleep_time
            stats["err_count"]=err_count
            stats["err_time"]= err_time
            

            raise Exception(f"Failed to send email to {to_address}") 
        
        global ok_count, ok_time
        ok_count += 1
        ok_time += sleep_time
        stats["ok_count"]= ok_count
        stats["ok_time"]=ok_time

        return f"Email sent to {to_address} successfully after {sleep_time:.2f} seconds"    
    return mock_send_email





async def set_values_to_send_emails(semaphore, mock_send_email, email):
    async with semaphore:
        try:
            result = await mock_send_email(email)
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    
    

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
    return stats


class Results():
    def __init__(self, ok_time, ok_count, err_count, err_time, time_total):
        self.ok_time = ok_time
        self.ok_count = ok_count
        self.err_count = err_count
        self.err_time = err_time
        self.time_total = time_total
        
            



        
        
    