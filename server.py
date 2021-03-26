from flask import Flask, render_template, request, Response, send_file, jsonify
import requests
import json


# Server & Handling Setting
app = Flask(__name__)


@app.route("/api/", methods=['GET'])
def generate():
    try:

        keyword=request.args.get('keyword')
        num_samples = 1
        length = 300
        
        URL = 'https://feature-add-torch-serve-gpt-2-server-gkswjdzz.endpoint.ainize.ai/infer/gpt2_sherlock'
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(URL, headers=headers, data=json.dumps({
            'text': keyword,
            'num_samples': 1,
            'length': length
        }))

        return jsonify(res.json()), 200
    except Exception:
        print("Empty Text")
        return Response("fail", status=400)


# Health Check
@app.route('/healthz')
def health():
    return "ok", 200

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
