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
            parsed_items = re.search('^(\d{3})\s{2,}(\d{1,})\s{2,}(\w.*?)\s{2,}(\d{1,})\s{2,}(\d{2,})\s{2,}(\d{1,})\s{2,}(\d{1,})', i)
            parsed_log['hunt_area'] = parsed_items.group(1)
            parsed_log['hunt_type'] = parsed_items.group(2)
            parsed_log['description'] = parsed_items.group(3).lower()
            parsed_log['total_quota'] = int(parsed_items.group(4))
            parsed_log['first_choice_applicants'] = int(parsed_items.group(5))
            parsed_log['second_choice_applicants'] = int(parsed_items.group(6))
            parsed_log['third_choice_applicants'] = int(parsed_items.group(7))
            parsed_logs.append(parsed_log.copy())

        return parsed_logs
