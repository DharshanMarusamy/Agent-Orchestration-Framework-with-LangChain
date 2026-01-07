import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from researcher import Researcher
from analyst import Analyst
from writer import Writer

app = Flask(__name__)
CORS(app)

@app.route('/api/run-workflow', methods=['POST'])
def trigger_workflow():
    data = request.json
    topic = data.get('topic')
    if not topic: return jsonify({"error": "No topic provided"}), 400

    logs = []
    
    # Agent 1
    out1 = Researcher().run(topic)
    logs.append({"agent": "Researcher", "output": out1})
    if "Error" in out1: return jsonify({"final_email": out1, "logs": logs})
    time.sleep(1)

    # Agent 2
    out2 = Analyst().run(out1)
    logs.append({"agent": "Analyst", "output": out2})
    if "Error" in out2: return jsonify({"final_email": out2, "logs": logs})
    time.sleep(1)

    # Agent 3
    out3 = Writer().run(topic, out2)
    logs.append({"agent": "Writer", "output": out3})

    return jsonify({"final_email": out3, "logs": logs})

if __name__ == '__main__':
    print("🚀 Backend running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
