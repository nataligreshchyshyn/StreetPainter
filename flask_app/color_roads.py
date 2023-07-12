from azimuth_calculator import AzimuthCalculator
import matplotlib.pyplot as plt
import math
import random
import pandas as pd
import geopandas as gpd
from shapely.geometry import MultiLineString
from shapely.ops import linemerge
import matplotlib
matplotlib.use('Agg')


def get_line_coords(linestring):
    coords = linestring.coords
    start = coords[0]
    end = coords[-1]
    lat1, lon1 = start[1], start[0]
    lat2, lon2 = end[1], end[0]
    return lat1, lon1, lat2, lon2


def get_azimuth(line):
    lat1, lon1, lat2, lon2 = get_line_coords(line)
    calc = AzimuthCalculator(lat1, lon1, lat2, lon2)
    azimuth = calc.calculate_azimuth()
    return azimuth


def assign_azimuth_group(azimuth):
    group = math.floor(azimuth / 30)
    return group


def merge_lines_on_azimuth(gdf):
    grouped_geometries = []
    grouped = gdf.groupby('azimuth_group')

    for group_num, group_df in grouped:
        merged_line = linemerge(list(group_df['geometry']))

        if isinstance(merged_line, MultiLineString):
            for line in merged_line.geoms:
                grouped_geometries.append(line)
        else:
            grouped_geometries.append(merged_line)
    return grouped_geometries


def main(filepath):
    roads = gpd.read_file(filepath)
    roads['azimuth'] = roads['geometry'].apply(get_azimuth)
    roads['azimuth_group'] = roads['azimuth'].apply(assign_azimuth_group)
    grouped_geometries = merge_lines_on_azimuth(roads)
    gdf_grouped = gpd.GeoDataFrame(geometry=grouped_geometries)
    colors = ['red', 'green', 'blue', 'yellow', 'orange',
              'purple', 'cyan', 'magenta', 'lime', 'pink']
    random_colors = [random.choice(colors) for _ in range(len(gdf_grouped))]
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf_grouped.plot(ax=ax, color=random_colors)
    plt.savefig('static/images/result.png', bbox_inches='tight')
    return 'static/images/result.png'
