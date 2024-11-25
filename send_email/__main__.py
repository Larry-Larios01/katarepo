from send_email.mail import set_values_to_send_emails, create_mock_send_email
import asyncio
import argparse
import json
import time
from send_email.factory_method import DataSourceFactory

async def main():
        start_time = time.perf_counter()
        parser = argparse.ArgumentParser()
        parser.add_argument("--env", default=".env",help="change the credentials")
        parser.add_argument("--source", help="you can select the file")
        parser.add_argument("--fail_rate", default="0.2" ,help="the ratio of failure")
        parser.add_argument("--concurrency", default= "5", help="how many parallel mail are send")
        parser.add_argument("--file_type", default= "csv", help="how many parallel mail are send")
    
        args = parser.parse_args()

        concurrency = int(args.concurrency)
        fail_rate = float(args.fail_rate)
        

        source = DataSourceFactory.create_data_source(source_type=args.file_type, path=args.source,env=args.env )

 
        
        send_email_func = create_mock_send_email(fail_rate=fail_rate)

        results = await set_values_to_send_emails(source,concurrency,send_email_func)
        end_time = time.perf_counter()

        results["total_time"]=end_time-start_time

        result_json = json.dumps(results)
       
        print(result_json)

        #stats.time_total= time_final
        #results_json = json.dumps(stats.__dict__, indent=4)
        #print(results_json)


    





    





if __name__ == "__main__":
    asyncio.run(main())

        