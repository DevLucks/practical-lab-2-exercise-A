from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
STUDENTS = {
    "1001": {"name": "Ada", "results": {"Math": "A", "Eng": "B+"}},
    "1002": {"name": "Tunde", "results": {"Math": "B-", "Eng": "A-"}}
}

@app.route("/")
def hello():
    return "Student-Staff Demo App"

@app.route("/ask", methods=["POST"])
def ask():
    # example: {"student_id": "1001", "query": "check results"}
    data = request.get_json(force=True)
    student_id = data.get("student_id")
    query = data.get("query", "").lower()

    if student_id not in STUDENTS:
        return jsonify({"reply": "Student not found"}), 404

    if "result" in query or "results" in query or "check my results" in query:
        return jsonify({"reply": "Please call /results with your student_id to get results."})
    return jsonify({"reply": "Course Advisor: How can I help you further?"})

@app.route("/results", methods=["GET"])
def results():
    # call like: /results?student_id=1001
    student_id = request.args.get("student_id")
    if not student_id or student_id not in STUDENTS:
        return jsonify({"error": "student_id required or not found"}), 400
    return jsonify({"student": STUDENTS[student_id]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
