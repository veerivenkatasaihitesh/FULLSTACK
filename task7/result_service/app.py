import sys
import os
from flask import Flask, jsonify

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service import get_result
from exceptions import ResultCalculationException

app = Flask(__name__)


@app.route("/result/<int:student_id>", methods=["GET"])
def result(student_id):

    try:
        return jsonify(get_result(student_id))

    except ResultCalculationException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5002, debug=True)