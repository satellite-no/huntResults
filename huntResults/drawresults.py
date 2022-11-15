import re
import pdfplumber

class DrawResults:
    def __init__(self, pdf):
        self.pdf = pdf

    def get_draw_results_by_line(self, pdf):
        results = []
        for page in pdf.pages:
            area_type_results = page.search('(\d{3})\s{2,}(\d)\s{2,}(\w.*?)\s{2,}(\d{1,})\s{1,}(\d{1,})\s{2,}(\d{1,})\s{2,}(\d{1,})')
            for line in area_type_results:
                results.append(line['text'].rstrip())
        return results

    def parse_draw_results_by_line(self):
        result_lines = self.get_draw_results_by_line(self.pdf)
        parsed_log = {}
        parsed_logs = []
        for i in result_lines:
            main_line = re.search('^(\d{3})\s{2,}(\d{1,})\s{2,}(\w.*?)\s{2,}(\d{1,})\s{2,}(\d{2,})\s{2,}(\d{1,})\s{2,}(\d{1,})', i)
            parsed_log['hunt_area'] = main_line.group(1)
            parsed_log['hunt_type'] = main_line.group(2)
            parsed_log['description'] = main_line.group(3).lower()
            parsed_log['total_quota'] = int(main_line.group(4))
            parsed_log['first_choice_applicants'] = int(main_line.group(5))
            parsed_log['second_choice_applicants'] = int(main_line.group(6))
            parsed_log['third_choice_applicants'] = int(main_line.group(7))
            parsed_logs.append(parsed_log.copy())

        return parsed_logs

class PPResults:
    def __init__(self, pdf):
        self.pdf = pdf

    def get_pp_results_by_line(self, pdf):
        results = []
        for page in pdf.pages:
            area_type_results = page.search('(\d{1,3})\s(\d|\W).*')
            for line in area_type_results:
                results.append(line['text'].rstrip())
        return results

    def parse_pp_results_by_line(self):
        result_lines = self.get_pp_results_by_line(self.pdf)
        parsed_log = {}
        parsed_logs = []
        main_line_regex = '^(\d{3})\s+(\d)\s+(\w.*?)\s+(\d+)\s+(\d|\W)\s+(\d+)\s+(\d+)\s+(\d+\W\d{2})\W'
        secondary_line_regex = '^(\d+)\s+(\d|\W)\s+(\d+)\s+(\d+)\s+(\d+\W\d{2})\W'
        for i in result_lines:
            main_line = re.search(main_line_regex, i)
            secondary_line = re.search(secondary_line_regex, i)
            if main_line:
                results = {}
                parsed_log['hunt_area'] = main_line.group(1)
                parsed_log['hunt_type'] = main_line.group(2)
                parsed_log['description'] = main_line.group(3).lower()
                parsed_log['results'] = []
                results['quota'] = main_line.group(4).lower()
                results['issued'] = int(main_line.group(5))
                results['pref_points'] = int(main_line.group(6))
                results['first_choice_applicants'] = int(main_line.group(7))
                results['first_choice_success_odds'] = float(main_line.group(8))
                parsed_log['results'].append(results.copy())
                parsed_logs.append(parsed_log.copy())
            elif secondary_line:
                results = {}
                results['quota'] = int(secondary_line.group(1).lower())
                if secondary_line.group(2).isnumeric():
                    results['issued'] = int(secondary_line.group(2))
                else:
                    results['issued'] = secondary_line.group(2)
                results['pref_points'] = int(secondary_line.group(3))
                results['first_choice_applicants'] = int(secondary_line.group(4))
                results['first_choice_success_odds'] = float(secondary_line.group(5))
                parsed_log['results'].append(results.copy())

        return parsed_logs