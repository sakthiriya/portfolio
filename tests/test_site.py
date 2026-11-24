
import unittest
from pathlib import Path

class WebsiteTests(unittest.TestCase):

    def setUp(self):
        self.html_file = Path("index.html")
        self.html_content = self.html_file.read_text(encoding="utf-8")

    def test_html_file_exists(self):
        self.assertTrue(self.html_file.is_file())

    def test_page_title_exists(self):
        self.assertIn(
            "<title>Sakthivel S | Cloud Engineer</title>",
            self.html_content
        )

    def test_technologies_are_present(self):
        self.assertIn("Docker", self.html_content)
        self.assertIn("Kubernetes", self.html_content)

    def test_application_heading_exists(self):
        self.assertIn("Building reliable", self.html_content)
        self.assertIn("cloud infrastructure.", self.html_content)


if __name__ == "__main__":
    unittest.main()

