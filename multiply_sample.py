import os
import sys
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

NUM_OF_OPERATIONS = 1
if len(sys.argv) >= 2:
    NUM_OF_OPERATIONS = int(sys.argv[1])

BATCH_SIZE = 1
IMAGE_SIZE = 1024
IMAGE_CHANNEL = 4

images = tf.truncated_normal([BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNEL], 0.0, 0.5, dtype=tf.float32)
filters = tf.truncated_normal([BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNEL], 0.0, 0.5, dtype=tf.float32)
converted_images = tf.multiply(images, filters)

with tf.Session() as sess:
    for i in range(0, NUM_OF_OPERATIONS):
        data = sess.run(converted_images)

    print(NUM_OF_OPERATIONS, end="")
