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

import os
import hashlib
import geopandas


from src.apps.fileds.models import Fields
from src.config import settings
from src.config.log import set_logger
import rasterio.warp
from shapely.geometry import shape



async def reload_fields():
    content = {"msg": "reload success"}
    file_geojson = os.path.join(os.getcwd(), settings.FOLDER_DATA, settings.FIELDS_FILE_GEOJSON_IN)
    # folder_geojson = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT)
    file_geojson_out = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT, settings.FIELDS_FILE_GEOJSON_OUT)
    name_field = settings.FIELDS_NAME_FIELD # 'name_ru'
    crs_out = settings.CRS_OUT

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
        # gdf1.geometry.to_crs(crs=crs_out)
        # geometry = rasterio.warp.transform_geom(
        #     src_crs=4326,
        #     dst_crs=crs_out,
        #     geom=gdf1.geometry.values,
        # )
        # mercator_world = gdf1.set_geometry(
        #     [shape(geom) for geom in geometry],
        #     crs=crs_out,
        # )
        # print(gdf1)
        # print(gdf1.geometry.crs)
        log = set_logger()
        log.info(gdf1)

        await Fields.objects.delete(each=True)

        for i in range(0, len(gdf1)):
            str_name = str(gdf1.loc[i, 'name_ru']).encode()
            hash_object = hashlib.md5(str_name)
            hash_md5 = hash_object.hexdigest()
            fields_table = Fields(
                name_ru=str_name,
                lon=gdf1.loc[i, 'lon'],
                lat=gdf1.loc[i, 'lat'],
                crs=crs_out,
                hash=hash_md5,
            )
            # await fields_table.save()
            await fields_table.upsert()
            # print(gdf1.loc[i, 'name_ru'])

    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content
