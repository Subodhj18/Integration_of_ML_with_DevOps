#!/usr/bin/env python
# coding: utf-8

# In[21]:


import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras import backend as K
import numpy
import os



def model_train(epoch,n):
    batch_size = 32
    num_classes = 10
    epochs = epoch

    # input image dimensions
    img_rows, img_cols = 28, 28

    # loading the dataset and splitting into train and test sets
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)
    #changing datatype
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    #performing one hot encoding
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    #model creation
    model = Sequential()
    
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu',
                     input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    if n>1:
        model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_data=(x_test, y_test))
#     score = model.evaluate(x_test, y_test, verbose=0)
#     a=score*100
    model.save("MY_MNIST_MODEL.h5")
    os.system("mv /MY_MNIST_MODEL.h5 /MYCODE")
    return a





no_epoch=1
no_layer=1
accuracy_train_model=model_train(no_epoch,no_layer)

# scores = model.int(evaluate(x_test, y_test, verbose=1))
# print('Test loss:', scores[0])
# print('Test accuracy:', scores[1])

# accuracy_file = open('accuracy.txt','w')
f = open("accuracy.txt","w+")
# accuracy_file.write(str(scores[1]))
# accuracy_file.close()


f.write(str(accuracy_train_model[-1]))
f.close()
os.system("mv /accuracy.txt /MYCODE")
display_matter = open('accuracy_display.html','w+')
display_matter.write('<pre>\n---------------------------------------------\n')
display_matter.write('\nAccuracy achieved : ' + str(accuracy_train_model)+'\n</pre>')
display_matter.close()


# In[ ]:




