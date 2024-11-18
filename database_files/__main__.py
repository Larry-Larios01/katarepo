import sys
from database_files.conexion_with_postgres import run_query
import argparse


def take_path()-> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default=".env",help="change the credentials",)
    parser.add_argument("--output", default="string", help="you can select the output")
    parser.add_argument("--file", help="you can select the output")
    args = parser.parse_args()


    query = run_query(args.file, args.env, args.output)

    if args.output == "json":
        print(query)

    if args.output == "string":
        for row in query:
            print(row)


    
    
    


if __name__==  "__main__":
    
   take_path()