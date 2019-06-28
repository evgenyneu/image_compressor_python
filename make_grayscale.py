import imageio
import numpy as np

# Makes a grayscale image from a colored one
image = imageio.imread('marmite_500x500.bmp')
rgb = np.array(image)

r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
gray = gray.astype(np.uint8)
imageio.imwrite('marmite_500x500_gray.bmp', gray)