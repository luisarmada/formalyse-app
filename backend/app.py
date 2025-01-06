from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2
import atexit
import threading
# import psutil

# def log_memory_usage():
#     process = psutil.Process()
#     memory_info = process.memory_info()
#     print(f"Memory usage: {memory_info.rss / 1024 ** 2:.2f} MB")

camera_lock = threading.Lock()


app = Flask(__name__)
CORS(app)

camera = None  # Global camera variable

def generate_frames():
    global camera
    with camera_lock:
        try:
            while True:
                if camera is None or not camera.isOpened():
                    break

                success, frame = camera.read()
                if not success:
                    print("Failed to read frame from the camera.")
                    break

                _, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        except Exception as e:
            print(f"Error in generate_frames: {e}")
        finally:
            print("Stopping frame generation.")



@app.route('/video')
def video_feed():
    global camera
    if camera is None or not camera.isOpened():
        return "Camera not activated", 400

    def stream():
        try:
            yield from generate_frames()
        except GeneratorExit:
            print("Client disconnected.")
        finally:
            print("Stopping video stream.")

    return Response(stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global camera

    # Extract slug from the request body
    data = request.json
    slug = data.get("slug", None)  # Default to None if slug is not provided

    if slug:
        print(f"Received slug: {slug}")  # Print the slug to the terminal
    else:
        print("can't find slug")

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


is_shutting_down = False  # Track shutdown state

def cleanup_resources():
    global camera, is_shutting_down
    is_shutting_down = True
    if camera is not None:
        camera.release()
        cv2.destroyAllWindows()
        camera = None
        print("Camera released during app shutdown.")

# Register cleanup for actual app shutdown
atexit.register(cleanup_resources)

@app.teardown_appcontext
def teardown(exception=None):
    global is_shutting_down
    if is_shutting_down:
        print("Teardown during shutdown.")
        return  # Cleanup already handled in `atexit`
    print("Teardown after request - no action taken.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
