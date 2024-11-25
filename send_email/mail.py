import asyncio
import random
import csv 
import time
from collections.abc import Iterable
from typing import TypedDict
from itertools import batched


def create_mock_send_email(fail_rate=0.2, max_sleep_time=5):
    async def mock_send_email(to_address):
        
        # Simulate random sleep time
        sleep_time = random.uniform(0, max_sleep_time)
        await asyncio.sleep(sleep_time)        # Simulate failure based on the provided fail rate
        if random.random() < fail_rate:
            raise Exception(f"Failed to send email to {to_address}, failed after {sleep_time:.2f}") 


        return f"Email sent to {to_address} successfully after {sleep_time:.2f} seconds"    
    return mock_send_email


            

async def sender(queue, send_email_func, results):
    tasks = []
    batch = []
    while True:
        while not queue.empty():
            item = await queue.get()
            batch.append(item)
            queue.task_done()
            

        tasks = [send_email_func(email) for email in batch]

        # Procesar todas las tareas del lote
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        for response in responses:
            if isinstance(response, Exception):
                print(f"Error: {response}")
                results["err_time"] += float(response.split()[-1])
                results["err_count"] += 1

            
            else:
                print(response)
                results["ok_count"] += 1
                results["ok_time"]+= float(response.split()[-2])
                

class Result(TypedDict):
    time_total: int
    err_count: int
    ok_count: int

    

async def set_values_to_send_emails(rows: Iterable[dict], concurrency: int, send_email_func):
    if concurrency <= 0:
        concurrency = 1

    do_continue = True
    result = Result(time_total=0, err_count=0, ok_count=0)

    start = time.time()
    this_iter = iter(rows)
    while do_continue:
        tasks = []
        for _ in range(concurrency):
            try:
                row = next(this_iter)
                email = row["Email"]
                task = asyncio.create_task(send_email_func(email))
                tasks.append(task)
            except StopIteration:
                do_continue = False
                break

        if not do_continue and not tasks:
            break
        
        response = await asyncio.gather(*tasks, return_exceptions=True)
        for res in response:
            if isinstance(res, Exception):
                result["err_count"] += 1
                continue

            result["ok_count"] += 1

    end = time.time()


    result["time_total"] = end - start


    return result
        


def chunked(source: Iterable, size=int)-> Iterable[list]:
    list_batches= []
    for batch in batched(source, size):
        list_batches.append(batch)
    return list_batches




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



        
            



        
        
    