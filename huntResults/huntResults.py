import argparse
import drawresults
import pdfplumber

def main():
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
        results = drawresults.DrawResults(pdf)
        parsed_lines = results.parse_draw_results_by_line()

        print(parsed_lines)

main()