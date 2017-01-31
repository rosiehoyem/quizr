import os
import pandas as pd
import numpy as np
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__) # create the application instance :)

app.config.from_object(__name__) # load config from this file , quizr.py

app.config.update(dict(
    SECRET_KEY='development key'
))
app.config.from_envvar('QUIZR_SETTINGS', silent=True)

def get_vocab():
    base = "https://docs.google.com/spreadsheets/d/"
    doc_id = "13uFW3lriigsAKJTAn_Ilo3fo7ZdeLUKbtqOe65Bf4iw"
    export_sheet = "/export?gid=577814466&format=csv"
    url = base + doc_id + export_sheet
    vocab = pd.read_csv(url,index_col=False)
    sample = vocab.sample(10)
    return sample.to_dict(orient = "records")

@app.route('/')
def index():
    vocab = get_vocab()
    return render_template('index.html', vocab=vocab)