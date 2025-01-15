import os
import shutil
import glob
from flask import Flask, jsonify, render_template, Response, request
from flask_cors import CORS, cross_origin
from signLang.pipeline.training_pipeline import TrainingPipeline
from signLang.utils.main_utils import decodeImage, encodeImageIntoBase64

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train")
def trainRoute():
    try:
        obj = TrainingPipeline()
        obj.run_pipeline()
        return "Training successful!"
    except Exception as e:
        return str(e)


@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("cd yolov5 && python detect.py --weights best.torchscript --img 416 --conf 0.25 --source ../data/inputImage.jpg")

        # Dynamically get the latest output image
        output_dir = max(glob.glob("yolov5/runs/detect/*"), key=os.path.getctime)
        output_image = os.path.join(output_dir, "inputImage.jpg")
        
        opencodedbase64 = encodeImageIntoBase64(output_image)
        result = {"image": opencodedbase64.decode('utf-8')}
        
        # Clean up
        shutil.rmtree("yolov5/runs", ignore_errors=True)
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify(result)





@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.torchscript --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080, debug=True)


# import os, sys
# from signLang.pipeline.training_pipeline import TrainingPipeline
# # from signLang.utils.main_utils import decodeImage, encodeImageIntoBase64

# obj = TrainingPipeline()
# obj.run_pipeline()
