import asyncio
import random
import csv 
import time
def create_mock_send_email(fail_rate=0.2, max_sleep_time=5):
    async def mock_send_email(to_address):
        # Simulate random sleep time
        sleep_time = random.uniform(0, max_sleep_time)
        await asyncio.sleep(sleep_time)        # Simulate failure based on the provided fail rate
        if random.random() < fail_rate:
            raise Exception(f"Failed to send email to {to_address}")        
        return f"Email sent to {to_address} successfully after {sleep_time:.2f} seconds"    
    return mock_send_email





async def set_values_to_send_emails(path, fail_rate, concurrency):
    concurrency = int(concurrency)
    rate= float(fail_rate)
    mock_send_email= create_mock_send_email(fail_rate=rate)
    tasks = []
    i = 0
    


    with open(path, newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        row_count = sum(1 for _ in reader)
        csvfile.seek(0) 
        next(reader)

        for row in reader:
            i+= 1
            tasks.append(asyncio.create_task(mock_send_email(row['Email'])))

            if i == concurrency or  concurrency >= row_count:
                await asyncio.gather(*tasks, return_exceptions= True)
                tasks = []
                i = 0


    return time.perf_counter()
            

            
        
        
    