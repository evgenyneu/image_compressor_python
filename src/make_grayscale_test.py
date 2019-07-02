from make_grayscale import make_grayscale
import os


def test_make_grayscale():
    output_path = "images/test_3x3_gray_test.bmp"
    os.remove(output_path) if os.path.exists(output_path) else None

    make_grayscale("images/test_3x3.png", output_path)
    assert os.path.exists(output_path)
    os.remove(output_path)
