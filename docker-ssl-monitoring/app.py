from flask import Flask, Response
from prometheus_client import generate_latest, CollectorRegistry, Counter

app = Flask(__name__)

registry = CollectorRegistry()
REQUESTS = Counter('hello_world_total', 'Hello World invocations', registry=registry)

@app.route("/")
def hello():
    REQUESTS.inc()
    return "<h1 style='color:blue'>Hello World from Docker!</h1>"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(registry), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
