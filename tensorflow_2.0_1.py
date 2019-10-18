import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
hello = tf.constant('Hello, TensorFlow!')
print(hello)
