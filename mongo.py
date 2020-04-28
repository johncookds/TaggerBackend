# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

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
  rawtext = mongo.db.rawtext
  url = request.json['url']
  text = request.json['text']
  page = request.json['page']
  reference_url = request.json['reference_url']
  entry_id = rawtext.insert({'url': url, 
                            'text': text,
                            'page': page,
                            'reference_url': reference_url})
  new_entry = rawtext.find_one({'_id': entry_id })
  output = {'text' : new_entry['text']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
