import datetime
import time , json
from typing import Union
from uuid import UUID
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi import Body, FastAPI , Form , Depends
from typing import Union , List
from pydantic import BaseModel, EmailStr
from fastapi_keycloak import FastAPIKeycloak, OIDCUser ,KeycloakError
from bson import ObjectId
app = FastAPI()
mongodb_uri = 'mongodb+srv://eam:1234@cluster0.yablyhz.mongodb.net/test'
#ข้อ 1
@app.get("/01")
def topic1():
    return {
        "Hello": "World",
    }


#ข้อ 2

target_date = datetime.date(2023, 12, 31) 
timestamp = 1673838688
today = datetime.date.fromtimestamp(timestamp) 
time_left = target_date - today 
days_left = time_left.days
date = datetime.date.fromtimestamp(timestamp)
date_time = datetime.datetime.fromtimestamp(timestamp)
date_time_thai = date_time.strftime('%d') 
mon_time = date_time.strftime('%B') 
mon_time_thai = date_time.strftime('%m') 
thisdict =	{
    "01": "มกราคม",
    "02": "กุมภาพันธ์",
    "03": "มีนาคม",
    "04": "เมษายน",
    "05": "พฤษภาคม",
    "06": "มิถุนายน",
    "07": "กรกฎาคม",
    "08": "สิงหาคม",
    "09": "กันยายน",
    "10": "ตุลาคม",
    "11": "พฤศจิกายน",
    "12": "ธันวาคม",
    }
month = thisdict[mon_time_thai]
year_time_thai = int(date_time.strftime('%Y')) + 543
year_thai = str(year_time_thai)
hour_time_thai = date_time.strftime('%H')
minute_time_thai = date_time.strftime('%M')
second_time_thai = date_time.strftime('%S')
date_time_utc = date_time.strftime('%d/%m/%Y, %H:%M:%S') 
timer = date_time.strftime('%X %p') 

@app.get("/02")
def topic2():

    return {
    "timestamp" : timestamp,
    "date_format": date,
    "date_time_format": date,
    "date_time_format_thai": "วันที่ " + date_time_thai + " เดือน " + month +" ปี "+ year_thai + " เวลา " + hour_time_thai + " นาฬิกา " + minute_time_thai + " นาที " + second_time_thai + " วินาที ",
    "date_time_format_utc": date_time_utc,
    "date_time_format_eng_utc": "The day is " + date_time_thai + " the month is " + mon_time +", the time is " + timer,
    "date_diff_to_end_year": days_left
    }

#ข้อ 3
@app.get("/03")
async def topic3(date_start: str = ""):
    today = datetime.datetime.today()
    d1 = today.strftime("%m/%d/%Y")
    try:
        datetime_object = datetime.datetime.strptime(date_start, '%m/%d/%Y')
    except:
        return {
            "error_message" : "date_start date format invalid " + d1,
            "status_code" : "422"
        }
    d_time_thai = datetime_object.strftime('%d') 
    m_time = date_time.strftime('%B') 
    m_time_thai = datetime_object.strftime('%m') 
    monthz = thisdict[m_time_thai]
    y_time_thai = int(datetime_object.strftime('%Y')) + 543
    y_thai =  str(y_time_thai)
    h_time_thai = datetime_object.strftime('%H')
    m_time_thai = datetime_object.strftime('%M')
    s_time_thai = datetime_object.strftime('%S')
    timers = datetime_object.strftime('%X %p') 
    return {
        "date_format" : date_start,
        "error_message" : "",
        "date_time_format": date_time,
        "date_time_format_thai": "วันที่ " + d_time_thai + " เดือน " + monthz +" ปี "+ y_thai + " เวลา " + h_time_thai + " นาฬิกา " + m_time_thai + " นาที " + s_time_thai + " วินาที ",
        "date_time_format_utc": date_time_utc,
        "date_time_format_eng_utc": "The day is " + d_time_thai + " the month is " + m_time +", the time is " + timers,
        "date_diff_to_end_year": days_left
    }
    
#ข้อ 4
@app.get("/04")
async def topic4(month: str = ""):
    
    try:
        month_object = datetime.datetime.strptime(month, '%m')
        months = thisdict[month]
    except:
        return {
            "error_message" : "" ,
            "status_code" : "422"
        }
    return {
        "เดือน" : months,
       
    }

#ข้อ 5
@app.get("/05")
async def topic5() -> dict:
     return {
    "timestamp" : timestamp,
    "date_format": date,
    "date_time_format": date,
    "date_time_format_thai": "วันที่ " + date_time_thai + " เดือน " + month +" ปี "+ year_thai + " เวลา " + hour_time_thai + " นาฬิกา " + minute_time_thai + " นาที " + second_time_thai + " วินาที ",
    "date_time_format_utc": date_time_utc,
    "date_time_format_eng_utc": "The day is " + date_time_thai + " the month is " + mon_time +", the time is " + timer,
    "date_diff_to_end_year": days_left
    }

#ข้อ 6
@app.get("/06")
async def topic6(date_start) -> dict:
    today = datetime.datetime.today()
    d1 = today.strftime("%m/%d/%Y")
    try:
        datetime_object = datetime.datetime.strptime(date_start, '%m/%d/%Y')
    except:
        return {
            "error_message" : "date_start date format invalid " + d1,
            "status_code" : "422"
        }
    d_time_thai = datetime_object.strftime('%d') 
    m_time = date_time.strftime('%B') 
    m_time_thai = datetime_object.strftime('%m') 
    monthz = thisdict[m_time_thai]
    y_time_thai = int(datetime_object.strftime('%Y')) + 543
    y_thai =  str(y_time_thai)
    h_time_thai = datetime_object.strftime('%H')
    m_time_thai = datetime_object.strftime('%M')
    s_time_thai = datetime_object.strftime('%S')
    timers = datetime_object.strftime('%X %p') 
    return {
        "date_format" : date_start,
        "error_message" : "",
        "date_time_format": date_time,
        "date_time_format_thai": "วันที่ " + d_time_thai + " เดือน " + monthz +" ปี "+ y_thai + " เวลา " + h_time_thai + " นาฬิกา " + m_time_thai + " นาที " + s_time_thai + " วินาที ",
        "date_time_format_utc": date_time_utc,
        "date_time_format_eng_utc": "The day is " + d_time_thai + " the month is " + m_time +", the time is " + timers,
        "date_diff_to_end_year": days_left
    }



idp = FastAPIKeycloak(
    server_url="http://ec2-54-179-216-229.ap-southeast-1.compute.amazonaws.com:8080",
    client_id="test01",
    client_secret="8cPESoXnzKyloPjvaRbSLqOZQCD44xVB",
    admin_client_id="admin-cli",
    admin_client_secret="MqJ1LKFhbEM6iVFJrBYhtWu2g3HuLH7u",
    realm="test01",
    callback_uri="http://localhost:8081/callback"
)
#ข้อ 7 
idp.add_swagger_config(app)


class user(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

@app.post("/07")
async def topic7(user: user):
    try:
        return idp.create_user(first_name = user.first_name ,last_name= user.last_name, username=user.username, email=user.email, password=user.password,send_email_verification = False)
    except KeycloakError as e:
        return {
            "Status_Code" : e.status_code,
            "error_message":e.reason
        }

@app.get("/08")
def topic8(user: OIDCUser = Depends(idp.get_current_user())):

    return user


#ข้อ 9 สมัครแล้ว
#ข้อ 10
client = MongoClient(mongodb_uri)
db = client['test01']
test2 = db["test01"]
#ข้อ 11
@app.post("/11")
async def topic11(date_start,user: OIDCUser = Depends(idp.get_current_user())) -> dict:
    today = datetime.datetime.today()
    d1 = today.strftime("%m/%d/%Y")
    try:
        datetime_object = datetime.datetime.strptime(date_start, '%m/%d/%Y')
    except:
        return {
            "error_message" : "date_start date format invalid " + d1,
            "status_code" : "422"
        }
    d_time_thai = datetime_object.strftime('%d') 
    m_time = date_time.strftime('%B') 
    m_time_thai = datetime_object.strftime('%m') 
    monthz = thisdict[m_time_thai]
    y_time_thai = int(datetime_object.strftime('%Y')) + 543
    y_thai =  str(y_time_thai)
    h_time_thai = datetime_object.strftime('%H')
    m_time_thai = datetime_object.strftime('%M')
    s_time_thai = datetime_object.strftime('%S')
    timers = datetime_object.strftime('%X %p') 
    try:
        for item in test2.find({}):
            mydict = {
            "date_format" : date_start,
            "error_message" : "",
            "date_time_format": date_time,
            "date_time_format_thai": "วันที่ " + d_time_thai + " เดือน " + monthz +" ปี "+ y_thai + " เวลา " + h_time_thai + " นาฬิกา " + m_time_thai + " นาที " + s_time_thai + " วินาที ",
            "date_time_format_utc": date_time_utc,
            "date_time_format_eng_utc": "The day is " + d_time_thai + " the month is " + m_time +", the time is " + timers,
            "date_diff_to_end_year": days_left
            }
        x = test2.insert_one(mydict)
        return{
            "message" : "Insert Data Success"
        }
    except:
         return{
            "message" : "error"
        }

#ข้อ 12
@app.get("/12")
async def topic12(limit: int = 10,user: OIDCUser = Depends(idp.get_current_user())) :
    #for myresult in test2.find({}).limit(limitz):
    test2.find({}).limit(limit)
    return json.loads(dumps(test2.find({}).limit(limit)))

#ข้อ 13
@app.get("/13/{id}")
async def topic13(id: str,user: OIDCUser = Depends(idp.get_current_user())) :
    oid2 = { "_id": ObjectId(id) }
    mydoc = test2.find(oid2)  
    return json.loads(dumps(mydoc))

#ข้อ 14
@app.put("/14/{id}")
async def topic14(id: str,user: OIDCUser = Depends(idp.get_current_user())) :
    oid2 = { "_id": ObjectId(id) }
    myquery = { "date_format": "10/10/2000" }
    newvalues = { "$set": { "date_format": "06/15/2000" } }
    test2.update_one(myquery, newvalues)
    for x in test2.find(oid2):
        print(x)
    return json.loads(dumps(x))
   
#ข้อ 15
@app.delete("/15/{id}")
async def topic15(id: str,user: OIDCUser = Depends(idp.get_current_user())) :
    oid2 = { "_id": ObjectId(id) }
    try:
        test2.delete_one(oid2)
        for x in test2.find(oid2):
            print(test2.de)
        return {"message" : "Delete Success"}
    except:
         return{
            "message" : "error"
        }
   