from flask import Flask, g, session

app = Flask("draw")
app.secret_key = "oeihfoiwehfiowehf"
import draw.routes
