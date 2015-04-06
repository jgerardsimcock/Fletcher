import requests
import json

API_url = "http://104.236.209.60:8888/predict"

one_example  = {"example": [192]}

payload = json.dumps(one_example)


headers = {'content-type': 'application/json'}

response = requests.post(API_url, data=payload, headers=headers)

print 'Response status code is %s' % response.status_code

print "The full response is:"
print response. text

output = response.json()

predicted_class = output["predicted"][0]

print "The predicted class for x =192 is %s" % predicted_class

new_x = 838393893
payload = json.dumps({"example": new_x})
response = requests.post(API_url, data=payload, headers=headers)
output = response.json()
predicted_class = output["predicted"][0]

print "The predicted class for x = 838393893 is %s" % predicted_class



