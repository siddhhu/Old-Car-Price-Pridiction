from flask import Flask,render_template,request
import smtplib 

app = Flask(__name__, template_folder='templates')


@app.route("/",methods=["GET","POST"])
def hello():
    if request.method=="POST":
        subject=request.form['subject']
        receiver=request.form['receiver']
        text=request.form['message']
        message=f'Subject: {subject}\n\n{text} '
        print(message)
        # Python code to illustrate Sending mail from 
# your Gmail account 

# creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
        s.starttls() 

# Authentication 
        s.login("user_gmail", "user_password") 

# message to be sent 
       
# sending the mail 
        s.sendmail("receiver_gmail", receiver, message) 

# terminating the session 
        s.quit() 

    else:
        return render_template('index.html')
    return render_template('new.html')

        
    

if __name__ == "__main__":
    app.run(debug=True)