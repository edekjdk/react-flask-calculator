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
    image_output = result["image_output"]

    return jsonify(
        {
            "input": userInput,
            "output": output,
            "image_output": image_output,
            "latex_output": latex_output,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
