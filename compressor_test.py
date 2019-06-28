from compressor import load_image


def test_load_image():
    result = load_image('marmite_500x500_gray.bmp')
    assert result.shape == (500, 500)
