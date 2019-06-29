# A Python image compression program

This a Python program I wrote for fun to practice linear algebra. It uses singular value expansion method to reduce the size of an image.

## Setup

THe program depends on `imageio` and `numpy` libraries for opening/saving image files. Here is how to install it:

Conda:

```
conda install -c conda-forge imageio
```


Pip:

```
pip install imageio
```


## Creating a grayscale image

Run [make_grayscale.py](make_grayscale.py) to create a grayscale image.


## Testing

Install the `pytest` Python package and run the unit tests:

```
pytest
```

## The unlicense

This work is in [public domain](LICENSE).

