# boundary-mapper

## What is this?

This project creates a mapping between postcodes and the proposed Westminster constituency electoral boundaries from the [Boundary Commission's 2023 review](https://boundarycommissionforengland.independent.gov.uk/2023-review/).

## What assumptions have been made?

The mapping only includes English postcodes.

The mapping only includes active postcodes (i.e. postcodes that haven't been terminated).

The mapping excludes postcodes that don't have corresponding grid references in the ONS data (an entry is added to `output/errors.csv` for these postcodes).

The mapping excludes postcodes that don't fall within an electoral boundary (an entry is added to `output/errors.csv` for these postcodes).

## How can I use the mapping?

The generated mapping file, `output/mapping.csv`, can be found [here](https://github.com/hjmoss/boundary-mapper/raw/main/output/mapping.csv).

**Caveat**: `output/mapping.csv` contains ~1.5 million rows, Microsoft Excel can't display this many rows and will truncate the dataset.

Check the errors [here](https://github.com/hjmoss/boundary-mapper/raw/main/output/errors.csv).

## How can I run this myself?

1. Clone the project
2. Install the dependencies (e.g. using miniconda)
3. Download and unzip the following source data files into a `data` directory within the project:
    1. [May 2023 Postcode data from the ONS](https://www.arcgis.com/sharing/rest/content/items/bd25c421196b4546a7830e95ecdd70bc/data) (from [here](https://geoportal.statistics.gov.uk/datasets/ons-postcode-directory-may-2023/about))
    2. [Final recommended boundaries from the Boundary Commission](https://boundarycommissionforengland.independent.gov.uk/wp-content/uploads/2023/06/984162_2023_06_27_Final_recommendations_England_shp.zip) (from [here](https://boundarycommissionforengland.independent.gov.uk/2023-review/))
3. Run `python generate_mapping.py`
