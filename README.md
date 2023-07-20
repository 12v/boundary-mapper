# Convert postcodes to updated Westminster constituencies

## What is this?

This project creates a mapping to convert between postcodes and the proposed Westminster constituency electoral boundaries from the 2023 reviews of the [English](https://boundarycommissionforengland.independent.gov.uk/2023-review/), [Scottish](https://www.bcomm-scotland.independent.gov.uk/reviews/2023-review-uk-parliament-constituencies), and [Welsh](https://bcomm-wales.gov.uk/reviews/06-23/2023-parliamentary-review-final-recommendations) boundary commissions.

This project also creates mappings from wards to constituencies, and from constituencies to wards.

## How can I use the converter?

In addition to using the underlying mapping CSV files directly, a simple UI for conerting postcodes into their corresponing constituencies is available [here](https://12v.github.io/boundary-mapper/).

The generated conversion file mapping postcodes to new Westminster constituencies, `output/postcode_to_constituency_mapping.csv`, can be found [here](https://github.com/12v/boundary-mapper/blob/main/output/postcode_to_constituency_mapping.csv).

A mapping of wards to new Westminster constituencies,  `output/ward_to_constituencies_mapping.csv`,  can be found [here](https://github.com/12v/boundary-mapper/blob/main/output/ward_to_constituencies_mapping.csv).

A mapping of new Westminster constituencies to wards,  `output/constituency_to_wards_mapping.csv`,  can be found [here](https://github.com/12v/boundary-mapper/blob/main/output/constituency_to_wards_mapping.csv).

**Caveat**: `output/postcode_to_constituency_mapping.csv` contains >1.7 million rows, Microsoft Excel can't display this many rows and will truncate the dataset.

Check the errors [here](https://github.com/12v/boundary-mapper/blob/main/output/errors.csv).

## What assumptions have been made?

The mapping only includes English, Scottish, and Welsh postcodes, as shapefiles for the Northern Ireland constituencies have not been published.

The mapping only includes active postcodes (i.e. postcodes that haven't been terminated).

The mapping excludes postcodes that don't have corresponding grid references in the ONS data (an entry is added to `output/errors.csv` for these postcodes).

The mapping excludes postcodes that don't fall within an electoral boundary (an entry is added to `output/errors.csv` for these postcodes).

## How can I run this myself?

1. Clone the project
2. Install the dependencies (e.g. using miniconda)
3. Run `python analyse_postcodes.py`
4. (Optional) To generate the ward-constituency and constituency-ward mappings, run `python analyse_wards.py`
    1. N.B. this requires step 3 to have been run already
