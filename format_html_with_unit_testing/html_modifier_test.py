import unittest
from html_modifier import *
import html_modifier

class TestTheProject(unittest.TestCase):

    # ----------- TESTS FOR read_csv_and_format FUNCTION -------------

    """ This test checks if some important HTML elements exist in the returned,
        formatted string from 'read_csv_and_format' function.
        This ensures that the formatting is indeed executed,and ';' is replaced
        with <td>."""
    def test_check_for_html_elements(self):
        self.assertIn("<td>", read_csv_and_format(input_csv))
        self.assertIn("</td>",read_csv_and_format(input_csv))
        self.assertIn("<tr>", read_csv_and_format(input_csv))
        self.assertIn("</tr>", read_csv_and_format(input_csv))

    """ This test checks if the formatting function works, by ensuring that
        the returned, formatted string is not None, and is not empty."""
    def test_table_data(self):
        self.assertIsNotNone(read_csv_and_format(input_csv))
        self.assertNotEqual("",read_csv_and_format(input_csv))


    """ This test checks for exceptions (namely, IOERROR). It ensures that
        errors are never raised. And if they are, the test fails, indicating an
        'IOERROR caught' message."""
    def test_check_no_exceptions_exist(self):
        try:
            read_csv_and_format(input_csv)
        except:
            self.fail("IOError caught!")

    # ----------- TESTS FOR read_html_file FUNCTION ------------

    """ This test checks that the function 'read_html_file', which is responsible
        for reading the HTML file, works as expected."""
    def test_html_is_read(self):
        self.assertNotEqual("", read_html_file(input_html))
        self.assertIsNotNone(read_html_file(input_html))


    """ This test checks that the original HTML file, and the modified HTML file,
        do not equal each other. This ensures that the formatting and writing was
        indeed executed."""
    def test_change_in_files(self):
        self.assertNotEqual(read_html_file(input_html), read_html_file(output_html))



    """ This test checks if the original HTML file has curly brackets, 
    which are important for the string.format() method to work."""
    def test_input_html_file_has_curly_brackets(self):
        self.assertIn("{}",read_html_file(input_html))


    #-------- TESTS FOR html_file_formatter_outputter FUNCTION ----------


    """ This test checks if the output HTML file does not contain curly 
    brackets {}. If the test fails, then curly brackets are in the file, and
    thus, the formatting/outputting did not work."""
    def test_output_html_file_has_no_curly_brackets(self):
        self.assertNotIn("{}",read_html_file(output_html))