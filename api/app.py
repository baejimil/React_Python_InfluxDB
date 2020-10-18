from flask import *
from flask_cors import CORS

from influxdb import InfluxDBClient
from datetime import datetime, timedelta

from functools import wraps

app=Flask(__name__)
CORS(app)
app.debug=True

def use_db(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        host='localhost'
        port=8086
        user='root'
        user_password='1234'
        dbname='example'
        client=InfluxDBClient(host, port, user, user_password, dbname )

        g=f.__globals__
        result = f(*args, **kwargs)

        return result
    return wrap

@app.route('/', methods=['GET', 'POST'])
# @use_db
def index():
    host='localhost'
    port=8086
    user = 'root'
    password = '1234'
    dbname = 'example'
    # dbuser = 'smly'
    # dbuser_password = '1234'
    query = 'select Float_value from Dummy_HTML;'
    # query_where = 'select Int_value from cpu_load_short where host=$host;'
    bind_params = {'host': 'server01'}
    json_body = [
        {
            "measurement": "Dummy_HTML",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": 'None',
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    dt = datetime.now() - timedelta(seconds=6)
    json_body[0]['time'] = dt
    print ("UTC now=<%s>" % (dt))
    client=InfluxDBClient(host, port, user, password, dbname )

    # print("Create database: " + dbname)
    # client.create_database(dbname)

    # print("Create a retention policy")
    # client.create_retention_policy('retention_policy', '3d', 3, default=True)

    # print("Switch user: " + dbuser)
    # client.switch_user(dbuser, dbuser_password)

    
    # print("Write points: {0}".format(json_body))
    dummy=request.form.get('dummy')
    print('Dummy : ')
    print(dummy)
    json_body[0]['fields']['Dummy']=dummy
    print(json_body)
    client.write_points(json_body)

    # print("Querying data: " + query)
    result = client.query(query)

    # print("Result: {0}".format(result))

    # print("Querying data: " + query_where)
    # result = client.query(query_where, bind_params=bind_params)

    # print("Result: {0}".format(result))

    # print("Switch user: " + user)
    # client.switch_user(user, password)

    # print("Drop database: " + dbname)
    # client.drop_database(dbname)

    return redirect('http://127.0.0.1:3000/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
