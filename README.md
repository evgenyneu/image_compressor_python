# A Python image compression program

This a Python program I wrote for fun to practice linear algebra that I learned in Monash uni from Tim Garoni. The code uses singular value expansion method to reduce the size of an image.

## Setup

The program depends on `imageio` and `numpy` libraries for opening/saving image files. Here is how to install it:

```
pip install numpy
pip install imageio
```


## Creating a grayscale image

Run [make_grayscale.py](make_grayscale.py) to create a grayscale image.


## Testing

Install the `pytest` Python package

```
pip install pytest
```

and run the unit tests:

```
pytest
```

## The unlicense

This work is in [public domain](LICENSE).

