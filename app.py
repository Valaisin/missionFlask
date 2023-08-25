from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/reformat", methods=['POST'])
def reformat_basic():
    try:
        input_data = request.json

        # extract the relevant data
        file_name = input_data['Filename']
        first_frame_number = input_data['FirstFrameNumber']
        last_frame_number = input_data['LastFrameNumber']

        # Jsonify & format.
        return jsonify({
            "FirstFrame": file_name.replace('%07d', str(first_frame_number)),
            "LastFrame": file_name.replace('%07d', str(last_frame_number))
        }), 200
    except Exception as exception:
        return jsonify({"Exception": str(exception)}), 500


if __name__ == '__main__':
    app.run()
