from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_jobs
from extractors.file import save_to_file

db = {
    
}

app = Flask("Jobscrapper") #�ö�ũ ���ø����̼��� ����

@app.route("/") #URL�� �ö�ũ �ڵ带 �����ϴ� �ö�ũ�� ���ڷ�����. �ٷ� �Ʒ��� �ִ� �Լ��� �����Ų��.
def home():  #(keyword�� �������� ��ũ �޺κ��� �޶���)input�� submit���� ��, �ش� ��ũ�� �̵�
    return render_template("home.html") #html���� ���� ������ ���� ������ {{name}}���� ���

@app.route("/search")
def search():
    keyword = request.args.get("keyword") #�Է��� keyword�� get�Ѵ� -name�� keyword�� �����߱⿡
    if keyword == None:
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs) #{%%}�� html���� python�ڵ带 �ְ� ���ش�.

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword,db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1")