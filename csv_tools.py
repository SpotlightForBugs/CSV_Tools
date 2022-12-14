# This file contains lots of functions for working with csv files
# the functions are: Printing the contents of a csv file,converting the csv file into Text,xslx,html,xml,sql, Searching for a specific value in a csv file, and converting the csv file into a dictionary,
# converting the csv to json and as an image, and converting the csv to a list of dictionaries.


import argparse
import csv
import os
import time
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt
import sentry_sdk

sentry_sdk.init(
    dsn="https://625283987ad44866a380211753df2f58@o1363527.ingest.sentry.io/4503932642656256",
    traces_sample_rate=0.5,
)


def recognize_delimiter(csv_file_path):
    """This function recognizes the delimiter of a csv file"""
    with open(csv_file_path) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        return dialect.delimiter


def create_pandas_table_from_csv(csv_file_path, delimiter):
    """This function converts a csv file into a pandas table"""
    return pd.read_csv(csv_file_path, delimiter=delimiter)


def format_pandas_table_as_html(pandas_table):
    """This function converts a pandas table into html"""
    return pandas_table.to_html()


def format_pandas_table_as_xlsx(pandas_table, output_file_path, csv_file_path):
    """This function converts a pandas table into xlsx and writes it to a file"""

    pandas_table.to_excel(
        output_file_path,
        sheet_name=output_file_path.replace("xlsx", ""),
        index=False,
        header=False,
    )
    # open the excel file
    workbook = xlsxwriter.Workbook(output_file_path)
    worksheet = workbook.add_worksheet()
    # open the csv file
    with open(csv_file_path, "r") as csv_file:
        # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=recognize_delimiter(csv_file_path))
        # iterate over the rows in the csv file
        for row_count, row in enumerate(csv_reader):
            # iterate over the columns in the csv file
            for col_count, item in enumerate(row):
                # write the item to the excel file
                worksheet.write(row_count, col_count, item)
    # close the excel file
    workbook.close()
    # close the csv file
    csv_file.close()


def format_panadas_table_as_sql(pandas_table):
    """This function converts a pandas table into sql commands that can be used to create a table"""
    sql = ""
    for index, row in pandas_table.iterrows():
        sql += "INSERT INTO table_name VALUES ("
        for item in row:
            sql += f"'{item}',"
        sql = sql[:-1]
        sql += ");"
        sql += "\n"
    return sql


def format_pandas_table_as_json(pandas_table):
    """This function converts a pandas table into json"""
    return pandas_table.to_json()


def format_pandas_table_as_xml(pandas_table):
    """This function converts a pandas table into xml"""
    return pandas_table.to_xml()


def format_pandas_table_as_markdown(pandas_table, delimiter):
    """This function converts a pandas table into a markdown table"""
    markdown = "" + "|"
    for column in pandas_table.columns:
        markdown += f" {column} |"
    markdown += "\n"
    markdown += "|"
    for _ in pandas_table.columns:
        markdown += " --- |"
    markdown += "\n"
    for index, row in pandas_table.iterrows():
        markdown += "|"
        for item in row:
            markdown += f" {item} |"
        markdown += "\n"
    return markdown


def format_pandas_table_as_txt(pandas_table):
    """This function converts a pandas table into text"""
    return pandas_table.to_string()


def format_table_as_pdf(pandas_table, output_file_path):
    """
    The format_table_as_pdf function converts a pandas table into a pdf table with matplotlib

    :param pandas_table: Pass the pandas dataframe that will be converted to a pdf table
    :param output_file_path: Specify the path of the output file
    :return: A pdf file with the table in it
    """
    if not output_file_path:
        output_file_path = f"output{time.time()}.pdf"
    elif not output_file_path.endswith(".pdf"):
        output_file_path += ".pdf"

    # this function converts a pandas table into a pdf file, default output file is output.pdf
    """This function converts a pandas table into a pdf table with matplotlib"""
    plt.axis("tight")
    plt.axis("off")
    table = plt.table(
        cellText=pandas_table.values, colLabels=pandas_table.columns, loc="center"
    )
    table.auto_set_font_size(True)
    table.set_fontsize(12)
    table.scale(3, 3)
    plt.savefig(output_file_path, bbox_inches="tight", pad_inches=0)


def convert_pandas_table_as_image(pandas_table, output_file_path):
    """This function converts a pandas table into an image
    The size of the image is determined by the number of rows and columns in the table
    The size of the font is filling the specific rectangle it is in
    """
    print(
        "This function does not always work and is subject to change, the output may not be what you expect,\n but it is still a cool feature, so I left it in"
    )
    if not output_file_path:
        output_file_path = f"output{time.time()}.png"
    elif not output_file_path.endswith(".png"):
        output_file_path += ".png"

    # this function converts a pandas table into an image, default output file is output.png

    # get the number of rows and columns of the table
    row_count = len(pandas_table.index)
    column_count = len(pandas_table.columns)

    # get the width and height of the image
    image_width = 5000
    image_height = 5000

    cell_height = image_height / row_count

    try:
        # create a new image
        image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    except MemoryError as e:
        print(
            f"Memory Error: Please use a smaller image width and height,trying with {image_width-1000}x{image_height-1000}"
        )
        try:
            image = Image.new(
                "RGB", (image_width - 1000, image_height - 1000), (255, 255, 255)
            )
        except MemoryError:
            print(
                "Memory Error: Please use a smaller image width and height,autofix failed"
            )

    if image:
        # create a new draw
        draw = ImageDraw.Draw(image)

        # get the height of the font
        font_height = cell_height / 1.5

        # get the font
        font = ImageFont.truetype("arial.ttf", int(font_height))

        # get the width and height of each cell
        cell_width = image_width / column_count
        # draw the table
        for index, row in pandas_table.iterrows():
            for item_index, item in enumerate(row):
                # calculate the x and y position of the text
                x = item_index * cell_width
                y = index * cell_height
                # draw the text
                draw.text((x, y), str(item), (0, 0, 0), font=font)

        # save the image
        image.save(output_file_path)
        # close the image

    else:
        print("Image creation failed")


def format_csv(csv_file_path):
    # this function formats a csv file to be more readable and easier to work with.
    # The functionalty of the csv file must be preserved
    # The function does not write to a file, it returns a string
    """This function formats a csv file to be more readable and easier to work with. The functionalty of the csv file must be preserved"""
    csv_string = ""
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=recognize_delimiter(csv_file_path))
        for row in csv_reader:
            for item in row:
                csv_string += f"{item},"
            csv_string = csv_string[:-1]
            csv_string += "\n"
    return csv_string


def print_pandas_table(pandas_table):
    """This function prints the whole pandas table in a nice format"""
    print(pandas_table.to_string())


def search_for_value_in_pandas_table(pandas_table, value):
    """This function searches for a value in a pandas table and returns the row where the value is found
    ignore case"""
    for index, row in pandas_table.iterrows():
        for item in row:
            if str(item).lower() == str(value).lower():
                return row
    return f"{value} was not found"


def convert_pandas_table_to_dict(pandas_table):
    """This function converts a pandas table into a dictionary"""
    return pandas_table.to_dict()


parser = argparse.ArgumentParser(
    description="This program contains lots of functions for working with csv files"
)
parser.add_argument("-p", "--path", help="The path to the csv file", required=True)
parser.add_argument(
    "-d",
    "--delimiter",
    help="The delimiter of the csv file, if not specified, the program will try to recognize the delimiter",
    action="store",
    dest="delimiter",
)
parser.add_argument(
    "-q",
    "--query",
    help="The value to search for in the csv file",
    action="store",
    dest="value",
)
# only allow one of the choices of the format argument to be specified
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-x",
    "--xlsx",
    help="Convert the csv file to xlsx",
    action="store_const",
    const="xlsx",
    dest="format",
)
group.add_argument(
    "-j",
    "--json",
    help="Convert the csv file to json",
    action="store_const",
    const="json",
    dest="format",
)
group.add_argument(
    "-t",
    "--txt",
    help="Convert the csv file to txt",
    action="store_const",
    const="txt",
    dest="format",
)
group.add_argument(
    "-htm",
    "--html",
    help="Convert the csv file to html",
    action="store_const",
    const="html",
    dest="format",
)
group.add_argument(
    "-xm",
    "--xml",
    help="Convert the csv file to xml",
    action="store_const",
    const="xml",
    dest="format",
)
group.add_argument(
    "-s",
    "--sql",
    help="Convert the csv file to sql",
    action="store_const",
    const="sql",
    dest="format",
)
group.add_argument(
    "-pdf",
    "--pdf",
    help="Convert the csv file to pdf",
    action="store_const",
    const="pdf",
    dest="format",
)
group.add_argument(
    "-m",
    "--md",
    help="Convert the csv file to markdown",
    action="store_const",
    const="md",
    dest="format",
)
group.add_argument(
    "-i",
    "--image",
    help="Convert the csv file to an image",
    action="store_const",
    const="image",
    dest="format",
)
group.add_argument(
    "-c",
    "--csv",
    help="format the CSV file if it is poorly indented etc.",
    action="store_const",
    const="csv",
    dest="format",
)


parser.add_argument(
    "-o", "--output", help="The path to the output file", action="store", dest="output"
)
parser.add_argument(
    "-v",
    "--verbose",
    help="Print the table",
    action="store_true",
    dest="verbose",
    required=False,
    default=False,
)
args = parser.parse_args()


def put_argparse_help_in_the_readme():
    """This function puts the argparse help in the readme, in the section called "Usage"
    it deletes the old usage section and replaces it with the new one
    the section starts with the line "usage: csv_tools.py [-h]" and ends with the line <!--end_of_usage-->.

    """
    readme = open("README.md", "r").read()
    start = readme.find("usage: csv_tools.py [-h]")
    end = readme.find("<!--end_of_usage-->")
    readme = readme[:start] + readme[end:]
    readme = readme.replace(
        "<!--end_of_usage-->", f"{parser.format_help()}\n<!--end_of_usage-->"
    )
    open("README.md", "w").write(readme)


args = parser.parse_args()


put_argparse_help_in_the_readme()


if __name__ == "__main__":
    delimiter = args.delimiter or recognize_delimiter(args.path)
    pandas_table = create_pandas_table_from_csv(args.path, delimiter)

    if args.format:
        if args.format == "html":
            output = format_pandas_table_as_html(pandas_table)
        elif args.format == "xlsx":
            output = format_pandas_table_as_xlsx(
                pandas_table, args.output, csv_file_path=args.path
            )
        elif args.format == "json":
            output = format_pandas_table_as_json(pandas_table)
        elif args.format == "xml":
            output = format_pandas_table_as_xml(pandas_table)
        elif args.format == "sql":
            output = format_panadas_table_as_sql(pandas_table)
        elif args.format == "pdf":
            output = format_table_as_pdf(pandas_table, args.output)
        elif args.format == "dict":
            output = convert_pandas_table_to_dict(pandas_table)
        elif args.format == "md":
            output = format_pandas_table_as_markdown(
                pandas_table, delimiter=recognize_delimiter(args.path)
            )
        elif args.format == "txt":
            output = format_pandas_table_as_txt(pandas_table)
        elif args.format == "image":
            output = convert_pandas_table_as_image(pandas_table, args.output)
        elif args.format == "csv":
            output = format_csv(args.path)
        else:
            print(args.format)

        if (
            args.output
            and args.format != "xlsx"
            and args.format != "pdf"
            and args.format != "image"
        ):
            # if the file already exists, the program will ask the user if they want to overwrite it
            if os.path.exists(args.output):
                overwrite = input(
                    f'The file "{args.output}" already exists, do you want to overwrite it? (y/n)'
                )
                if overwrite in ("y", "Y"):

                    with open(args.output, "w") as output_file:
                        output_file.write(output)
                else:
                    print("The file was not overwritten")

                    create_new_file = input("Do you want to create a new file? (y/n)")
                    if create_new_file in ("y", "Y"):
                        new_file_name = input("Enter the name of the new file: ")
                        with open(new_file_name, "w") as output_file:
                            output_file.write(output)
            else:

                output_file_path = args.output
                output_file_path = output_file_path.replace("." + args.format, "")
                output_file_path = output_file_path + "." + args.format
                with open(output_file_path, "w") as output_file:
                    output_file.write(output)

        elif args.format not in ("xlsx", "pdf", "image", "csv"):

            print("The output file was not specified, the output will be printed")
            print(output)

        elif args.format == "csv" and not args.output:
            print("The output file was not specified, the table will be printed")
            print_pandas_table(pandas_table)
        elif args.format == "csv":
            # write the csv file from the string, each line is a row
            with open(args.output, "w") as output_file:
                output_file.write(output)

        elif (
            args.format == "xlsx"
            and not args.output
            or args.format == "pdf"
            and not args.output
            or args.format == "image"
            and not args.output
        ):
            print(
                "The output file was not specified, the output will be saved in the same folder as the csv file"
            )

    if args.value:
        print(search_for_value_in_pandas_table(pandas_table, args.value))

    if args.verbose:
        print_pandas_table(pandas_table)
