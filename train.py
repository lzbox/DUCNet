import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(f'ultralytics/cfg/models/DUCNet.yaml')
    model.train(data='./dataset.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=0,
                workers=4,
                optimizer='SGD',
                project='runs/train',
                name="DUCNet",
                )
