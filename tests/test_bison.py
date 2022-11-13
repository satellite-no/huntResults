from huntResults import drawresults
import pdfplumber
import pytest

pdf_file = 'tests/bison.pdf'
with pdfplumber.open(pdf_file) as pdf:
    results = drawresults.DrawResults(pdf)
    parsed_lines = results.parse_draw_results_by_line()

    def test_bisonDrawArea(): 
        assert parsed_lines[0]['hunt_area'] == '002'
        
    def test_bisonDrawType(): 
        assert parsed_lines[0]['hunt_type'] == '1'

    def test_bisonDrawDesc(): 
        assert parsed_lines[0]['description'] == 'any wild bison'

    def test_bisonDrawQuota(): 
        assert parsed_lines[0]['total_quota'] == '25'

    def test_bisonDrawFirst(): 
        assert parsed_lines[0]['first_choice_applicants'] == '413'

    def test_bisonDrawSecond(): 
        assert parsed_lines[0]['second_choice_applicants'] == '0'

    def test_bisonDrawThird(): 
        assert parsed_lines[0]['third_choice_applicants'] == '0'