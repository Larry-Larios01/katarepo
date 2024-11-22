from send_email.mail import set_values_to_send_emails, run_csv
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

        stats = await run_csv(args.source, args.fail_rate, args.concurrency)
        end_time = time.perf_counter()
        time_final = end_time-start_time
        stats["total_time"]= time_final
        results_json = json.dumps(stats, indent=4)
        print(results_json)


    





    





if __name__ == "__main__":
    asyncio.run(main())

        