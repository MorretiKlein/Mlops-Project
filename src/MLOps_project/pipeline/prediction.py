import cv2
from ultralytics import YOLO

model_path = 'evaluation/train/weights/best.pt'
model = YOLO(model_path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model.predict(frame)
    
    if results[0].boxes is not None:  
        for box in results[0].boxes.xyxy:
            x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3]) 
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  
            cv2.putText(frame, f"person", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) 

    cv2.imshow('person Prediction', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
