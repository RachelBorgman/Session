from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret and safe'

@app.route('/')
def create_visitor():
    if "visits" in session:
        session["visits"] = session["visits"] + 1
    else:
        session["visits"] = 0
    return render_template('index.html', number_of_visits=session['visits'])

@app.route('/plus_2')
def plus_2():
    if "visits" in session:
        session["visits"] = session["visits"] + 1
    else:
        session["visits"] = 0
    return redirect('/')

@app.route('/plus_x', methods=['POST'])
def plus_x():
    data = request.form
    x=int(data['number_visits'])
    if "visits" in session:
        session["visits"] = session["visits"] + int(x)
    else:
        session["visits"] = 0
    return render_template('index.html', number_of_visits=session['visits'], x=x)

@app.route('/destroy_session')
def destroy():
    session.clear()		# clears all keys
    return redirect('/')
    
if __name__=="__main__":   
    app.run(debug=True, host="localhost", port=8000)