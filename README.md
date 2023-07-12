# Postcode to updated Westminster constituency converter

## How can I use the converter?

A simple UI is available [here](https://12v.github.io/boundary-mapper/).

The generated conversion file, `output/mapping.csv`, can be found [here](https://github.com/12v/boundary-mapper/raw/main/output/mapping.csv).

**Caveat**: `output/mapping.csv` contains >1.7 million rows, Microsoft Excel can't display this many rows and will truncate the dataset.

Check the errors [here](https://github.com/12v/boundary-mapper/raw/main/output/errors.csv).

## What is this?

This project creates a mapping to convert between postcodes and the proposed Westminster constituency electoral boundaries from the 2023 reviews of the [English](https://boundarycommissionforengland.independent.gov.uk/2023-review/), [Scottish](https://www.bcomm-scotland.independent.gov.uk/reviews/2023-review-uk-parliament-constituencies), and [Welsh](https://bcomm-wales.gov.uk/reviews/06-23/2023-parliamentary-review-final-recommendations) boundary commissions.

## What assumptions have been made?

The mapping only includes English, Scottish, and Welsh postcodes.

The mapping only includes active postcodes (i.e. postcodes that haven't been terminated).

The mapping excludes postcodes that don't have corresponding grid references in the ONS data (an entry is added to `output/errors.csv` for these postcodes).

The mapping excludes postcodes that don't fall within an electoral boundary (an entry is added to `output/errors.csv` for these postcodes).

## How can I run this myself?

1. Clone the project
2. Install the dependencies (e.g. using miniconda)
3. Download and unzip the following source data files into a `data` directory within the project:
    1. [May 2023 Postcode data from the ONS](https://www.arcgis.com/sharing/rest/content/items/bd25c421196b4546a7830e95ecdd70bc/data) (from [here](https://geoportal.statistics.gov.uk/datasets/ons-postcode-directory-may-2023/about))
    2. [Final recommended boundaries from the English Boundary Commission](https://boundarycommissionforengland.independent.gov.uk/wp-content/uploads/2023/06/984162_2023_06_27_Final_recommendations_England_shp.zip)
    3. [Final recommended boundaries from the Scottish Boundary Commission](https://www.bcomm-scotland.independent.gov.uk/sites/default/files/2023_review_final/bcs_final_recs_2023_review.zip)
    4. [Final recommended boundaries from the Welsh Boundary Commission](https://bcomm-wales.gov.uk/sites/bcomm/files/review/Shapefiles.zip)
3. Run `python generate_mapping.py`
