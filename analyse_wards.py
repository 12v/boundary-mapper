import csv
import os

ward_mapping_path = 'data/ONSPD_MAY_2023_UK/Documents/Ward names and codes UK as at 05_23.csv'

with (
    open('output/mapping.csv') as output_file,
    open(ward_mapping_path, encoding='utf-8-sig') as ward_mapping_file
):
    output = csv.DictReader(output_file)

    ward_mapping = csv.DictReader(ward_mapping_file)

    results_dict = {}

    for postcode in output:
        if postcode['ward'] not in results_dict:
            results_dict[postcode['ward']] = []

        if postcode['new_constituency_name'] not in results_dict[postcode['ward']]:
            results_dict[postcode['ward']].append(postcode['new_constituency_name'])

    ward_dict = {}
    
    for ward in ward_mapping:
        ward_dict[ward['WD23CD']] = ward['WD23NM']

    with(open('output/ward_results.csv', mode='w')) as ward_results_file:
        ward_results_writer = csv.writer(ward_results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ward_results_writer.writerow(['ward', 'constituency1', 'constituency2', 'constituency3'])

        for ward in results_dict:
            ward_results_writer.writerow([ward_dict[ward], *results_dict[ward]])
