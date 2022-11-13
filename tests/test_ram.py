from huntResults import drawresults
import pdfplumber
import unittest

class BisonDrawTest(unittest.TestCase):

    def bisonDrawResultTest(self):
        pdf_file = 'bison.pdf'
        with pdfplumber.open(pdf_file) as pdf:
            results = drawresults.DrawResults(pdf)
            parsed_lines = results.parse_draw_results_by_line()
        
        self.assertEqual(parsed_lines[0]['hunt_area'], '002', "Area Should be 002")

if __name__ == '__main__':
    unittest.main()