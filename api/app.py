from flask import Flask, request, jsonify
#from db.data_models import Base

app = Flask(__name__)

# Database configuration
DB_URL = 'sqlite:///db.globant_db'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        files = request.files
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)