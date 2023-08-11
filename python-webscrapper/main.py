from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_jobs
from extractors.file import save_to_file

db = {
    
}

app = Flask("Jobscrapper") #플라스크 애플리케이션을 생성

@app.route("/") #URL과 플라스크 코드를 매핑하는 플라스크의 데코레이터. 바로 아래에 있는 함수를 실행시킨다.
def home():  #(keyword를 기준으로 링크 뒷부분이 달라짐)input을 submit했을 때, 해당 링크로 이동
    return render_template("home.html") #html문서 내의 변수를 지정 가능함 {{name}}으로 사용

@app.route("/search")
def search():
    keyword = request.args.get("keyword") #입력한 keyword를 get한다 -name을 keyword라 설정했기에
    if keyword == None:
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs) #{%%}는 html내에 python코드를 넣게 해준다.

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