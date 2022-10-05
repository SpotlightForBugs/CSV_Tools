#This file contains lots of functions for working with csv files
#the functions are: Printing the contents of a csv file,converting the csv file into Text,xslx,html,xml,sql, Searching for a specific value in a csv file, and converting the csv file into a dictionary, 
#converting the csv to json and as an image, and converting the csv to a list of dictionaries.
 
 
import argparse
import csv
import json
import os
import sys
import pandas as pd



def recognize_delimiter(csv_file_path):
    """This function recognizes the delimiter of a csv file"""
    with open(csv_file_path) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        return dialect.delimiter
    

 
def create_pandas_table_from_csv(csv_file_path,delimiter):
    """This function converts a csv file into a pandas table"""
    return pd.read_csv(csv_file_path,delimiter=delimiter)


        

def format_pandas_table_as_html(pandas_table):
    """This function converts a pandas table into html"""
    return pandas_table.to_html()

def format_pandas_table_as_xlsx(pandas_table):
    """This function converts a pandas table into xlsx"""
    return pandas_table.to_excel()

def format_panadas_table_as_sql(pandas_table):
    """This function converts a pandas table into sql"""
    return pandas_table.to_sql()

def format_pandas_table_as_json(pandas_table):
    """This function converts a pandas table into json"""
    return pandas_table.to_json()

def format_pandas_table_as_xml(pandas_table):
    """This function converts a pandas table into xml"""
    return pandas_table.to_xml() 

def format_table_as_pdf(pandas_table):
    """This function converts a pandas table into a pdf"""
    return pandas_table.to_pdf()    

def format_table_as_markdown(pandas_table):
    """This function converts a pandas table into markdown"""
    return pandas_table.to_markdown()

def print_pandas_table(pandas_table):
    """This function prints the whole pandas table in a nice format"""
    print(pandas_table.to_string())
    
    

    
    
    
def search_for_value_in_pandas_table(pandas_table,value):
    """This function searches for a value in a pandas table and returns the row where the value is found"""
    try:
        return pandas_table.loc[pandas_table['value'] == value]
    except:
        print(f'The value "{value}" was not found in the table')
        return "The value was not found in the table"


def convert_pandas_table_to_dict(pandas_table):
    """This function converts a pandas table into a dictionary"""
    return pandas_table.to_dict()


parser = argparse.ArgumentParser(description='This program contains lots of functions for working with csv files')
parser.add_argument('-p','--path',help='The path to the csv file',required=True)
parser.add_argument('-d','--delimiter',help='The delimiter of the csv file, if not specified, the program will try to recognize the delimiter',action='store',dest='delimiter')
parser.add_argument('-q','--query',help='The value to search for in the csv file',action='store',dest='value')
parser.add_argument('-f','--format',help='The format to convert the csv file to',action='store',dest='format',choices=['html','xlsx','json','xml','sql','pdf','dict','md'])
parser.add_argument('-o','--output',help='The path to the output file',action='store',dest='output')
parser.add_argument('-v','--verbose',help='Print the table',action='store_true',dest='verbose',required=False,default=False)




args = parser.parse_args()



if __name__ == '__main__':
    if args.delimiter:
        delimiter = args.delimiter
    else:
        delimiter = recognize_delimiter(args.path)
        
        
        
    pandas_table = create_pandas_table_from_csv(args.path,delimiter)
    
    
    
    if args.format:
        if args.format == 'html':
            output = format_pandas_table_as_html(pandas_table)
        elif args.format == 'xlsx':
            output = format_pandas_table_as_xlsx(pandas_table)
        elif args.format == 'json':
            output = format_pandas_table_as_json(pandas_table)
        elif args.format == 'xml':
            output = format_pandas_table_as_xml(pandas_table)
        elif args.format == 'sql':
            output = format_panadas_table_as_sql(pandas_table)
        elif args.format == 'pdf':
            output = format_table_as_pdf(pandas_table)
        elif args.format == 'dict':
            output = convert_pandas_table_to_dict(pandas_table)
        elif args.format == 'md':
            output = format_table_as_markdown(pandas_table)
            
        if args.output:
            #if the file already exists, the program will ask the user if they want to overwrite it
            if os.path.exists(args.output):
                overwrite = input(f'The file "{args.output}" already exists, do you want to overwrite it? (y/n)')
                if overwrite == 'y' or overwrite == 'Y':
                    
                    with open(args.output,'w') as output_file:
                        output_file.write(output)
                else:
                    print('The file was not overwritten')
                    
                    create_new_file = input('Do you want to create a new file? (y/n)')
                    if create_new_file == 'y' or create_new_file == 'Y':
                        new_file_name = input('Enter the name of the new file: ')
                        with open(new_file_name,'w') as output_file:
                            output_file.write(output)
                    else:
                        pass
            else:
                output_file_path = args.output
                output_file_path = output_file_path.replace("."+args.format,'')
                output_file_path = output_file_path + "." + args.format
                with open(output_file_path,'w') as output_file:
                    output_file.write(output)
            
            
           
        else:
            print('The output file was not specified, the output will be printed to the screen\n')
            
           
            print(output)




