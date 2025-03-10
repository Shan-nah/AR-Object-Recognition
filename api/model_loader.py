import torch
from torchvision import models

def load_model():
    model = models.resnet50(pretrained=True)
    model.eval()
    return model

if __name__ == "__main__":
    model = load_model()
    print("Model Loaded Successfully")
