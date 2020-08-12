# -*- coding: utf-8 -*-
# Modified by DDzialkowski 2020, norm choice added

from detectron2.config import CfgNode as CN


def add_mobilenet_config(cfg):
    _C = cfg

    _C.MODEL.MOBILENET = CN()

    _C.MODEL.MOBILENET.VERSION = 2
    _C.MODEL.MOBILENET.CONV_BODY = "V-39-eSE"
    _C.MODEL.MOBILENET.OUT_FEATURES = ["stage2", "stage3", "stage4", "stage5"]

    # Options: FrozenBN, GN, "SyncBN", "BN"
    _C.MODEL.MOBILENET.NORM = "BN"

    _C.MODEL.MOBILENET.OUT_CHANNELS = 256

    _C.MODEL.MOBILENET.BACKBONE_OUT_CHANNELS = 256
