from compressor import load_image, compress_image
import os


def test_compress_image():
    terms = 20
    iterations = 5
    path_out = f"images/marmite_500x500_gray_compressed_{terms}terms_{iterations}iterations.bmp"

    compress_image("images/marmite_500x500_gray.bmp", path_out, terms=terms, iterations=iterations)
    assert os.path.exists(path_out)
    os.remove(path_out)


def test_load_image():
    result = load_image('images/test_3x3_gray.bmp')
    assert result.shape == (3, 3)

    assert result[0][0] == 79
    assert result[0][1] == 59
    assert result[0][2] == 0

    assert result[1][0] == 149
    assert result[1][1] == 119
    assert result[1][2] == 99

    assert result[2][0] == 254
    assert result[2][1] == 219
    assert result[2][2] == 199
