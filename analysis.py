import fiona
import csv
from shapely.geometry import shape
from shapely import Point

COORDINATE_ERROR = 'No coordinates found for postcode'
CONSTITUENCY_ERROR = 'No constituency found for postcode'

shapefile_path = "data/2022_11_8_Revised_proposals_England_shp/2022_11_8_Revised_proposals_England.shp"
old_constituency_id_mapping_path = 'data/ONSPD_MAY_2023_UK/Documents/Westminster Parliamentary Constituency names and codes UK as at 12_14.csv'
postcode_directory_path = 'data/ONSPD_MAY_2023_UK/Data/ONSPD_MAY_2023_UK.csv'

constituencies = []
with fiona.open(shapefile_path) as boundaries:
    constituencies = [
        (constituency.properties['Constituen'], shape(constituency['geometry']))
        for constituency in iter(boundaries)
    ]

old_constituency_ids_dict = {}
with open(old_constituency_id_mapping_path, encoding='utf-8-sig') as old_id_file:
    old_ids = csv.DictReader(old_id_file)
    old_constituency_ids_dict = {old_id['PCON14CD']: old_id['PCON14NM'] for old_id in old_ids}

postcode_count = sum(1 for _ in open(postcode_directory_path))

with (
    open('output.csv', mode='w') as output_file,
    open(postcode_directory_path) as postcodes_file,
    open('errors.csv', mode='w') as error_file
):
    output_fieldnames = [
        'postcode',
        'old_constituency_id',
        'old_constituency_name',
        'new_constituency_name'
    ]
    error_fieldnames = ['postcode', 'message']

    output_writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
    output_writer.writeheader()

    error_writer = csv.DictWriter(error_file, fieldnames=error_fieldnames)
    error_writer.writeheader()

    postcodes = csv.DictReader(postcodes_file)
    for i, postcode in enumerate(postcodes):
        if i % 10000 == 0:
            print(str(i) + " of " + str(postcode_count) + ", " + "{:.1f}%".format(100*i/postcode_count))

        if postcode['ctry'] != 'E92000001':
            continue

        if postcode['doterm'] != '':
            continue

        if postcode['oseast1m'] == '' or postcode['osnrth1m'] == '':
            print(", ".join([postcode['pcd'], COORDINATE_ERROR]))
            error_writer.writerow({
                error_fieldnames[0]: postcode['pcd'],
                error_fieldnames[1]: COORDINATE_ERROR
            })
            continue

        point = Point(int(postcode['oseast1m']), int(postcode['osnrth1m']))

        match = ''

        for constituency_name, constituency_shape in constituencies:
            if point.within(constituency_shape):
                match = constituency_name
                break
        
        if match == '':
            print(", ".join([postcode['pcd'], CONSTITUENCY_ERROR]))
            error_writer.writerow({
                error_fieldnames[0]: postcode['pcd'],
                error_fieldnames[1]: CONSTITUENCY_ERROR
            })
        else:
            # print(", ".join([postcode['pcd'],  postcode['pcon'], match]))
            output_writer.writerow({
                output_fieldnames[0]: postcode['pcd'],
                output_fieldnames[1]: postcode['pcon'],
                output_fieldnames[2]: old_constituency_ids_dict[postcode['pcon']],
                output_fieldnames[3]: match
            })
