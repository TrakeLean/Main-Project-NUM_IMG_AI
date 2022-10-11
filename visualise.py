# Visualise image tensor 0 to 9
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.datasets import mnist
x = 0
(X_train, y_train), (X_test, y_test) = mnist.load_data()
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
train_dataset = train_dataset.shuffle(len(train_dataset))
#train_dataset = train_dataset.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)

for (img, label) in train_dataset:
    number = 2
    if label.numpy() == number:
        plt.imshow(img, cmap='Greys')
        plt.show()
        print(img.numpy(), label.numpy())
        x+=1
        print('')
        print('---'*30)
        print('')
        break