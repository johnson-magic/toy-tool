import unittest
import numpy as np
from PIL import Image

from ttool.read import ReadImage


class TestReadMethods(unittest.TestCase):

    def test_ReadImage(self):
        img_pillow = ReadImage("./data/color.png", "pillow")
        self.assertTrue(isinstance(img_pillow, Image.Image))

        img_opencv = ReadImage("./data/color.png", "opencv")
        self.assertTrue(isinstance(img_opencv, np.ndarray))


if __name__ == '__main__':
    unittest.main()
