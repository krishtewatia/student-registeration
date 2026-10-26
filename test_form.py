
from html.parser import HTMLParser
from pathlib import Path
import unittest


class RegistrationFormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = {}
        self.selects = {}
        self.buttons = []
        self.current_select = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs[attrs.get("id")] = attrs

        elif tag == "select":
            select_id = attrs.get("id")
            self.selects[select_id] = attrs
            self.current_select = select_id

        elif tag == "button":
            self.buttons.append(attrs)

    def handle_endtag(self, tag):
        if tag == "select":
            self.current_select = None


class TestStudentRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html = Path("index.html").read_text(encoding="utf-8")
        cls.parser = RegistrationFormParser()
        cls.parser.feed(html)

    def test_registration_form_exists(self):
        self.assertTrue(
            any(f.get("id") == "registrationForm"
                for f in self.parser.forms)
        )

    def test_student_name_field(self):
        self.assertIn("studentName", self.parser.inputs)
        self.assertEqual(
            self.parser.inputs["studentName"].get("type"), "text"
        )

    def test_roll_number_field(self):
        self.assertIn("rollNumber", self.parser.inputs)

    def test_email_field(self):
        self.assertIn("email", self.parser.inputs)
        self.assertEqual(
            self.parser.inputs["email"].get("type"), "email"
        )

    def test_course_field(self):
        self.assertIn("course", self.parser.selects)

    def test_submit_button(self):
        self.assertTrue(
            any(b.get("type") == "submit" for b in self.parser.buttons)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
