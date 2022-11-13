from huntResults import drawresults
import pdfplumber
import pytest

pdf_file = 'tests/PP-ram.pdf'
with pdfplumber.open(pdf_file) as pdf:
    results = drawresults.ppResults(pdf)
    parsed_lines = results.parse_draw_results_by_line()

    def test_bisonDrawArea():
        assert parsed_lines[0]['hunt_area'] == '002'
        
    def test_bisonDrawType(): 
        assert parsed_lines[0]['hunt_type'] == 1

    def test_bisonDrawDesc(): 
        assert parsed_lines[0]['description'] == 'any wild bison'

    def test_bisonDrawQuota(): 
        assert parsed_lines[0]['quota'] == '25'

    def test_bisonDrawFirst(): 
        assert parsed_lines[0]['issued'] == '413'

    def test_bisonDrawSecond(): 
        assert parsed_lines[0]['pref_points'] == '0'

    def test_bisonDrawThird(): 
        assert parsed_lines[0]['first_choice_applicants'] == '0'
    
    def test_bisonDrawThird(): 
        assert parsed_lines[0]['first_choice_success_odds'] == '0'