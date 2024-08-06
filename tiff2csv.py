import pandas as pd
import numpy as np
from PIL import Image, ImageOps
import argparse
import csv

class TIFFToCSVConverter:
    def __init__(self, file, output):
        """
        Initialize the converter with the input TIFF file and output CSV file name.
        
        :param file: Path to the input TIFF file.
        :param output: Path to the output CSV file.
        """
        self.file = file
        self.output = output

    def convert(self):
        """
        Convert the TIFF file to a CSV file.
        """
        try:
            # Open the TIFF file
            img = Image.open(self.file)
            
            # Convert image to grayscale if it's not already
            if img.mode != 'L':
                img = ImageOps.grayscale(img)
            
            # Convert image data to numpy array
            img_data = np.array(img)

            # Get the dimensions of the image
            height, width = img_data.shape

            # Open the output CSV file
            with open(self.output + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['idx', 'classId'])

                # Convert the image data to the desired CSV format
                non_zero_indices = np.argwhere(img_data != 0)
                for y, x in non_zero_indices:
                    idx = y * width + x
                    classId = img_data[y, x]
                    writer.writerow([idx, classId])
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """
    Main function to parse command line arguments and initiate the conversion.
    """
    # Read args from command line
    parser = argparse.ArgumentParser(description='Convert TIFF to CSV')
    parser.add_argument('--file', type=str, required=True, help='TIFF file to convert')
    parser.add_argument('--output', type=str, default='output', help='Output CSV file name')

    args = parser.parse_args()

    converter = TIFFToCSVConverter(file=args.file, output=args.output)
    converter.convert()

if __name__ == '__main__':
    main()