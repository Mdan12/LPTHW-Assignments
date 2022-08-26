from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template, flash
from gothonweb import planisphere
from functools import wraps

app = Flask(__name__)
numpad_list = []
numpad_correct = ['1', '2', '3']
username = []
password = []
@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for("login"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        Uname = request.form.get('Uname')
        Pass = request.form.get('Pass')
        if request.form.get('login'):
            if Uname in username and Pass in password:
                session["logged_in"] = True
                session['room_name'] = planisphere.START
                return redirect(url_for("firstroom"))
            if Pass not in username or Uname not in username:
                return redirect(url_for("wrong"))


        if request.form.get('registerbtn'):
            return redirect(url_for('register'))

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route("/wrong", methods=['GET', 'POST'])
def wrong():
    if request.method == "GET":
        return render_template("wrong.html")
    else:
        return render_template("you_died.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")

    else:
        user = request.form.get('user')
        psw = request.form.get('psw')
        registerbtn = request.form.get('Register')
        if registerbtn:
            username.append(user)
            password.append(psw)
        return redirect(url_for('login'))



@app.route("/firstroom", methods=['GET', 'POST'])
@login_required
def firstroom():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")

    if request.method == "POST":
        if request.form.get('tell a joke'):
            session['room_name'] = planisphere.LASER
        elif request.form.get('dodge!'):
            session['room_name'] = planisphere.DODGE
        elif request.form.get('shoot!'):
            session['room_name'] = planisphere.SHOOT
        elif request.form.get('tryagain'):
            session['room_name'] = planisphere.START

        return redirect(url_for("secondroom"))


@app.route("/secondroom", methods=['GET', 'POST'])
@login_required
def secondroom():

    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")

    if request.method == "POST":

        if request.form.get('1'):
            numpad_list.append('1')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('2'):
            numpad_list.append('2')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('3'):
            numpad_list.append('3')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('4'):
            numpad_list.append('4')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('5'):
            numpad_list.append('5')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('6'):
            numpad_list.append('6')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('7'):
            numpad_list.append('7')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('8'):
            numpad_list.append('8')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('9'):
            numpad_list.append('9')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('0'):
            numpad_list.append('0')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('*'):
            numpad_list.append('*')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))
        if request.form.get('#'):
            numpad_list.append('#')
            if len(numpad_list) < 3:
                room = planisphere.load_room(room_name)
                return render_template("show_room.html", room=room)
            if len(numpad_list) == 3:
                 if numpad_list == numpad_correct:
                      session['room_name'] = planisphere.ONE
                      return redirect(url_for("thirdroom"))
                 else:
                     session['room_name'] = planisphere.STAR
                     return redirect(url_for("thirdroom"))

        if request.form.get('tryagain'):
            session['room_name'] = planisphere.START


@app.route("/thirdroom", methods=['GET', 'POST'])
@login_required
def thirdroom():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")
    if request.method == "POST":
        if request.form.get('throw the bomb'):
            session['room_name'] = plaisphere.BOMBA
        elif request.form.get('slowly place the bomb'):
            session['room_name'] = planisphere.BOMB
        elif request.form.get('tryagain'):
            session['room_name'] = planisphere.START
        return redirect(url_for("winner"))

@app.route("/winner", methods=['GET'])
@login_required
def winner():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")



app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWWQ5$/,?RT'

if __name__ == "__main__":
    app.run(debug=True)
