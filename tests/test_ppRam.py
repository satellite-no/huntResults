from huntResults import drawresults
import pdfplumber
import pytest

pdf_file = 'tests/pp-ram.pdf'
with pdfplumber.open(pdf_file) as pdf:
    results = drawresults.PPResults(pdf)
    parsed_lines = results.parse_pp_results_by_line()

    def test_bisonDrawArea():
        assert parsed_lines[9]['hunt_area'] == '010'
        
    def test_bisonDrawType():
        assert parsed_lines[9]['hunt_type'] == '1'

    def test_bisonDrawDesc():
        assert parsed_lines[9]['description'] == 'any ram'

    def test_bisonDrawQuota():
        assert parsed_lines[9]['results'][1]['quota'] == 1

    def test_bisonDrawFirst():
        assert parsed_lines[9]['results'][1]['issued'] == 1

    def test_bisonDrawSecond():
        assert parsed_lines[9]['results'][1]['pref_points'] == 18

    def test_bisonDrawThird():
        assert parsed_lines[9]['results'][1]['first_choice_applicants'] == 2
    
    def test_bisonDrawThird():
        assert parsed_lines[9]['results'][1]['first_choice_success_odds'] == 50