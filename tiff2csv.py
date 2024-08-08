import numpy as np
from PIL import Image
import csv
import argparse
import os
import sys

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
            img = np.array(img)


            # Get the dimensions of the image
            height, width = img.shape

            if self.output.endswith('.csv'):
                self.output = self.output[:-4]

            # if output exists, delete it
            try:
                os.remove(self.output + '.csv')
            except FileNotFoundError:
                pass

            # Open the output CSV file
            with open(self.output + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['idx', 'classId'])

                # Convert the image data to the desired CSV format
                for y in range(height):
                    for x in range(width):
                        classId = img[y, x]
                        if classId != 0.0:  # Skip 0.0 values
                            idx = y * width + x
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