#  @classmethod
# def request(url, urllib2=None):
#         fh = urllib2.urlopen(url)
#         return cls.create(url=url, response=json.loads(fh.read()))
#
# #
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)

# url = "http://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
# df = geopandas.read_file(url)

import json
import os

import geopandas

from src.config import settings


def reload_fields():
    content = {"message": "reload success"}
    file_geojson = os.path.join(settings.FOLDER_DATA, settings.FILE_FIELDS)
    FILE_NAME_OUT = os.path.join(settings.FOLDER_DATA, 'fields_points.geojson')
    NAME_FIELD = 'name_ru'
    CRS = 4326      # WGS 84

    try:
        # with open(file_geojson, 'r', encoding="utf8") as f:
        #     data = json.load(f)
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        # print(gdf["name_ru"])
        # gdf = gdf.explode(ignore_index=True)
        # MultiPolygon to Polygon
        gdf = gdf.explode(column='geometry', ignore_index=True, index_parts=False)

        gdf = gdf.dissolve(by=NAME_FIELD, as_index=False)
        # gdf = gdf.convex_hull

        gdf['centroid'] = gdf.centroid
        # gdf_dissolve.to_file("qqq.geojson", driver='GeoJSON')

        gdf = gdf.to_crs(crs=CRS)

        gdf1 = gdf[[NAME_FIELD, 'centroid']]
        gdf1.set_geometry("centroid")
        # gdf1.rename_geometry('geom', inplace=True)
        gdf1 = gdf1.rename(columns={'centroid': 'geom'}).set_geometry('geom')

        # print(gdf1.geometry.name)
        print(gdf1)
        # gdf1.to_file("aaa.geojson", driver='GeoJSON')
        # gdf1.to_excel("aaa.xlsx")
        # gdf1.to_file('aaa.shp')
        gdf1.to_file(FILE_NAME_OUT, driver='GeoJSON')
        # print(data)
        # for feature in data:
        #     print(feature)
        #     if len(feature["features"]):
        #     #     # print(len(data["features"]))
        #         print(feature["properties"])
        # str_test = data["features"][0]["name_ru"]
        # print(str_test)



    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content
