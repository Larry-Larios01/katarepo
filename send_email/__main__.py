from send_email.mail import set_values_to_send_emails
import asyncio
import argparse


async def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("--env", default=".env",help="change the credentials")
        parser.add_argument("--source", help="you can select the file")
        parser.add_argument("--fail_rate", default="0.2" ,help="the ratio of failure")
        parser.add_argument("--concurrency", default= "5", help="how many parallel mail are send")
    
    
        args = parser.parse_args()

        end_time = await set_values_to_send_emails(args.source, args.fail_rate, args.concurrency)
        print(end_time)


    





    





if __name__ == "__main__":
        asyncio.run(main())