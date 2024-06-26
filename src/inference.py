import os
from ultralytics import YOLOv10
import cv2
import time
from tqdm import tqdm
import torch

class HelmetDetectionModel:
    def __init__(self, model_path):
        self.model = YOLOv10(model_path)

    def predict(self, image_path):
        return self.model(source=image_path)[0]

def load_model(model_path):
    return HelmetDetectionModel(model_path)

def run_inference_single(model, image_path):
    pred = model.predict(image_path)
    return pred

def run_inference_dir(model, test_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    img_files = [img_file for img_file in os.listdir(
        test_dir) if img_file.endswith(('.png', '.jpg', '.jpeg'))]

    for img_file in tqdm(img_files, 
                         desc='Processing images',
                         leave=True, 
                         ncols=100):
        img_path = os.path.join(test_dir, img_file)
        img_out = model.predict(img_path)
        img_out.save(os.path.join(
            output_dir, f'{os.path.splitext(img_file)[0]}_pred.png'))

    print(f'Inference completed. Results are saved in {output_dir}.')


if __name__ == '__main__':
    start_time = time.time()
    start_time_str = time.strftime("%Y/%m/%d %H:%M", time.localtime(start_time))
    print('-------------------------------------')
    print('Running Inference script at', start_time_str, '\n')

    MODEL_PATH = '../models/best1.pt'
    TEST_DIR = '../data/test/images'
    OUTPUT_DIR = '../assets/output_images'
    model = load_model(MODEL_PATH)
    run_inference_dir(model, TEST_DIR, OUTPUT_DIR)

    end_time = time.time()
    end_time_str = time.strftime("%Y/%m/%d %H:%M", time.localtime(end_time))
    print('\nDone with Inference at', end_time_str)
