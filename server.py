from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB Connection
MONGO_URI = "mongodb+srv://tushita_p07:Game%40007@cluster0.qec13jd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["parkingDB"]
parking_slots = db["slots"]

# Initialize Slots (Run once)
def initialize_slots():
    if parking_slots.count_documents({}) == 0:
        slots = [{"id": i, "status": "available"} for i in range(1, 11)]
        parking_slots.insert_many(slots)

initialize_slots()

# Get all parking slots
@app.route("/slots", methods=["GET"])
def get_slots():
    slots = list(parking_slots.find({}, {"_id": 0}))
    return jsonify(slots)

# Book a parking slot
@app.route("/book", methods=["POST"])
def book_slot():
    data = request.json
    slot_id = data.get("id")

    if parking_slots.find_one({"id": slot_id, "status": "occupied"}):
        return jsonify({"error": "Slot already occupied"}), 400

    parking_slots.update_one({"id": slot_id}, {"$set": {"status": "occupied"}})
    return jsonify({"message": "Slot booked successfully"})

if __name__ == "__main__":
    app.run(debug=True)
