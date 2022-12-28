import json
import os
import hashlib
from typing import Dict, Any

import geopandas

from src.apps.lu.models import LU
from src.config import settings
from src.config.log import set_logger

#TODO добавить номер лицензии


async def lu_reload():
    content = {"msg": "Success"}
    file_geojson = os.path.join(os.getcwd(), settings.FOLDER_DATA, settings.LU_FILE_GEOJSON_IN)
    file_geojson_out = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT, settings.LU_FILE_GEOJSON_OUT)
    name_field = settings.LU_NAME_FIELD  # 'name_ru'
    nom_lic = settings.LU_NOM_LIC_FIELD # nom_lic
    crs_out = settings.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        # MultiPolygon to Polygon
        gdf = gdf.explode(column='geometry', ignore_index=True, index_parts=False)
        # Объединяем два контура одного месторождения с одинаковым наименованием
        gdf = gdf.dissolve(by=name_field, as_index=False)
        # gdf.envelope
        # gdf.to_crs('epsg:32663').centroid.to_crs(crs_out)
        gdf['centroid'] = gdf.centroid

        gdf = gdf.to_crs(crs=crs_out)

        gdf1 = gdf[[name_field, 'centroid', nom_lic]]
        gdf1.set_geometry("centroid")
        gdf1 = gdf1.rename(columns={'centroid': 'geom'}).set_geometry('geom')
        gdf1.to_file(file_geojson_out, driver='GeoJSON')
        for i in range(0, len(gdf1)):
            gdf1.loc[i, 'lon'] = gdf1.geometry.centroid.x.iloc[i]
            gdf1.loc[i, 'lat'] = gdf1.geometry.centroid.y.iloc[i]
        log = set_logger(settings.LU_FILE_LOG)

        log.info(gdf1)

        await LU.objects.delete(each=True)

        for i in range(0, len(gdf1)):
            str_name = str(gdf1.loc[i, name_field]).encode()
            str_nom_lic= str(gdf1.loc[i, nom_lic]).encode()
            hash_object = hashlib.md5(str_name)
            hash_md5 = hash_object.hexdigest()
            lu_table = LU(
                name_ru=str_name,
                lon=gdf1.loc[i, 'lon'],
                lat=gdf1.loc[i, 'lat'],
                crs=crs_out,
                hash=hash_md5,
                nom_lic=str_nom_lic
            )
            await lu_table.upsert()
            # print(gdf1.loc[i, 'name_ru'])
        count = await LU.objects.count()
        log.info(f"Total LU count {count}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content


async def lu_get_all():
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.LU_FILE_LOG)

    try:
        lu_all = await LU.objects.all()

        log.info("lu load successfully")
        return lu_all
    except Exception as e:
        content = {"msg": f"reload fail. can't read lu from database {LU.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


#
#
async def lu_get_all_count() -> dict[str, str | Any] | dict[str, str]:
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.LU_FILE_LOG)

    try:
        # table_exist = lu.
        lu_all_count = await LU.objects.count()

        log.info(f"lu count load successfully: {lu_all_count}")
        content = {"msg": "Success", "count": lu_all_count}
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't read count of lu from database {LU.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


#
#
async def lu_get_geojson_file():
    content = {"msg": "Success"}
    file_geojson_out = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT, settings.LU_FILE_GEOJSON_OUT)
    log = set_logger(settings.LU_FILE_LOG)
    log.info(f"Getting file {file_geojson_out}")
    try:
        with open(file_geojson_out, 'r', encoding="utf8") as fp:
            geojson_file = json.load(fp)
            return geojson_file

    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson_out}"}
        str_err = "Exception occurred " + str(e)
        # print(str_err)
        log.info(str_err)
        return content
