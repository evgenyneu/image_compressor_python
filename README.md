# A Python image compression program

This is a Python program I wrote for fun to apply linear algebra theory I learned in Monash uni. The code uses singular value expansion method to reduce the size of an image.

## Setup

First, [install Python](https://www.python.org/downloads/). Next, install dependencies:

```
pip install numpy
pip install imageio
```

Finally, download this source code:

```
git clone https://github.com/evgenyneu/image_compressor_python.git
```

## Usage

Compress an image file `image.jpg` using ten terms of the singular value expansion:

```
python src/compress.py image.jpg --terms=10
```


### Available options


```
  -h, --help            show this help message and exit
  --output OUTPUT       path to the compressed image that will be created
  --terms TERMS         number of terms in the singular value expansion
  --iterations ITERATIONS
                        number of iterations of the power method
  --notext              do not put text on the image
```

### Compress all images in a directory

This following program allows to compress many images with different quality all at once. This can be useful for comparing many different outcomes and see how the `terms` setting affects image quality:

```
$ python src/process_samples.py INPUT_DIR OUTPUT_DIR
```

Replace `INPUT_DIR` with the name of directory that contains images you want to compress, in JPG, PNG or BMP format. All images in the directory will be compressed.

Replace `OUTPUT_DIR` with a name of the directory where you want compressed images to be placed.


#### Example

This example uses the images from `images/for_compression` directory:

```
$ python src/process_samples.py images/for_compression images/compressed/

Creating images:
images/compressed/100x100/marmite_100x100_1_terms_49.8x_compression.jpg
images/compressed/100x100/marmite_100x100_2_terms_24.9x_compression.jpg
images/compressed/100x100/marmite_100x100_5_terms_10.0x_compression.jpg
images/compressed/100x100/marmite_100x100_10_terms_5.0x_compression.jpg
images/compressed/100x100/marmite_100x100_20_terms_2.5x_compression.jpg
```

## Compression results

The program produced the following compressed images featuring my cat Marmite. The image size are 1000 by 1000 pixels. The compression results for images of different sizes are located [here](images/compressed).

![1 term compression](images/compressed/1000x1000/marmite_1000x1000_1_terms_499.8x_compression.jpg)

![2 term compression](images/compressed/1000x1000/marmite_1000x1000_2_terms_249.9x_compression.jpg)

![5 term compression](images/compressed/1000x1000/marmite_1000x1000_5_terms_100.0x_compression.jpg)

![10 term compression](images/compressed/1000x1000/marmite_1000x1000_10_terms_50.0x_compression.jpg)

![20 term compression](images/compressed/1000x1000/marmite_1000x1000_20_terms_25.0x_compression.jpg)

![50 term compression](images/compressed/1000x1000/marmite_1000x1000_50_terms_10.0x_compression.jpg)

![100 term compression](images/compressed/1000x1000/marmite_1000x1000_100_terms_5.0x_compression.jpg)

![150 term compression](images/compressed/1000x1000/marmite_1000x1000_150_terms_3.3x_compression.jpg)

![200 term compression](images/compressed/1000x1000/marmite_1000x1000_200_terms_2.5x_compression.jpg)

![300 term compression](images/compressed/1000x1000/marmite_1000x1000_300_terms_1.7x_compression.jpg)

![500 term compression](images/compressed/1000x1000/marmite_1000x1000_500_terms_1.0x_compression.jpg)

### Original uncompressed image

![Uncompressed image](images/for_compression/marmite_1000x1000.jpg)



## Run unit tests

Install `pytest`

```
pip install pytest
```

and run the unit tests:

```
pytest
```


## The unlicense

This work is in [public domain](LICENSE).

