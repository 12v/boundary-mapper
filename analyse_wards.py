import csv

ward_names_and_codes_path = 'data/postcodes/Documents/Ward names and codes UK as at 05_23.csv'

with (
    open('output/postcode_to_constituency_mapping.csv') as output_file,
    open(ward_names_and_codes_path, encoding='utf-8-sig') as ward_names_and_codes_file
):
    output = csv.DictReader(output_file)

    ward_names_and_codes = csv.DictReader(ward_names_and_codes_file)

    ward_codes_to_names = {}
    
    for ward in ward_names_and_codes:
        ward_codes_to_names[ward['WD23CD']] = ward['WD23NM']

    wards_dict = {}
    constituencies_dict = {}

    for postcode in output:
        ward = postcode['ward']
        constituency = postcode['new_constituency_name']

        if ward not in wards_dict:
            wards_dict[ward] = {}

        if constituency not in wards_dict[ward]:
            wards_dict[ward][constituency] = 0
        
        wards_dict[ward][constituency] += 1


        if constituency not in constituencies_dict:
            constituencies_dict[constituency] = {}
        
        if ward not in constituencies_dict[constituency]:
            constituencies_dict[constituency][ward] = 0
        
        constituencies_dict[constituency][ward] += 1


    with(open('output/ward_to_constituencies_mapping.csv', mode='w')) as ward_results_file:
        ward_results_writer = csv.writer(ward_results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        ward_with_most_constituencies = max(wards_dict.values(), key=lambda x: len(x))
        max_constituency_count = len(ward_with_most_constituencies)

        header_row = ['wardId', 'ward']

        for i in range(max_constituency_count):
            header_row.append(f'constituency{i+1}')
            header_row.append(f'#postcodes{i+1}')

        ward_results_writer.writerow(header_row)

        for ward in sorted(wards_dict):
            row = [ward, ward_codes_to_names[ward]]
            constituencies = wards_dict[ward]
            for constituency in sorted(constituencies, key=constituencies.get, reverse=True):
                row.append(constituency)
                row.append(constituencies[constituency])
            ward_results_writer.writerow(row)

    with(open('output/constituency_to_wards_mapping.csv', mode='w')) as constituency_results_file:
        constituency_results_writer = csv.writer(constituency_results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        constituency_with_most_wards = max(constituencies_dict.values(), key=lambda x: len(x))
        max_ward_count = len(constituency_with_most_wards)

        header_row = ['constituency']

        for i in range(max_ward_count):
            header_row.append(f'ward{i+1}')
            header_row.append(f'#postcodes{i+1}')
        
        constituency_results_writer.writerow(header_row)

        for constituency in sorted(constituencies_dict):
            row = [constituency]
            wards = constituencies_dict[constituency]
            for ward in sorted(wards, key=wards.get, reverse=True):
                row.append(ward)
                row.append(wards[ward])
            constituency_results_writer.writerow(row)
