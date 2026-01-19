from ultralytics import YOLO

# weights ஃபோல்டரில் உள்ள உங்கள் மாடலை லோடு செய்கிறது
model = YOLO("weights/custom_yolo_model.pt") 

# இமேஜை கொடுத்து ஸ்கேன் செய்தல்
results = model.predict("invoice_image.jpg")
