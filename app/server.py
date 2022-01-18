from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
import math

app = Flask(__name__,template_folder='template')


def build_url(search_str, fields, system,sort_field, sort_order):
    
    
    q = "*:*"
    sort_str = f"{sort_field} {sort_order}"
    url = f"http://localhost:8983/solr/{system}/select?defType=edismax&q.op=OR&q={search_str}&qf={fields}&sort={sort_str}&indent=true&rows=10"
    
    return url

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results")
def results():

    page = request.args.get('page')
    query= request.args.get('query')
    query_url = query +  f"&start={(int(page) - 1) * 10}"
    response = requests.get(query_url).json()['response']
    results = response['docs']
    num_docs = response['numFound']
    num_pages = math.ceil(num_docs / 10.0)
    return render_template('result.html',query=query, results=results, page=page, num_pages=num_pages)


@app.route("/article/<article_id>")
def article(article_id):
    pass
    url = f"http://localhost:8983/solr/system3/select?q=id:{article_id}&q.op=OR&indent=true&fl=*,%20score,%20%5Bchild%5D"
    query_res = requests.get(url).json()['response']
    if query_res['numFound'] == 0:
        print("Error, no results found")

    article = query_res['docs'][0]

    return render_template('article.html', result=article)




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

    system = request.form['system']   
    sort_field = request.form['sortField']
    sort_order = request.form['sortOrder']
    query_url = build_url(search_str, search_fields, system,sort_field, sort_order)
    

    return redirect(url_for('results', query=query_url, page="1")) #TODO add pages

app.secret_key = os.urandom(24)
app.run(debug = True)



