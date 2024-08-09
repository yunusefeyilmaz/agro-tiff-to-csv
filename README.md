# GeoTIFF to CSV Converter

## Overview

This script converts GeoTIFF files to CSV format, suitable for use with QGIS. Each pixel value in the TIFF image is represented as a row in the resulting CSV file.

For converting CSV files to GeoTIFF format, refer to the ***[CSV to GeoTIFF Converter repository](https://github.com/yunusefeyilmaz/agro-csv-to-tiff)***.

## Features

- **GeoTIFF Compatibility**: Processes GeoTIFF files for use with QGIS.
- **CSV Conversion**: Converts pixel values to CSV format.
- **Error Handling**: Manages exceptions and skips invalid values.

## Installation

Ensure you have the required libraries installed:

```bash
pip install numpy tifffile
```

## Usage
### Command-Line Arguments
- --file (required): Path to the input GeoTIFF file.
- --output (optional): Path to the output CSV file. Defaults to output.

### Example Command
```bash
python tiff_to_csv.py --file input_geotiff.tiff --output output_file
```
