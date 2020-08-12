# mobilenet
mobilenetV2 for detectron2<br>

example how to use:<br>

from mobilenet.utils import  add_mobilenet_config, build_mobilenetv2_fpn_backbone<br>
cfg = get_cfg()<br>

cfg.merge_from_file('mobilenet/configs/Base-RCNN-MobileNet-FPN_V1.yaml')<br>
add_mobilenet_config(cfg)<br>
cfg.MODEL.MOBILENET.NORM='FrozenBN'<br>
cfg.MODEL.MOBILENET.ACTIVATION='Mish'
