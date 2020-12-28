from flask import Flask, url_for, request, redirect, abort, jsonify
from LessonsDao import lessonDao

app = Flask(__name__, static_url_path="", static_folder="staticpages")

# Get All
@app.route("/lessons")
def getAll():
    return jsonify(lessonDao.getAll())

@app.route("/lessons/<int:id>")
def findById(id):
    return jsonify(lessonDao.findById(id))

@app.route("/lessons", methods=["POST"])
def create():
    if not request.json:
        abort(400)
    
    lessons = {
        "id": request.json["id"],
        "lecturer": request.json["lecturer"],
        "subject": request.json["subject"],
        "delivered": request.json["delivered"],
        "price": request.json["price"]
    }
    return jsonify(lessonDao.create(lessons))

@app.route("/lessons/<int:id>", methods=["PUT"])
def update(id):
    foundLessons = lessonDao.findById(id)   
    if foundLessons == {}:
        return jsonify({}), 404
    currentLesson = foundLessons
    if "lecturer" in request.json:
        currentLesson["lecturer"] = request.json["lecturer"]
    if "subject" in request.json:
        currentLesson["subject"] = request.json["subject"]
    if "delivered" in request.json:
        currentLesson["delivered"] = request.json["delivered"]
    if "price" in request.json:
        currentLesson["price"] = request.json["price"]
    lessonDao.update(currentLesson)

    return jsonify(currentLesson)

@app.route("/lessons/<int:id>", methods=["DELETE"])
def delete(id):
    lessonDao.delete(id)
    return jsonify({"done": True})



if __name__ == "__main__":
    app.run(debug=True)