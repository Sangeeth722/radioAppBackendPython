#
from flask import Flask, request, send_file, jsonify, after_this_request
from flask_cors import CORS
from pyradios import RadioBrowser
#
app = Flask(__name__)
CORS(app)

@app.route("/api", methods=['POST'])
def radio():
    rb = RadioBrowser()
    data = request.get_json()
    tag = data.get('tag','Malyalam')

    stations = rb.stations_by_tag(tag)
    return  jsonify(stations)

if __name__ == "__main__":
    app.run(debug=True)


#
# from pyradios import RadioBrowser
#
#
# rb = RadioBrowser()
#
# stations = rb.stations_by_tag("english")
# print(stations[5])
