# QGIS Python Scripts for Archaeology

This repository houses Python scripts intended for use within QGIS and the Archaeology sector.

## ArchDensity

### Description

The `ArchDensity` script calculates the total area in square meters of archaeological features within a specified excavation area. Additionally, it computes the density of these features within the excavation zone, excluding any invalid geometries during calculation.

### Usage

To utilize the `ArchDensity` script:

1. Open QGIS and access the Python Console.
2. Copy and paste the script into the console or save it as a Python file in the QGIS Python directory.
3. Ensure the necessary QGIS processing modules are installed.
4. Execute the script and provide inputs for the Excavation Area and Archaeology Area.

### Dependencies

- QGIS (version X.X or later)
- PyQt5 (QGIS-compatible version)

## Transect Generator

### Description

The `Transect Generator` script creates transects within a defined polygon area based on specified intervals and directions. It generates lines that intersect with the polygon layer, creating transects suitable for archaeological surveys or land analysis.

### Usage

To generate transects using the script:

1. Load the polygon layer defining the area in QGIS.
2. Ensure the script is accessible within the QGIS Python environment.
3. Invoke the `generate_transects` function and provide the required parameters: polygon layer name, interval distance, and direction.

### Dependencies

- QGIS (version X.X or later)
- PyQt5 (QGIS-compatible version)

## Example Usage

Here's an example of how to generate transects:

```python
generate_transects("ExcavationArea", 10, "N-S")
```
