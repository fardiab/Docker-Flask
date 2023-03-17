from flask import Flask
from redis import Redis
app = Flask(__name__)
r = Redis(host='redis', decode_responses=True, port=6379)

r.set('counter', 0)

@app.route('/')
def hello_world():
    r.incr('counter')
    return f"You are visitor number {r.get('counter')}"

if __name__ == "__main__":
    app.run(debug=True)