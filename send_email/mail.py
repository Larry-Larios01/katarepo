import asyncio

import random
import csv 
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
    rate= float(fail_rate)
    mock_send_email= create_mock_send_email(fail_rate=rate)
    

    import csv

    with open(path, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            result = await mock_send_email(row['Email'])
            print(result)
        
    