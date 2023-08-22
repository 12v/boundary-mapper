import csv

with (
    open('output/postcode_to_constituency_mapping.csv') as output_file
):
    output = csv.DictReader(output_file)

    sector_dict = {}

    for postcode in output:
        sector = postcode['postcode'][:-2]

        constituency = postcode['new_constituency_name']

        if sector not in sector_dict:
            sector_dict[sector] = []

        if constituency not in sector_dict[sector]:
            sector_dict[sector].append(constituency)

    ambiguous_sectors = [sector for sector in sector_dict if len(sector_dict[sector]) > 1]
    unambiguous_sectors = [sector for sector in sector_dict if len(sector_dict[sector]) == 1]

    ambiguous_sector_count = len(ambiguous_sectors)
    unambiguous_sector_count = len(unambiguous_sectors)

    print(unambiguous_sector_count / (ambiguous_sector_count + unambiguous_sector_count))
