import argparse
import numpy as np
import tensorflow as tf

def detect(model, img):
    # Load the TFLite model and allocate tensors
    interpreter = tf.lite.Interpreter(model)
    interpreter.allocate_tensors()
    
    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    # Test the model on random input data
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    interpreter.invoke()
    
    # get_tensor() returns a copy of the tensor data
    # use tensor() in order to get a pointer to the tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='models/yolov5s.pt', help='weights path')
    parser.add_argument('--img-size', nargs='+', type=int, default=[320, 320], help='image (height, width)')
    parser.add_argument('--batch-size', type=int, default=1, help='batch size')
    #parser.add_argument('--half', action='store_true', help='FP16 half-precision export')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    detect(opt)
