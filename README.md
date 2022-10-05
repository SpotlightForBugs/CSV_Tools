# CSV_Tools

---

CSV_Tools is a collection of tools for working with CSV files.
It is written in Python and is available on GitHub.

---

## Installation

---

```bash
git clone https://gitHub.com/SpotlightForBugs/CSV_Tools.git
cd CSV_Tools
pip install -r requirements.txt
```

---

## Usage
```fish
usage: csv_tools.py [-h] -p PATH [-d DELIMITER] [-q VALUE] [-x | -j | -t | -htm | -xm | -s | -pdf | -m | -i | -c] [-o OUTPUT] [-v]

This program contains lots of functions for working with csv files

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The path to the csv file
  -d DELIMITER, --delimiter DELIMITER
                        The delimiter of the csv file, if not specified, the program will try to recognize the delimiter
  -q VALUE, --query VALUE
                        The value to search for in the csv file
  -x, --xlsx            Convert the csv file to xlsx
  -j, --json            Convert the csv file to json
  -t, --txt             Convert the csv file to txt
  -htm, --html          Convert the csv file to html
  -xm, --xml            Convert the csv file to xml
  -s, --sql             Convert the csv file to sql
  -pdf, --pdf           Convert the csv file to pdf
  -m, --md              Convert the csv file to markdown
  -i, --image           Convert the csv file to an image
  -c, --csv             format the CSV file if it is poorly indented etc.
  -o OUTPUT, --output OUTPUT
                        The path to the output file
  -v, --verbose         Print the table
```
<!--end_of_usage-->


### inspired by P.B.





