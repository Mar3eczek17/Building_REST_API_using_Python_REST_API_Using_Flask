from flask import Flask, jsonify

app = Flask(__name__)


courses = [{'name': "Python Programming Certification",
            'course_id': "0",
            'Description': "Python programming certification helps you learn"
                           "python in the structured learning path with innovative "
                           "out of the box projects matching the industry standards",
            'price': "visit Edureka.co to know more"},
            {'name': "PData Science With Python Certification",
            'course_id': "1",
            'Description': "Data science with python helps you master the data science "
                           "life cycle processes in a structured learning path",
            'price': "AI and Machine Learning Certification"},
           {'course_id': "2",
            'Description': "AI and ML cetification will help you master AI/ML with "
                           "top notch projects like speechrecognition, chatbots, etc.",
            'price': "cisit edureka.co to know more"},
           {'name': "Python Spark Certification",
            'course_id': "3",
            'Description': "ySpark Certification Traning is designed to procide you the knowladge and akillsr "
                           "that are required to become a successful Spark Developer using Python and prepare "
                           "you for the Clouders Hadoop and Spark Developer Certification Exam",
            'price': "visit edureka.co to know more"},
           {'name': "Natural Language Processing With Python Certification",
            'course_id': "4",
            'Description': "Natural Language Processing with Python course will take you through the essential "
                           "of txt processing all the way up to classifying texts using Macine Larning algorithms.",
            'price': "visit edureka.co to know more"}
           ]


@app.route('/')
def index():
    return "Welcom To The Course API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'Courses': courses[course_id]})

@app.route("/courses", methods=['POST'])
def create():
    course = {'name': "Natural Language Processing With Python Certification",
            'course_id': "5",
            'Description': "Natural Language Processing with Python course will take you through the essential "
                           "of txt processing all the way up to classifying texts using Macine Larning algorithms.",
            'price': "visit edureka.co to know more"}
    courses.append(course)
    return jsonify({'Created': course})

@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({'course':courses[course_id]})

@app.route("/courses/<int:course_id>", methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)