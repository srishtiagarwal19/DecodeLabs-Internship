# Project 4: OCR Text Recognition

## Objective

Build an Optical Character Recognition (OCR) system capable of extracting text from images using Python, OpenCV, and Tesseract OCR.

## Technologies Used

* Python
* OpenCV
* Tesseract OCR
* Pytesseract

## Features

* Image preprocessing using grayscale conversion
* Noise reduction using Gaussian Blur
* Otsu thresholding
* Text extraction using OCR
* Bounding box generation around detected words
* Confidence score calculation
* Export extracted text to a file

## Input

An image containing text.

## Output

* Extracted text displayed in terminal
* Bounding boxes around detected words
* Confidence scores for each detected word
* Saved text file (`output.txt`)
* Processed image (`processed.jpg`)

## Sample Result

Detected Text:

ARTIFICIAL INTELLIGENCE
PROJECT 4
HELLO WORLD

Average OCR Confidence: 95%+

## Conclusion

The OCR system successfully extracts text from images with high accuracy and demonstrates the use of image preprocessing and machine learning-based text recognition.
