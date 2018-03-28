#!/usr/bin/env python3

import numpy as np
from .model.puzzle import setting, generate, states, transitions, generate_configs, successors
from .model.puzzle import validate_states, validate_transitions, to_configs
from .split_image import split_image
from .util import preprocess
import os

def setup():
    setting['base'] = 14

    def loader(width,height):
        base = setting['base']
        panels = split_image(os.path.join(os.path.dirname(__file__), "lenna.png"),width,height)
        stepy = panels.shape[1]//base
        stepx = panels.shape[2]//base
        panels = panels[:,:stepy*base,:stepx*base,]
        panels = panels.reshape((panels.shape[0],base,stepy,base,stepx))
        panels = panels.mean(axis=(2,4))
        panels = preprocess(panels)
        return panels

    setting['loader'] = loader
