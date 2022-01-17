from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import math

app = Flask(__name__,template_folder='template')


def build_url(search_str, fields, sort_params):
    
    search_str = ""
   
    if len(fields) != 0:
        search_str = f'{{!edismax qf="{fields}" v="{search_str}"}}'

    q = "*:*"
    
    if search_str != "":
        q = " " + search_str

    # fq_rating = f"rating:[{rating_range[0]} TO {rating_range[1]}]"
    # fq_pages = f"pages:[{pages_range[0]} TO {pages_range[1]}]"
    # fq_reviews = f"num_reviews:[{reviews_range[0]} TO {reviews_range[1]}]"
    # fq_totalratings = f"totalratings:[{totalratings_range[0]} TO {totalratings_range[1]}]"

    sort_str = f"{sort_params[0]} {sort_params[1]}"

    fq = "type:book"
    url = f"http://localhost:8983/solr/system3/select?q={q}&fl=*,[child]&fq={fq}&q.op=OR&defType=lucene&indent=true&sort={sort_str}&rows=10"

    return url

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    print( request.form)
    return render_template('index.html')

app.secret_key = os.urandom(24)
app.run(debug = True)