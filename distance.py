import geopandas as gpd
from pandas import DataFrame


def create_distance_matrix(data_raw: DataFrame) -> DataFrame:
    geo_data = gpd.GeoDataFrame(
        data_raw[['Latitud', 'Longitud']],
        geometry=gpd.points_from_xy(data_raw['Latitud'], data_raw['Longitud']),
        crs='EPSG:4326'
    )
    distance = []
    for _, row in geo_data.iterrows():
        distance.append(geo_data['geometry'].distance(row['geometry']) * 100)

    return DataFrame(distance)
