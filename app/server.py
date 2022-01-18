from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import math

app = Flask(__name__,template_folder='template')


def build_url(search_str, fields):
    
    
    q = "*:*"
  
    url = f"http://localhost:8983/solr/system3/select?defType=edismax&q.op=OR&q={search_str}&qf={fields}&indent=true&rows=10"
    
    return url

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results")
def results():

    page = request.args.get('page')
    print("Page:", page)
    query= request.args.get('query')
    query_url = query +  f"&start={(int(page) - 1) * 10}"
    response = requests.get(query_url).json()['response']
    results = response['docs']
    num_docs = response['numFound']
    print("Start:", response['start'])
    print("Query:", request.args.get('query'))
    num_pages = math.ceil(num_docs / 10.0)
    
    return render_template('result.html',query=query, results=results, page=page, num_pages=num_pages)






@app.route("/search", methods=['POST'])
def search():
    no_fields=True
    search_str = request.form['search_str']
    search_fields = ""
    fields = ['text', 'title', 'thread_title','author', 'country', 'site_url','type']
    weights = ['^1 ', '^2 ', '^2 ', '^3 ','^1 ', '^1.3 ','^1 '] 
    for i, field in enumerate(fields):
        if field in request.form:
            search_fields += field + weights[i]
            no_fields=False
    if(no_fields):
        for i, field in enumerate(fields):
            search_fields += field + weights[i]
           
    query_url = build_url(search_str, search_fields)
    
    return redirect(url_for('results', query=query_url, page="1")) #TODO add pages

app.secret_key = os.urandom(24)
app.run(debug = True)



