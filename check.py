from flask import Flask, jsonify
import cv2
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def capture_images():
    cap = cv2.VideoCapture(0)
    captured_images = []

    for i in range(5):
        ret, frame = cap.read()
        if ret:
            image_name = f'image_{i + 1}.png'
            cv2.imwrite(image_name, frame)
            captured_images.append(image_name)
            time.sleep(1)  
        else:
            return jsonify({"error": "Failed to capture image"}), 500

    
    cap.release()
    cv2.destroyAllWindows()

    return jsonify({"captured_images": captured_images})

if __name__ == '__main__':
    app.run(debug=True)
