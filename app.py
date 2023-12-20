from flask import Flask, request, jsonify
from models.ngram import correctWord, correctSentences, suggestions


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
 
@app.route('/api/v1/id/word-correction', methods=['POST'])
def id_word_correction():
    # Ambil data yang dikirimkan dengan metode POST
    req = request.get_json()
    # print(req)
    response = {
        'before':req['word'],
        'result':correctWord(req['word']),
        'suggestions': list(suggestions(req['word']))
    }

    response_data = {'message': 'Kata berhasil dikoreksi!', 'data': response}
    # response_data['data']['result'] = list(response_data['data']['result'])
    return jsonify(response_data)

@app.route('/api/v1/id/sentence-correction', methods=['POST'])
def id_sentence_correctiopm():
    # Ambil data yang dikirimkan dengan metode POST
    req = request.get_json()
    
    response = {
        'before':req['sentences'],
        'result':correctSentences(req['sentences'])
    }

    response_data = {'message': 'Kalimat berhasil dikoreksi!', 'data': response}
    
    return jsonify(response_data)


@app.route('/api/v1/id/sentence-correction', methods=['POST'])
def id_sentence_correction():
    # Ambil data yang dikirimkan dengan metode POST
    req = request.get_json()
    
    response = {
        'before':req['sentence'],
        'result':correctSentences(req['sentence'])
    }

    response_data = {'message': 'Kalimat berhasil dikoreksi!', 'data': response}
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)