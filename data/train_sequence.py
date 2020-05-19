import tensorflow as tf
import pandas as pd
import os
import csv
from PIL import Image
from util.resize import resize_img
from util.encoder import Encoder


class TrainSequence(tf.keras.utils.Sequence):
    """
    TrainSequence

    Keras Sequence class for loading image and label data during training time. Note that data can be loaded
    much quicker if TfRecord format is used.
    """

    def __init__(self, img_path, label_path, desired_size=(64, 1024), encode_labels=True,
                 encode_max_seq_size=None, encode_char_set_path=None):
        """
        Setup necessary file paths and load csv data using pandas.

        :param img_path: The filepath to the images
        :param label_path: The filepath to the labels CSV
        :param desired_size: The shape all images will be resized and padded to
        :param encode_labels: T/F - Whether or not to receive labels as strings or indices
        :param encode_max_seq_size: Max sequence size as given in Encoder
        :param encode_char_set_path: Charset path as given in Encoder
        """
        if not os.path.exists(label_path):
            raise Exception('Label CSV not contained in', label_path)
        elif not os.path.exists(img_path):
            raise Exception('Image path does not exist in', img_path)

        if encode_labels:
            # A maximum sequence size must be specified if labels are to be encoded
            assert encode_max_seq_size is not None

            # A character set path must be specified if labels are to be encoded
            assert encode_char_set_path is not None and os.path.exists(encode_char_set_path)

            self.encoder = Encoder(encode_char_set_path, max_sequence_size=encode_max_seq_size)

        self.img_path = img_path
        self.desired_size = desired_size
        self.encode_labels = encode_labels
        self.df = pd.read_csv(label_path, header=None, sep='\t', names=['word', 'transcription'],
                              quoting=csv.QUOTE_NONE)

    def tensor_image(self, path):
        """
        Open an image file using PIL, resize it, and convert to tensor.

        :param path: Filepath to the image to be opened
        :return: The image as a tensor
        """
        img = Image.open(path)
        img = resize_img(img, self.desired_size)
        x = tf.constant(img, dtype=tf.float32)

        return x

    def __getitem__(self, index):
        """
        The method to index into the sequence to grab images and labels in tensor format.

        :param index: The index of the image/label to be retrieved
        :return: image and label as tensors
        """
        img = self.tensor_image(self.img_path + self.df['word'][index])
        img = tf.transpose(img)
        img = tf.constant(img, dtype=tf.float32)
        img = tf.expand_dims(img, 2)

        transcription = self.df['transcription'][index]

        if self.encode_labels:
            label = self.encoder.str_to_idxs(transcription)
            label = tf.constant(label, dtype=tf.int64)
        else:
            label = tf.constant(transcription, dtype=tf.string)

        return img, label

    def __len__(self):
        """
        The length of the sequence.

        :return: sequence length
        """
        return len(self.df)
