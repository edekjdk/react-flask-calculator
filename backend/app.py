from flask import Flask, jsonify
from services import MathEngine
from services import Expression_processor


app = Flask(__name__)


@app.route("/math/<string:userInput>")
def math(userInput):
    processor = Expression_processor(userInput)
    engine = MathEngine(processor.get_inner_expression(), processor.mode)
    result = engine.evaluate()
    output = result["output"]
    latex_output = result["latex_output"]

    return jsonify(
        {
            "input": str(userInput),
            "output": str(output),
            "latex_output": str(latex_output),
        }
    )
    # return "{}".format(type(output))


if __name__ == "__main__":
    app.run(debug=True)
