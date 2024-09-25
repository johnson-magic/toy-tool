import os
import unittest
import numpy as np
from PIL import Image

from ttool.read import ReadImage

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)


class TestReadMethods(unittest.TestCase):

    def test_ReadImage(self):
        path_test_data = os.path.join(current_directory, "./data/color.jpg")
        img_pillow = ReadImage(path_test_data, "pillow")
        self.assertTrue(isinstance(img_pillow, Image.Image))

        img_opencv = ReadImage(path_test_data, "opencv")
        self.assertTrue(isinstance(img_opencv, np.ndarray))


if __name__ == '__main__':
    unittest.main()
