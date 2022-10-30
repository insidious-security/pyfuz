
from fastapi import FastAPI, Request, File, UploadFile, Depends
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from typing import Any
from simplexml import dumps, loads
from datetime import date
#docs_url=None

app = FastAPI()

class XmlResponse(Response):
    media_type = "text/xml"

    def render(self, content: Any) -> bytes:
        return dumps({'response': content}).encode("utf-8")

@app.get('/blackarch')
def main():
     data = [{'User': 'a', 'date': date.today(), 'count': 1},
     {'User': 'b', 'date':  date.today(), 'count': 2}]
     return JSONResponse(content=jsonable_encoder(data))

@app.get('/torch')
def main():
     data = [{'Workstation': 'deathstar'},
     {'User': 'sidious'}]
     return JSONResponse(content=jsonable_encoder(data))

@app.get('/logging')
def main():
     data = [{'id': 1,'first_name': 'Jeanette','last_name': 'Penddreth','email': 'jpenddreth0@census.gov','gender': 'Female','ip_address': '26.58.193.2'}, 
     {'id': 2,'first_name': 'Giavani','last_name': 'Frediani','email': 'gfrediani1@senate.gov','gender': 'Male','ip_address': '229.179.4.212'}, 
     {'id': 3,'first_name': 'Noell','last_name': 'Bea','email': 'nbea2@imageshack.us','gender': 'Female','ip_address': '180.66.162.255'}, 
     {'id': 4,'first_name': 'Willard','last_name': 'Valek','email': 'wvalek3@vk.com','gender': 'Male','ip_address': '67.76.188.26'}]
     return JSONResponse(content=jsonable_encoder(data))

@app.get('/test1')
def main():
     data = [{'id': 1,'first_name': 'Jeanette','last_name': 'Penddreth','email': 'jpenddreth0@census.gov','gender': 'Female','ip_address': '26.58.193.2'}, 
     {'id': 2,'first_name': 'Giavani','last_name': 'Frediani','email': 'gfrediani1@senate.gov','gender': 'Male','ip_address': '229.179.4.212'}, 
     {'id': 3,'first_name': 'Noell','last_name': 'Bea','email': 'nbea2@imageshack.us','gender': 'Female','ip_address': '180.66.162.255'}, 
     {'id': 4,'first_name': 'Willard','last_name': 'Valek','email': 'wvalek3@vk.com','gender': 'Male','ip_address': '67.76.188.26'}]
     return XmlResponse(data)
