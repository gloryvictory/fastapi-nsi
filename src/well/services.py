import json
import os
import hashlib
from typing import Any

import geopandas
from src.models import WELL
from src import settings
from src.log import set_logger


async def well_reload():
    content = {"msg": "Fail"}
    file_geojson = os.path.join(settings.FOLDER_BASE, settings.FOLDER_DATA, settings.WELL_FILE_GEOJSON_IN)
    file_geojson_out = os.path.join(settings.FOLDER_BASE, settings.FOLDER_GEOJSON_OUT, settings.WELL_FILE_GEOJSON_OUT)
    name_well = settings.WELL_NAME_FIELD  # 'name_ru'
    name_area = settings.WELL_NAME_AREA_FIELD
    crs_out = settings.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        gdf1 = gdf.to_crs(crs=crs_out)
        gdf1.to_file(file_geojson_out, driver='GeoJSON')

        # gdf1.to_file(file_geojson_out+"_", driver='CSV')
        # gdf1.to_csv(file_geojson_out + "_", index=False)

        # for i in range(0, len(gdf1)):
        #     gdf1.loc[i, 'lon'] = gdf1.geometry.x.iloc[i]
        #     gdf1.loc[i, 'lat'] = gdf1.geometry.y.iloc[i]
        log = set_logger(settings.WELL_FILE_LOG)

        log.info(gdf1)

        await WELL.objects.delete(each=True)

        cnt_all = len(gdf1)

        cnt_areas = len(gdf1['pl'].unique())
        print(f"Count of AREAS : {cnt_areas}")

        for i in range(0, cnt_all):
            print(f"{i}  of {cnt_all}")
            # str_name = str(gdf1.loc[i, name_well]).encode()
            # str_name_area = str(gdf1.loc[i, name_area]).encode()
            # Получаем уникальное сочетание Площадь + №скважины
            str_name = str(gdf1.loc[i, name_well]).lower()
            str_name_area = str(gdf1.loc[i, name_area]).lower()

            str_name_well_uniq = str(str_name_area + " " + str_name).lower().encode()
            hash_object = hashlib.md5(str_name_well_uniq)
            hash_md5 = hash_object.hexdigest()

            d_lon = gdf1.geometry.x.iloc[i]
            d_lat = gdf1.geometry.y.iloc[i]
            # print(f"{i} , well {str_name}, pl: {str_name_area}")

            well_table = WELL(
                name_ru=str_name,
                lon=d_lon,
                lat=d_lat,
                crs=crs_out,
                hash=hash_md5,
                area=str_name_area
            )
            await well_table.upsert()

            log.info(f"well {str_name}, pl: {str_name_area}")
            # print(gdf1.loc[i, 'name_ru'])

        count = await WELL.objects.count()

        content = {"msg": "Success", "count": count}
        log.info(f"Total ngo count {count}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content


async def well_get_all():
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.WELL_FILE_LOG)

    try:
        well_all = await WELL.objects.all()

        log.info("wells load successfully")
        return well_all
    except Exception as e:
        content = {"msg": f"reload fail. can't read ngo from database {WELL.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


async def well_get_all_count() -> dict[str, str | Any] | dict[str, str]:
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.WELL_FILE_LOG)

    try:
        # table_exist = ngo.
        well_all_count = await WELL.objects.count()

        log.info(f"count load successfuly: {well_all_count}")
        content = {"msg": "Success", "count": well_all_count}
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't read count of ngo from database {WELL.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


async def well_get_geojson_file():
    content = {"msg": "Success"}
    file_geojson_out = os.path.join(settings.FOLDER_BASE, settings.FOLDER_GEOJSON_OUT, settings.WELL_FILE_GEOJSON_OUT)
    log = set_logger(settings.WELL_FILE_LOG)
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


async def well_get_by_area(area: str):
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.WELL_FILE_LOG)
    print(area)
    try:
        well_all = await WELL.objects.all(WELL.area == area)

        log.info("wells load successfully")
        return well_all
    except Exception as e:
        content = {"msg": f"reload fail. can't read ngo from database {WELL.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


async def well_get_area_count(area: str):
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.WELL_FILE_LOG)

    try:
        # table_exist = ngo.
        well_all = await WELL.objects.all(WELL.area == area)
        well_all_count = len(well_all)
        log.info(f"count load successfuly: {well_all_count}")
        content = {"msg": "Success", "count": well_all_count}
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't read count of ngo from database {WELL.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content
