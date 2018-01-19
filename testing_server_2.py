import json
from flask import Flask
from flask import request
from flask import make_response
import requests
from requests.auth import HTTPDigestAuth
import xml.etree.ElementTree as ET


app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello World!</h>"

@app.route('/webhook',methods=['post'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "get":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    name = parameters.get("smartplug")
    # 코드추가 #
    # 코드추가 #
    # 코드추가 #
    # 코드추가 #

    root = ET.fromstring(r.text)

    num = 1
    for element in root.findall("record"):
        num += 1
        print([element.findtext("timestamp"), element.findtext("usage")])
        if num > 10 :
            string_time = element.findtext("usage")
            break


    speech = name + "는 " + string_time + "kWh 만큼 사용하였습니다"
    #speech = "현재 노후회된 장비는 A구역의 실습지원 프런터로 고장난것으로 추정 됩니다."
    print("Responese:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "ElectricPower_testing"
    }

if __name__ == '__main__':
    app.run(debug=True)