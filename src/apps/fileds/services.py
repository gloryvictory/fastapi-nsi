# with open(file_geojson, 'r', encoding="utf8") as f:
#     data = json.load(f)

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

from src.apps.fileds.models import Fields
from src.config import settings

# async def fields_create():

async def reload_fields():
    content = {"message": "reload success"}
    file_geojson = os.path.join(settings.FOLDER_DATA, settings.FILE_FIELDS)
    folder_geojson = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT)
    file_geojson_out = os.path.join(folder_geojson, 'fields_points.geojson')
    print(file_geojson_out)
    name_field = 'name_ru'
    crs_out = 4326      # WGS 84

    try:

        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        # MultiPolygon to Polygon
        gdf = gdf.explode(column='geometry', ignore_index=True, index_parts=False)
        # Объединяем два контура одного месторождения с одинаковым наименованием
        gdf = gdf.dissolve(by=name_field, as_index=False)
        # gdf = gdf.convex_hull
        gdf['centroid'] = gdf.centroid

        gdf = gdf.to_crs(crs=crs_out)

        gdf1 = gdf[[name_field, 'centroid']]
        gdf1.set_geometry("centroid")
        gdf1 = gdf1.rename(columns={'centroid': 'geom'}).set_geometry('geom')
        # print(gdf1.geometry.name)

        # gdf1.to_file("test.geojson", driver='GeoJSON')
        # gdf1.to_excel("test.xlsx")
        # gdf1.to_file('test.shp')
        gdf1.to_file(file_geojson_out, driver='GeoJSON')
        for i in range(0, len(gdf1)):
            gdf1.loc[i, 'lon'] = gdf1.geometry.centroid.x.iloc[i]
            gdf1.loc[i, 'lat'] = gdf1.geometry.centroid.y.iloc[i]

        print(gdf1)

        # fields_table = Fields()
        for i in range(0, len(gdf1)):

            # fields_table.name_ru = gdf1.loc[i, 'name_ru']
            # fields_table.lon = gdf1.loc[i, 'lon']
            # fields_table.lat = gdf1.loc[i, 'lat']
            fields_table = await Fields.objects.create(
                name_ru=gdf1.loc[i, 'name_ru'],
                lon=gdf1.loc[i, 'lon'],
                lat=gdf1.loc[i, 'lat']
            )
            await fields_table.save()
            print(gdf1.loc[i, 'name_ru'])
            # print(gdf1.loc[i, 'lon'])
            # print(gdf1.loc[i, 'lat'])
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
