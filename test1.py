import unittest
from tkinter import *
from PIL import Image

from stegano import Stegno

class StegnoTest(unittest.TestCase):

    def setUp(self):
        self.stegno = Stegno()
        self.root = Tk()

    def tearDown(self):
        self.root.destroy()

    def test_decode(self):
        # Test case for decode method
        test_image_path = "logonew.png"  # Update the image path here
        test_image = Image.open(test_image_path, 'r')
        expected_output = "Hello, this is a test message for decoding."
        decoded_data = self.stegno.decode(test_image)
        self.assertEqual(decoded_data, expected_output)

    def test_encode_and_decode(self):
        # Test case for encoding and decoding
        test_image_path = "logo.png"  # Update the image path here
        test_image = Image.open(test_image_path, 'r')
        original_data = "This is a secret message."
        
        # Encode the data into the image
        self.stegno.encode_enc(test_image, original_data)
        
        # Decode the data from the image
        decoded_data = self.stegno.decode(test_image)

        self.assertEqual(decoded_data, original_data)

    def test_frame1_encode(self):
        # Test case for frame1_encode method
        f2 = Frame(self.root)
        self.stegno.frame1_encode(f2)
        # Ensure the frame is created successfully

    def test_frame1_decode(self):
        # Test case for frame1_decode method
        f2 = Frame(self.root)
        self.stegno.frame1_decode(f2)
        # Ensure the frame is created successfully

if __name__ == '__main__':
    unittest.main()

