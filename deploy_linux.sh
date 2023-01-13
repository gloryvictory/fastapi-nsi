#!/bin/bash
rm -rf /var/zsniigg/fastapi-nsi/
cp -r /ftp/1/* /var/zsniigg/
sudo chmod -R 777 /var/zsniigg/fastapi-nsi/
cd /var/zsniigg/fastapi-nsi/
docker build . -t fastapi-web
# docker run -p 8000:8000 fastapi-web
# docker run -d -p 8000:8000 fastapi-web
# docker rmi fastapi-web
