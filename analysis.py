import fiona
import csv
from shapely.geometry import shape
from shapely import Point

shapefile_path = "./2022_11_8_Revised_proposals_England_shp/2022_11_8_Revised_proposals_England.shp"
boundaries = fiona.open(shapefile_path)

constituency_dict = {}

for constituency in iter(boundaries):
    constituency_dict[constituency.properties['Constituen']] = shape(constituency['geometry'])

constituency_dict_items = constituency_dict.items()

old_ids_dict = {}

with open('./ONSPD_MAY_2023_UK/Documents/Westminster Parliamentary Constituency names and codes UK as at 12_14.csv', newline='') as old_id_file:
    old_ids = csv.DictReader(old_id_file, delimiter=',')
    for old_id in old_ids:
        old_ids_dict[old_id['\ufeffPCON14CD']] = old_id['PCON14NM']

with open('output.csv', 'w', newline='') as output_file:
    fieldnames = ['postcode', 'old_constituency_id', 'old_constituency_name', 'new_constituency_name']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    with open('./ONSPD_MAY_2023_UK/Data/ONSPD_MAY_2023_UK.csv', newline='') as postcodes_file:
        postcodes = csv.DictReader(postcodes_file, delimiter=',')
        i = 0
        for postcode in postcodes:
            if postcode['ctry'] != 'E92000001':
                continue

            if postcode['oseast1m'] == '' or postcode['osnrth1m'] == '':
                continue

            i += 1

            point = Point(int(postcode['oseast1m']), int(postcode['osnrth1m']))

            match = ''

            for constituency_name, constituency_shape in constituency_dict_items:
                if point.within(constituency_shape):
                    match = constituency_name
                    break
                
                continue

            if i % 10000 == 0:
                print(i)
            
            if match == '':
                print(postcode['pcd'], 'No constituency found')
            else:
                # print(", ".join([postcode['pcd'],  postcode['pcon'], match]))
                writer.writerow({fieldnames[0]: postcode['pcd'], fieldnames[1]: postcode['pcon'], fieldnames[2]: old_ids_dict[postcode['pcon']], fieldnames[3]: match})
