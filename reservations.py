from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for reservations
reservations = []

# Route to add a reservation
@app.route('/api/reservations', methods=['POST'])
def add_reservation():
    data = request.json
    customer_name = data.get('customerName')
    reservation_time = data.get('reservationTime')

    if customer_name and reservation_time:
        reservation = {'customerName': customer_name, 'reservationTime': reservation_time}
        reservations.append(reservation)
        return jsonify({"message": "Reservation added successfully!", "reservation": reservation}), 201
    else:
        return jsonify({"error": "Please provide both customer name and reservation time."}), 400

# Route to view all reservations
@app.route('/api/reservations', methods=['GET'])
def view_reservations():
    return jsonify(reservations), 200

if __name__ == '__main__':
    app.run(debug=True)
