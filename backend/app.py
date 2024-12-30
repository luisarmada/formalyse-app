from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2
import atexit

def cleanup_camera():
    global camera
    if camera is not None:
        camera.release()
        camera = None
        cv2.destroyAllWindows()
        print("Camera released during app shutdown.")

# Register the cleanup function
atexit.register(cleanup_camera)


app = Flask(__name__)
CORS(app)

camera = None  # Global camera variable

def generate_frames():
    global camera
    while True:
        if camera is None or not camera.isOpened():
            break

        success, frame = camera.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/video')
def video_feed():
    global camera
    if camera is None or not camera.isOpened():
        if camera is None:
            print("Camera is none bruh")
        elif not camera.isOpened():
            print("Camera not opened bruh")
        else:
            print("What the sigma")
        return "Camera not activated", 400
            
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)  # Open the camera
        if not camera.isOpened():
            print("Camera failed to open.")
            return jsonify({"status": "error", "message": "Failed to open camera"}), 500
        else:
            print("Camera opened.")
    else:
        print("Cam already opened..")
    return jsonify({"status": "success", "message": "Camera activated"})


@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    global camera
    if camera is not None:
        camera.release()  # Release the camera
        cv2.destroyAllWindows()  # Ensure all OpenCV windows are destroyed
        camera = None
        print("Camera successfully released.")
    else:
        print("Camera was already released or not initialized.")
    return jsonify({"status": "success", "message": "Camera deactivated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
