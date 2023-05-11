from flask import Flask
from flask_cors import CORS
import openai
from dd_ai.character import character_blueprint
from dd_ai.world import world_blueprint
from dd_ai.interaction import interaction_blueprint
from credentials import API_KEY

app = Flask(__name__)
CORS(app)

app.register_blueprint(character_blueprint)
app.register_blueprint(world_blueprint)
app.register_blueprint(interaction_blueprint)

openai.api_key = API_KEY

if __name__ == '__main__':
    app.run()