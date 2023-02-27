import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from flightsql import FlightSQLClient

token = "hABVMTND1Hao381K7mOnYlsVSSk_myy3Vwn4OZEnE9qsNgPniAmhvigj_Ciy0XhtVjj3Lr-apOhUO86AT1c2jw=="
org = "loginservice"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
bucket = "CSE"
class InfluxClient:
    
    def __init__(self):
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_client = FlightSQLClient(
            host = "eu-central-1-1.aws.cloud2.influxdata.com",
            token = os.environ.get("INFLUXDB_TOKEN"),
            metadata={"bucket-name": bucket}
        )
        return
    
    def insert_data(self, email):
    
        p = Point("signups").tag("signup").field("email", email)
        self.write_api.write(bucket=bucket, org=org, record=p)
            
    
    def insert_object(self, measurement, data_object):
            
        # point = (
        #     Point(measurement)
        #     .tag("service", "login_service")
        #     .field("action", "error")
        #     .field("user", "test")
        # )

        point = Point(measurement)
        for key in data_object:
            point = point.field(key, data_object[key])
            
        print(f"[POINT] {point}\n Line protocol: {point.to_line_protocol()}")
        self.write_api.write(bucket=bucket, org=org, record=point)
      
    """
    def query(self, query):
        info = self.query_client.execute(query)
        reader = self.query_client.do_get(info.endpoints[0].ticket)
        
        data = reader.read_all()
        df = data.to_pandas().sort_values(by="time")
        print(df)
        return
    """