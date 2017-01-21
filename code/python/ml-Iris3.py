import urllib
# If you are using Python 3+, import urllib instead of urllib2
import json
import re
import requests


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"],
                    "Values": [ [ "1", "1", "1", "1", "" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/a742afb173054d3ca4c4568eb889bb2d/services/13f806c7378e4d418a059f7e3a4a97bb/execute?api-version=2.0&details=true'
api_key = '<YOUR_API_KEY>' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)
response = urllib.request.urlopen(req)


    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

result = response.read()
print(result)