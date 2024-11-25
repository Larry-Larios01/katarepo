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


            
    
    

async def set_values_to_send_emails(rows: Iterable[dict], concurrency: int, send_email_func):
    concurrency = int(concurrency)
    i = 0
    row_count = len(rows)
    tasks = []
    
    
    for row in rows:
        i+= 1
        tasks.append(asyncio.create_task(send_email_func(row['Email'])))
        if i == concurrency or  concurrency >= row_count:
            results = await asyncio.gather(*tasks, return_exceptions= True)
            i = 0
            for result in results:
                if isinstance(result, Exception):
                    print(f"Error: {result}")
                else:
                    print(result)
            
            # Limpiar lista de tareas para el próximo lote
            tasks = []


         
        



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
        
            



        
        
    