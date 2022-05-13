from quart import Quart, request, jsonify

app = Quart(__name__)


@app.route('/')
async def index():
    return jsonify({'ip': request.remote_addr})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1864)
