from flask import Flask, request, jsonify
#from db.data_models import Base

app = Flask(__name__)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    file = request.files['file']
    return jsonify({'error': 'No file provided'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)