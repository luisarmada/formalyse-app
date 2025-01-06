from flask import Flask, request, send_file
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import io

app = Flask(__name__)

# Load a base body template image (ensure this image exists in the same directory)
base_image_path = "body_template.png"
highlight_color = (0, 140, 255, 128)  # Blue highlight with transparency

@app.route('/generate-body-chart', methods=['GET'])
def generate_body_chart():
    muscles = request.args.getlist('muscles')  # e.g., ['chest', 'biceps']

    # Open base image
    img = Image.open(base_image_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    # Example muscle group positions (dummy bounding boxes for testing)
    muscle_positions = {
        "chest": [(100, 100, 200, 150)],
        "biceps": [(70, 160, 90, 200), (210, 160, 230, 200)]
    }

    # Draw highlights on the overlay for specified muscles
    for muscle in muscles:
        if muscle in muscle_positions:
            for box in muscle_positions[muscle]:
                draw.rectangle(box, fill=highlight_color)

    # Combine base image with overlay
    combined = Image.alpha_composite(img, overlay)

    # Save image to a BytesIO object
    img_io = io.BytesIO()
    combined.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
