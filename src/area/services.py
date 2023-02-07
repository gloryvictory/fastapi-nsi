import json
import os
import hashlib
from typing import Any

import geopandas
from src.models import AREA
from src import settings
from src.log import set_logger


async def area_reload():
    content = {"msg": "Fail"}
    file_geojson = os.path.join(settings.FOLDER_BASE, settings.FOLDER_DATA, settings.WELL_FILE_GEOJSON_IN)
    name_area = settings.WELL_NAME_AREA_FIELD
    crs_out = settings.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        gdf1 = gdf.to_crs(crs=crs_out)

        log = set_logger(settings.WELL_FILE_LOG)

        await AREA.objects.delete(each=True)

        # cnt_all = len(gdf1)

        gdf_area = gdf1['pl'].unique()

        log.info(gdf_area)
        cnt_areas = len(gdf_area)

        # cnt_areas = len(gdf1['pl'].unique())
        print(f"Count of AREAS : {cnt_areas}")

        # for i in range(0, cnt_areas):
        #     print(f"{i}  of {cnt_areas}")
        #     # str_name_area = str(gdf1.loc[i, name_area]).encode()
        #     str_name_area = str(gdf_area.loc[i, name_area])
        #     hash_object = hashlib.md5(str_name_area.encode())
        #     hash_md5 = hash_object.hexdigest()
        #
        #     d_lon = gdf_area.geometry.x.iloc[i]
        #     d_lat = gdf_area.geometry.y.iloc[i]
        #
        #     area_table = AREA(
        #         name_ru=str_name_area,
        #         lon=d_lon,
        #         lat=d_lat,
        #         crs=crs_out,
        #         hash=hash_md5
        #     )
        #     await area_table.upsert()
        #
        #     log.info(f"pl: {str_name_area}")
        #
        # count = await AREA.objects.count()
        #
        # content = {"msg": "Success", "count": count}
        # log.info(f"Total ngo count {count}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content


async def area_get_all():
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.WELL_FILE_LOG)

    try:
        area_all = await AREA.objects.all()

        log.info("wells load successfully")
        return area_all
    except Exception as e:
        content = {"msg": f"reload fail. can't read ngo from database {AREA.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


async def area_get_all_count() -> dict[str, str | Any] | dict[str, str]:
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.WELL_FILE_LOG)

    try:
        # table_exist = ngo.
        area_all_count = await AREA.objects.count()

        log.info(f"ngo count load successfuly: {area_all_count}")
        content = {"msg": "Success", "count": area_all_count}
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't read count of ngo from database {AREA.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content

# async def area_get_geojson_file():
#     content = {"msg": "Success"}
#     file_geojson_out = os.path.join(settings.FOLDER_BASE, settings.FOLDER_GEOJSON_OUT, settings.WELL_FILE_GEOJSON_OUT)
#     log = set_logger(settings.WELL_FILE_LOG)
#     log.info(f"Getting file {file_geojson_out}")
#     try:
#         with open(file_geojson_out, 'r', encoding="utf8") as fp:
#             geojson_file = json.load(fp)
#             return geojson_file
#
#     except Exception as e:
#         content = {"msg": f"reload fail. can't read file {file_geojson_out}"}
#         str_err = "Exception occurred " + str(e)
#         # print(str_err)
#         log.info(str_err)
#         return content
