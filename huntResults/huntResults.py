import argparse
import pdfplumber

# Vars
parser = argparse.ArgumentParser()
parser.add_argument('pdf_file')

args = parser.parse_args()

try:
    pdf_file = args.pdf_file

except TypeError as e:

    print('Error: arguments must be characters')
    parser.print_help()
    sys.exit(1)

with pdfplumber.open(pdf_file) as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())

