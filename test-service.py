from flask import Flask, request
from jsonschema import validate, exceptions as jexcept


app = Flask(__name__)


hook_schema = {
    "type": "object",
    "properties": {
        "build_id": {"type": "number"},
        "warning": {"type": "string"},
        "you_know_this_is_totally_made_up": {"type": "boolean"}
    }
}

@app.route("/api-gateway-hook", methods=['POST'])
def grab_hook():
    """Create a method we can use for testing that contains a defined schema and pass it through an API gateway,
    having a positive and negative test.

    After looking in bitballoon for a quick moment, I can't determine for sure whether which
    data we're sending to gitlab, so I'm going to make up a structure to use here, and refine it later.
    """
    try:
        validate(request.json, schema=hook_schema)
        return "That is valid"
    except jexcept.ValidationError as ve:
        app.logger.error(f"Got an invalid schema: {str(ve)}")
        return "Invalid schema!", 400


if __name__ == '__main__':
    app.run_server(debug=True)
