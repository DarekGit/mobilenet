# mobilenet
mobilenetV2 for detectron2

example how to use:

from mobilenet.utils import  add_mobilenet_config, build_mobilenetv2_fpn_backbone
cfg = get_cfg()

cfg.merge_from_file('mobilenet/configs/Base-RCNN-MobileNet-FPN_V1.yaml')
add_mobilenet_config(cfg)
cfg.MODEL.MOBILENET.NORM='FrozenBN'
cfg.MODEL.MOBILENET.ACTIVATION='Mish'
