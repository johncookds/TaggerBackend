# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'tagger'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/tagger'

mongo = PyMongo(app)

@app.route('/text', methods=['GET'])
def get_all_text():
  return jsonify({})
#  star = mongo.db.stars
#  output = []
#  for s in star.find():
#    output.append({'name' : s['name'], 'distance' : s['distance']})
#  return jsonify({'result' : output})

@app.route('/text/', methods=['GET'])
def get_one_text(name):
  return jsonify({})
#  star = mongo.db.stars
#  s = star.find_one({'name' : name})
#  if s:
#    output = {'name' : s['name'], 'distance' : s['distance']}
#  else:
#    output = "No such name"
#  return jsonify({'result' : output})

@app.route('/text', methods=['POST'])
def add_text():
  now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  rawtext = mongo.db.rawtext
  request.json['datetime'] = now
  entry_id = rawtext.insert_one(request.json)
                            #'page': page,
                            #'reference_url': reference_url})
  try:
    new_entry = rawtext.find_one({'_id': entry_id })
  except:
    return 'save failed'
  return 'save succeeded'

if __name__ == '__main__':
    app.run(debug=True)
