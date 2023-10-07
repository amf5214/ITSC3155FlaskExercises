from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with app.app_context():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registration.db"
    options = ["Association for Information Systems", "Marketing Club", "Business Law Club"]
    db = SQLAlchemy(app)

    class Club_Registration(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        student_name = db.Column(db.String(200), nullable=True)
        student_id = db.Column(db.String(40), nullable=False)
        club_registered = db.Column(db.String(200), nullable=False, default="error")

        def __repr__(self):
            return f"<Club_Registration {self.id}>"

    db.create_all()


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        new_registration = Club_Registration(student_name = str(request.form["name"]), student_id = str(request.form["student-id"]), club_registered = str(request.form.get("club")))

        try:
            db.session.add(new_registration)
            db.session.commit()
            print("Current Registrations ", Club_Registration.query.order_by(Club_Registration.id).all())
            return redirect('/')

        except:
            print("Current Registrations ", Club_Registration.query.order_by(Club_Registration.id).all())
            return "There was an error registering for this club"

    else:
        return render_template("index.html", options=options)

@app.route('/registrations', methods=["GET"])
def show_reg():
    registrations = Club_Registration.query.order_by(Club_Registration.id).all()
    print(registrations)
    return render_template("registrations.html", registrations=registrations, admin=True)

@app.route('/delete/<int:rowid>')
def delete_id(rowid):
    reg_to_delete = Club_Registration.query.get_or_404(rowid)

    try:
        db.session.delete(reg_to_delete)
        db.session.commit()
        return redirect('/registrations')
    
    except:
        return "There was an error deleting the registration"

if __name__ == '__main__':
   app.run(debug=True, port=54913)
   