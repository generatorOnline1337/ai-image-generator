import unittest
from ai_image_tool.enhance import enhance_image
import os

class TestImageEnhancement(unittest.TestCase):
    def test_enhance_image(self):
        # Test enhancing an image
        output = enhance_image("tests/test_image.jpg")
        self.assertTrue(os.path.exists(output))

if __name__ == "__main__":
    unittest.main()
