from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2
import atexit
import threading
import mediapipe as mp

camera_lock = threading.Lock()

app = Flask(__name__)
CORS(app)

camera = None  # Global camera variable
draw_landmarks = True  # Landmarks enabled by default

# Initialize MediaPipe pose solution
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

def generate_frames():
    global camera, draw_landmarks
    with camera_lock:
        try:
            while True:
                if camera is None or not camera.isOpened():
                    break

                success, frame = camera.read()
                if not success:
                    print("Failed to read frame from the camera.")
                    break

                # Convert the frame to RGB for MediaPipe processing
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = pose.process(frame_rgb)

                # Draw landmarks if enabled
                if draw_landmarks and results.pose_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
                    )

                # Encode the frame as JPEG
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
        print("Can't find slug")

    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)  # Open the camera
        if not camera.isOpened():
            print("Camera failed to open.")
            return jsonify({"status": "error", "message": "Failed to open camera"}), 500
        else:
            # Reduce resolution and frame rate for performance
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            camera.set(cv2.CAP_PROP_FPS, 15)
            print("Camera opened.")
    else:
        print("Cam already opened.")
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

@app.route('/toggle_landmarks', methods=['POST'])
def toggle_landmarks():
    global draw_landmarks
    data = request.json
    draw_landmarks = data.get("enabled", True)
    print(f"Landmarks drawing {'enabled' if draw_landmarks else 'disabled'}.")
    return jsonify({"status": "success", "landmarks_enabled": draw_landmarks})

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
