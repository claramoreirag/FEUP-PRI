from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import math

app = Flask(__name__,template_folder='template')


def build_url(search_str, fields):
    
    
    q = "*:*"
  
    url = f"http://localhost:8983/solr/system3/select?defType=edismax&q.op=OR&q={search_str}&qf={fields}&indent=true&rows=10&start=00"
    
    return url

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results")
def results():

    page = request.args.get('page')
    print("Page:", page)
    query_url = request.args.get('query')
    if(page=='1'):
        query_url = query_url
    else:
        nextp=str(int(query_url[-2:])+10)
        print(nextp)
        query_url = query_url[0:-2]+nextp
    response = requests.get(query_url).json()['response']
    results = response['docs']
    num_docs = response['numFound']
    print("Start:", response['start'])
    print("Query:", request.args.get('query'))
    num_pages = math.ceil(num_docs / 10.0)
    
    return render_template('result.html',query=query_url, results=results, page=page, num_pages=num_pages)






@app.route("/search", methods=['POST'])
def search():
    no_fields=True
    search_str = request.form['search_str']
    search_fields = ""
    fields = ['text', 'title', 'thread_title','author', 'country', 'site_url','type']
    weights = ['^1 ', '^2 ', '^2 ', '^3 ','^1 ', '^1.3 ','^1 '] #TODO add weigths
    for i, field in enumerate(fields):
        if field in request.form:
            search_fields += field + weights[i]
            no_fields=False
    if(no_fields):
        for i, field in enumerate(fields):
            search_fields += field + '^1 '
           
    query_url = build_url(search_str, search_fields)
    
    return redirect(url_for('results', query=query_url, page="1")) #TODO add pages

app.secret_key = os.urandom(24)
app.run(debug = True)



