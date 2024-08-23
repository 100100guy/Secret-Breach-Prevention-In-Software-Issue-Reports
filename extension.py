from flask import Flask, request
import pandas as pd

from secret_finding_for_tool import prediction
from flask_cors import CORS

app = Flask(__name__)

app = Flask(__name__)
CORS(app, resources={r"/checkdescription": {"origins": "*"}})  # Replace "*" with the specific origin if needed

# receive json and predict if it contains secrets return true or false
@app.route('/checkdescription', methods=['POST'])
def predict_endpoint():
    payload = request.json
    print(payload)
    description = payload['description']
    dict ={}
    dict[0] = {'body': description}
    data = pd.DataFrame.from_dict(dict, "index")
    data.to_csv('issue.csv', index=False)     
    df = pd.read_csv('issue.csv')
    content = df['body'][0]
    result = prediction(content)
    return {'prediction': result}


if __name__ == '__main__':
    app.run(port=5000)