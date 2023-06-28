import fiona
import csv
from shapely.geometry import shape
from shapely import Point
from shapely.validation import make_valid
from rtree import index
import os

COORDINATE_ERROR = 'No coordinates found for postcode'
CONSTITUENCY_ERROR = 'No constituency found for postcode'

shapefile_path = 'data/984162_2023_06_27_Final_recommendations_England_shp/2023_06_27_Final_recommendations_England.shp'
old_constituency_id_mapping_path = 'data/ONSPD_MAY_2023_UK/Documents/Westminster Parliamentary Constituency names and codes UK as at 12_14.csv'
postcode_directory_path = 'data/ONSPD_MAY_2023_UK/Data/ONSPD_MAY_2023_UK.csv'

constituencies = []
r_tree = index.Index()
with fiona.open(shapefile_path) as boundaries:
    for i, constituency in enumerate(boundaries):
        constituency_shape = make_valid(shape(constituency['geometry']))
        constituencies.append((constituency.properties['Constituen'], constituency_shape))
        r_tree.insert(i, constituency_shape.bounds)

old_constituency_ids_dict = {}
with open(old_constituency_id_mapping_path, encoding='utf-8-sig') as old_id_file:
    old_ids = csv.DictReader(old_id_file)
    old_constituency_ids_dict = {old_id['PCON14CD']: old_id['PCON14NM'] for old_id in old_ids}

postcode_count = sum(1 for _ in open(postcode_directory_path)) - 1

if not os.path.exists('output'):
    os.makedirs('output')

with (
    open(postcode_directory_path) as postcodes_file,
    open('output/mapping.csv', mode='w') as output_file,
    open('output/errors.csv', mode='w') as error_file
):
    output_fieldnames = [
        'postcode',
        'old_constituency_id',
        'old_constituency_name',
        'new_constituency_name'
    ]
    error_fieldnames = ['postcode', 'message']

    postcodes = csv.DictReader(postcodes_file)

    output_writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
    output_writer.writeheader()

    error_writer = csv.DictWriter(error_file, fieldnames=error_fieldnames)
    error_writer.writeheader()

    for i, postcode in enumerate(postcodes):
        if i % 10000 == 0:
            print(str(i) + ' of ' + str(postcode_count) + ', ' + '{:.1f}%'.format(100*i/postcode_count))

        if postcode['ctry'] != 'E92000001':
            continue

        if postcode['doterm'] != '':
            continue

        if postcode['oseast1m'] == '' or postcode['osnrth1m'] == '':
            print(', '.join([postcode['pcd'], COORDINATE_ERROR]))
            error_writer.writerow({
                error_fieldnames[0]: postcode['pcd'],
                error_fieldnames[1]: COORDINATE_ERROR
            })
            continue

        point = Point(int(postcode['oseast1m']), int(postcode['osnrth1m']))

        match = ''
        
        for candidateIndex in r_tree.intersection(point.bounds):
            constituency_name, constituency_shape = constituencies[candidateIndex]
            if point.within(constituency_shape):
                match = constituency_name
                break
        
        if match == '':
            print(', '.join([postcode['pcd'], CONSTITUENCY_ERROR]))
            error_writer.writerow({
                error_fieldnames[0]: postcode['pcd'],
                error_fieldnames[1]: CONSTITUENCY_ERROR
            })
        else:
            output_writer.writerow({
                output_fieldnames[0]: postcode['pcd'],
                output_fieldnames[1]: postcode['pcon'],
                output_fieldnames[2]: old_constituency_ids_dict[postcode['pcon']],
                output_fieldnames[3]: match
            })
