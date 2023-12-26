from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import os

app = Flask(__name__)


# @app.route('/',methods=['GET'])
# def training():
#     os.system("python main.py")
#     return "Training Successful!" 



def gen_frames():  
    while True:
        model_path = 'evaluation/train/weights/best.pt'
        model = YOLO(model_path)
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        results = model.predict(frame)
        
        if results[0].boxes is not None:  
            for box in results[0].boxes.xyxy:
                x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3]) 
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  
                cv2.putText(frame, f"person", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) 

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
