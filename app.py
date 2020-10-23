from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# db =SQLAlchemy(app)


home_routes = (
    <h1>The following routes are available</h1> </p>
    <ul> 
        <li> "/api/v1.0/precipitation" </li>
        <li> "/api/v1.0/stations" </li>
        <li> "/api/v1.0/tobs" </li>
        <li>"/api/v1.0/<start>" </li>
        <li> "/api/v1.0/<start>/<end>"</li>
    </ul> 
)


@app.route("/")
def html(): 
    return """
    <h1>The following routes are available</h1>
    <ul> 
        <li>/api/v1.0/precipitation</li>
        <li>/api/v1.0/stations</li>
        <li>/api/v1.0/tobs</li>
        <li>/api/v1.0/<start></li>
        <li>/api/v1.0/<start>/<end></li>
    </ul> 
    """

@app.route("/api/v1.0/precipitation")
def precipitation():
    return "test"

@app.route("/api/v1.0/stations")
def stations():
    return "test"

@app.route("/api/v1.0/tobs")
def tobs():
    return "test"

@app.route("/api/v1.0/<start>")
def api():
    return "test"

@app.route("/api/v1.0/<start>/<end>")
def end():
    return"test"


#  try: 
#         name = request.json.get("name")
#         age = int(request.json.get("age"))
#         new_pet = Pet(name=name, age=age)
#         db.session.add(new_pet)
#         db.session.commit(new_pet)
#         return {"msg": "Success"}
#     except Exception as e:
#         return {"error": e}

# /api/v1.0/<start> and /api/v1.0/<start>/<end>

if __name__ == "__main__":
    app.run(debug=True)