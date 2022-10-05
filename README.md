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
usage: csv_tools.py [-h] -p PATH [-d DELIMITER] [-q VALUE] [-f {html,xlsx,json,xml,sql,pdf,dict,md}] [-o OUTPUT] [-v]

This program contains lots of functions for working with csv files

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The path to the csv file
  -d DELIMITER, --delimiter DELIMITER
                        The delimiter of the csv file, if not specified, the program will try to recognize the delimiter
  -q VALUE, --query VALUE
                        The value to search for in the csv file
  -f {html,xlsx,json,xml,sql,pdf,dict,md}, --format {html,xlsx,json,xml,sql,pdf,dict,md}
                        The format to convert the csv file to
  -o OUTPUT, --output OUTPUT
                        The path to the output file
  -v, --verbose         Print the table

---

```bash
python3 csv_tools.py -h
```
