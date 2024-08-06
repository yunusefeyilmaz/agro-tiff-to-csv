import pandas as pd
import numpy as np
from PIL import Image, ImageOps
import argparse

class TIFFToCSVConverter:
    def __init__(self, file, output, colored):
        self.file = file
        self.output = output
        self.colored = colored

    def convert(self):
        # Open the TIFF file
        img = Image.open(self.file)
        
        # Convert image to grayscale if it's not already and if colored is False
        if not self.colored and img.mode != 'L':
            img = ImageOps.grayscale(img)
        
        # Convert image data to numpy array
        img_data = np.array(img)

        # Get the dimensions of the image
        height, width = img_data.shape[:2]

        # Create a list to store the pixel data
        data = []

        # Convert the image data to the desired CSV format
        for y in range(height):
            for x in range(width):
                if img_data[y, x] != 0:  # Only include non-zero values
                    idx = y * width + x
                    if self.colored:
                        classId = img_data[y, x].tolist()  # For colored images, store RGB values
                    else:
                        classId = img_data[y, x]
                    data.append([idx, classId])

        # Create a DataFrame from the data
        df = pd.DataFrame(data, columns=['idx', 'classId'])

        # Save the DataFrame to a CSV file
        df.to_csv(self.output + '.csv', index=False)

def main():
    # Read args from command line
    parser = argparse.ArgumentParser(description='Convert TIFF to CSV')
    parser.add_argument('--file', type=str, required=True, help='TIFF file to convert')
    parser.add_argument('--output', type=str, default='outputCSV', help='Output CSV file name')
    parser.add_argument('--colored', action='store_true', help='Keep the image colored')

    args = parser.parse_args()

    converter = TIFFToCSVConverter(file=args.file, output=args.output, colored=args.colored)
    converter.convert()

if __name__ == '__main__':
    main()