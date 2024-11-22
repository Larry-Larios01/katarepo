from mail import set_values_to_send_emails
import asyncio
import argparse
import json
import time


async def main():
        start_time = time.perf_counter()
        parser = argparse.ArgumentParser()
        parser.add_argument("--env", default=".env",help="change the credentials")
        parser.add_argument("--source", help="you can select the file")
        parser.add_argument("--fail_rate", default="0.2" ,help="the ratio of failure")
        parser.add_argument("--concurrency", default= "5", help="how many parallel mail are send")
    
    
        args = parser.parse_args()

        csv_to_dict = [
    {"Email": "user0@gmail.com", "Subject": "Account Activation", "Body": "We have updated our terms and conditions."},
    {"Email": "user1@example.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user2@hotmail.com", "Subject": "Your Invoice", "Body": "Thank you for signing up with us!"},
    {"Email": "user3@outlook.com", "Subject": "Welcome!", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user4@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user5@hotmail.com", "Subject": "Account Activation", "Body": "Check out our latest news and updates!"},
    {"Email": "user6@gmail.com", "Subject": "Important Update", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user7@outlook.com", "Subject": "Your Invoice", "Body": "Here is your invoice for the recent purchase."},
    {"Email": "user8@hotmail.com", "Subject": "Important Update", "Body": "We have updated our terms and conditions."},
    {"Email": "user9@hotmail.com", "Subject": "Important Update", "Body": "We have updated our terms and conditions."}
    ]

        stats = await set_values_to_send_emails(csv_to_dict,0.2,10)
        end_time = time.perf_counter()
        time_final = end_time-start_time
        stats.time_total= time_final
        results_json = json.dumps(stats.__dict__, indent=4)
        print(results_json)


    





    





if __name__ == "__main__":
    asyncio.run(main())

        