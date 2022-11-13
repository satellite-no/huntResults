from huntResults import drawresults
import pdfplumber
import pytest

pdf_file = 'tests/ram.pdf'
with pdfplumber.open(pdf_file) as pdf:
    results = drawresults.DrawResults(pdf)
    parsed_lines = results.parse_draw_results_by_line()

    def test_ramDrawArea(): 
        assert parsed_lines[10]['hunt_area'] == '012'
        
    def test_ramDrawType(): 
        assert parsed_lines[10]['hunt_type'] == '1'

    def test_ramDrawDesc(): 
        assert parsed_lines[10]['description'] == 'any ram'

    def test_ramDrawQuota(): 
        assert parsed_lines[10]['total_quota'] == 1

    def test_ramDrawFirst(): 
        assert parsed_lines[10]['first_choice_applicants'] == 713

    def test_ramDrawSecond(): 
        assert parsed_lines[10]['second_choice_applicants'] == 0

    def test_ramDrawThird(): 
        assert parsed_lines[10]['third_choice_applicants'] == 0