#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 02:33:28 2020

@author: yazeed
"""

import cv2 
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # for loading in images
import helpers # helper functions


IMAGE_DIR_TRAINING = "traffic_light_images/training/"
IMAGE_DIR_TEST = "traffic_light_images/test/"
IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TRAINING)
selected_image = IMAGE_LIST[0][0]
plt.imshow(selected_image)

