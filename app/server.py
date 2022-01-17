from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import math

app = Flask(__name__,template_folder='template')


def build_url(search_str, fields):
    
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
    #TODO add sorts
    #TODO add ranges
    

    url = f"http://localhost:8983/solr/system3/select?q={q}&fl=*,[child]&q.op=OR&defType=lucene&indent=true&rows=10"

    return url

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results")
def results():

    page = request.args.get('page')
    print("Page:", page)

    #query_url = session['query_url']
    query_url = request.args.get('query')
    query_url = query_url +  f"&start={(int(page) - 1) * 10}"
    print(query_url)
    response = requests.get(query_url).json()['response']
    results = response['docs']
    num_docs = response['numFound']

    num_pages = math.ceil(num_docs / 10.0)

    return render_template('results.html', results=results, page=page, num_pages=num_pages)






@app.route("/search", methods=['POST'])
def search():
    search_str = request.form['search_str']
    search_fields = ""
    fields = ['text', 'title', 'thread_title','author', 'country', 'site_url','type']
    #weights = ['^0.5', '^0.2', '^1.2', '^1.3', '^1.3'] #TODO add weigths
    for i, field in enumerate(fields):
        if field in request.form:
            search_fields += field + '^1' + ' '
    query_url = build_url(search_str, search_fields)

    print(query_url)
    #session['query_url'] = query_url
    return redirect(url_for('results', query=query_url, page=1)) #TODO add pages

app.secret_key = os.urandom(24)
app.run(debug = True)



