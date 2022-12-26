import json
import os
import hashlib
import geopandas

from src.apps.ngr.models import NGR
from src.config import settings
from src.config.log import set_logger


async def ngr_reload():
    content = {"msg": "Success"}
    file_geojson = os.path.join(os.getcwd(), settings.FOLDER_DATA, settings.NGR_FILE_GEOJSON_IN)
    file_geojson_out = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT, settings.NGR_FILE_GEOJSON_OUT)
    name_field = settings.NGR_NAME_FIELD  # 'name_ru'
    crs_out = settings.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        # MultiPolygon to Polygon
        # gdf = gdf.explode(column='geometry', ignore_index=True, index_parts=False)
        # Объединяем два контура одного месторождения с одинаковым наименованием
        gdf = gdf.dissolve(by=name_field, as_index=False)
        # gdf.envelope
        # gdf.to_crs('epsg:32663').centroid.to_crs(crs_out)
        gdf['centroid'] = gdf.centroid

        gdf = gdf.to_crs(crs=crs_out)

        gdf1 = gdf[[name_field, 'centroid']]
        gdf1.set_geometry("centroid")
        gdf1 = gdf1.rename(columns={'centroid': 'geom'}).set_geometry('geom')
        gdf1.to_file(file_geojson_out, driver='GeoJSON')
        for i in range(0, len(gdf1)):
            gdf1.loc[i, 'lon'] = gdf1.geometry.centroid.x.iloc[i]
            gdf1.loc[i, 'lat'] = gdf1.geometry.centroid.y.iloc[i]
        log = set_logger(settings.NGR_FILE_LOG)

        log.info(gdf1)

        await NGR.objects.delete(each=True)

        for i in range(0, len(gdf1)):
            str_name = str(gdf1.loc[i, name_field]).encode()
            hash_object = hashlib.md5(str_name)
            hash_md5 = hash_object.hexdigest()
            ngr_table = NGR(
                name_ru=str_name,
                lon=gdf1.loc[i, 'lon'],
                lat=gdf1.loc[i, 'lat'],
                crs=crs_out,
                hash=hash_md5,
            )
            await ngr_table.upsert()
            # print(gdf1.loc[i, 'name_ru'])
        count = await NGR.objects.count()
        log.info(f"Total NGR count {count}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content


async def ngr_get_all():
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.NGR_FILE_LOG)

    try:
        ngr_all = await NGR.objects.all()

        log.info("ngr load successfully")
        return ngr_all
    except Exception as e:
        content = {"msg": f"reload fail. can't read ngr from database {NGR.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


#
#
async def ngr_get_all_count() -> int:
    content = {"msg": f"Unknown error"}
    log = set_logger(settings.NGR_FILE_LOG)

    try:
        # table_exist = ngr.
        ngr_all_count = await NGR.objects.count()

        log.info(f"ngr count load successfully: {ngr_all_count}")
        content = {"msg": "Success", "count": ngr_all_count}
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't read count of ngr from database {NGR.Meta.tablename}"}
        str_err = "Exception occurred " + str(e)
        print(str_err)
        log.info(str_err)
    return content


#
#
async def ngr_get_geojson_file():
    content = {"msg": "Success"}
    file_geojson_out = os.path.join(os.getcwd(), settings.FOLDER_GEOJSON_OUT, settings.NGR_FILE_GEOJSON_OUT)
    log = set_logger(settings.NGR_FILE_LOG)
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
