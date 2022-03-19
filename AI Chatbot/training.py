import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
from tf.keras.models import Sequential
from tf.keras.layers import Dense, Activation, Dropout
from tf.keras.optimizers import SGD