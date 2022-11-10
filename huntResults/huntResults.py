import argparse
import re
import pdfplumber

def get_draw_results_by_line(pdf):
    results = []
    for page in pdf.pages:
        area_type_results = page.search('(\d{3})\s{2,}(\d)\s{2,}(\w.*?)\s{2,}(\d)\s{2,}(\d{2,})\s{2,}(\d)\s{2,}(\d)\s')
        for line in area_type_results:
            results.append(line['text'].rstrip())
    return results

def parse_draw_results_by_line(result_lines):
    parsed_log = {}
    parsed_logs = []
    for i in result_lines:
        parsed_items = re.search('^(\d{3})\s{2,}(\d)\s{2,}(\w.*?)\s{2,}(\d)\s{2,}(\d{2,})\s{2,}(\d)\s{2,}(\d)', i)
        parsed_log['hunt_area'] = parsed_items.group(1)
        parsed_log['hunt_type'] = parsed_items.group(2)
        parsed_log['description'] = parsed_items.group(3).lower()
        parsed_log['total_quota'] = parsed_items.group(4)
        parsed_log['first_choice_applicants'] = parsed_items.group(5)
        parsed_log['second_choice_applicants'] = parsed_items.group(6)
        parsed_log['third_choice_applicants'] = parsed_items.group(7)
        parsed_logs.append(parsed_log.copy())

    return parsed_logs

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
        lines = get_draw_results_by_line(pdf)
        parsed_lines = parse_draw_results_by_line(lines)

        print(parsed_lines)

main()