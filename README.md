# boundary-mapper

## What is this?

This project creates a mapping between postcodes and the new proposed Westminster constituency electoral boundaries

## What assumptions have been made?

The mapping only includes English postcodes

The mapping only includes active postcodes (i.e. postcodes that haven't been terminated)

The mapping excludes postcodes that don't have corresponding grid references in the ONS data (an entry is added to `errors.csv` for these postcodes)

The mapping excludes postcodes that don't fall within an electoral boundary (an entry is added to `errors.csv` for these postcodes)

## How can I use the mapping?

The generated mapping can be found [here](https://github.com/hjmoss/boundary-mapper/raw/main/output.csv)

Check the errors [here](https://github.com/hjmoss/boundary-mapper/raw/main/errors.csv)

## How can I run this myself?

1. Clone the project
2. Install the dependencies (e.g. using miniconda)
3. Download and unzip the following source data files into a `data` directory within the project:
    1. [Postcode data from the ONS](https://www.arcgis.com/sharing/rest/content/items/bd25c421196b4546a7830e95ecdd70bc/data)
    2. [Proposed boundaries from the Boundary Commission](https://boundarycommissionforengland.independent.gov.uk/review2023/b65f7782-658b-4c4a-9cba-59c16c807f77/gis/2022_11_8_Revised_proposals_England_shp.zip)
3. Run `python analysis.py`
