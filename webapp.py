from flask import Flask, render_template, request, url_for, session, jsonify, g, flash, redirect, escape, Response
app = Flask(__name__)
import app

@app.route('/')
def slash():
    app.MasterFunction
    return render_template('index.html')
