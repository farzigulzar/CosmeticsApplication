from flask import Flask, render_template, request, send_file, jsonify
import base64
import cv2 as cv
import json
import numpy as np


app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to receive captured frame and send it back
@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    frame_data = data['frame']

    # Dedcoding the received json string
    encoded_data = frame_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    frame = cv.imdecode(nparr, cv.IMREAD_COLOR)
    

    # cv.imwrite('captured_frame.jpg', frame)

    print('showing imshow frames')
    cv.imshow('Captured Frame', frame)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # Process the frame data as needed
    # Example: Save the frame as an image file or perform other operations
    return jsonify({'message': 'Frame received and processed.'})

# Route to send a live frame to the client
@app.route('/receive-frame')
def receive_frame():
    # Example: Read an image file and send it to the client
    with open('live_frame.jpg', 'rb') as f:
        return send_file(f, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
    # print('printing main')

    # while 1:
    #     cv.imshow('frame', capture.frame_data)
    #     print('printing while 1')
    #     if (cv.waitKey(1) & 0xFF == ord('Q')):
    #         break

    # cv.destroyAllWindows()