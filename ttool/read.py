import cv2
import typing
from PIL import Image


def ReadImage(imagepath: str, mode: str = 'cv2') -> typing.Any:
    """Read image in one manner of opencv or pillow.

    Args:
        imagepath: img file path.
        mode: one of ['pillow', 'cv2'].
    """
    if mode == 'pillow':
        img = Image.open(imagepath)
    elif mode == "opencv":
        img = cv2.imread(imagepath)
    return img
