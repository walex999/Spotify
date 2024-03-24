#!/usr/bin/python3


import pandas as pd
from dotenv import load_dotenv
from os import getenv


load_dotenv("./spotify.env")

# import all streamin history values
strm0=getenv("streaming0")
print(strm0)
strm1=getenv("streaming1")
print(strm1)
strm2=getenv("streaming2")
print(strm2)


stream_db0 = pd.read_json(strm0)
stream_db1 = pd.read_json(strm1)
stream_db2= pd.read_json(strm2)

temp = pd.concat([stream_db0,stream_db1])
streaming_history = pd.concat([temp, stream_db2])


print(streaming_history.head(10))
print(streaming_history.size)
