import torch

weights_path = r"C:\Users\user\OneDrive\Desktop\face\Sign-Object-Detection-E2E\yolov5\bestmodel.pt"
model = torch.load(weights_path, map_location="cpu")
print(model)
