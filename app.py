from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def registration():
    return render_template('registration.html')

@app.route('/submit',methods=['POST'])
def success():

    username=request.form['username']
    email=request.form['email']
    password=request.form['password']
    return render_template('success.html',username=username,email=email,password=password)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
