#!/usr/bin/python3
from flask import Flask, request, render_template, make_response, redirect, url_for # 라이브러리 임포트

app = Flask(__name__) # 플라스크 기본 설정

try: # Try Catch문 Try를 먼저 시도하고 실패 시 except문을 실행한다.
    FLAG = open('./flag.txt', 'r').read() #flag.txt 파일을 오픈하여 FLAG라는 변수에 담는다.
except: #except문 실행
    FLAG = '[**FLAG**]' #플래그 불러오기 오류 시 [**FLAG**]라고 FLAG를 설정

users = { #유저 테이블이다.
    'guest': 'guest', #guest 계정
    'admin': FLAG #admin 계정
}

@app.route('/') #라우트, 웹서버의 필수라고 볼 수 있다. 웹사이트에서 naver.com 으로 접속 시 route('/')으로 접속되는 것이라고 볼 수 있다.
def index(): #인덱스(루트) 페이지를 보여주기 위한 함수
    username = request.cookies.get('username', None) #사용자의 브라우저에서 username이라는 이름의 쿠키를 불러온다. 없으면 None를 채운다.
    if username: #만약 username이 있다면?
        return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')
        #index.html을 반환하는데, text 옵션을 같이 넘긴다.
        #Hello {username}은 Hello하고 사용자의 아이디를 띄워준다는 뜻이다.
        #만약 username이 admin이라면 FLAG 값을 띄워주고, 아니라면 you are not admin이라고 띄워준다.
    return render_template('index.html') #username이 없다면 index.html을 그냥 반환한다.
    #여기서 반환이란, 사용자의 브라우저에 띄워주는 페이지를 말한다.

@app.route('/login', methods=['GET', 'POST']) #위에서 route('/')가 인덱스 페이지였다면, route('login')은 naver.com/login과 같다.
def login(): #로그인 페이지를 보여주기 위한 함수
    if request.method == 'GET': #만약 브라우저에서 요청한 Method가 GET이라면?
        return render_template('login.html') #login.html 페이지를 반환해준다.
    elif request.method == 'POST': #만약 POST라면?
        username = request.form.get('username') #사용자가 입력한 아이디를 username 변수에 넣고,
        password = request.form.get('password') #비밀번호를 password 함수에 넣는다.
        try: #다시 try catch문이 나왔네요!
            pw = users[username] #users 테이블 안에 username 넣어 요청을 하면 password를 반환해준다. 이 값을 pw라는 함수에 넣는다.
        except: #만약 실패했다면?
            return '<script>alert("not found user");history.go(-1);</script>' #"not found user"라고 팝업을 띄워줍니다.
        if pw == password: #만약 pw가 사용자가 입력한 비밀번호와 같다면?
            resp = make_response(redirect(url_for('index')) ) #index 페이지로 리다이렉트 하고,
            resp.set_cookie('username', username) #쿠키에 username을 써준다!
            return resp #브라우저로 반환!
        return '<script>alert("wrong password");history.go(-1);</script>' #만약 같지 않다면 "wrong password"를 띄워준다!

app.run(host='0.0.0.0', port=8000) #플라스크 실행!
