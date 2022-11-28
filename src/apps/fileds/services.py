#  @classmethod
# def request(url, urllib2=None):
#         fh = urllib2.urlopen(url)
#         return cls.create(url=url, response=json.loads(fh.read()))
#
#
import json
import os

from src.config import settings


def reload_fields():
    content = {"message": "reload success"}
    file_geojson = os.path.join(settings.FOLDER_DATA, settings.FILE_FIELDS)
    try:
        with open(file_geojson, 'r', encoding="utf8") as f:
            data = json.load(f)
        print(data)
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content
