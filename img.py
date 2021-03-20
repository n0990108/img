#!/user/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image
import os

for file in os.listdir('orig'):
	if file.endswith('.jpg'):
		img = Image.open(os.path.join('orig', file))   # 读取图片
		img = img.convert("L")   # 转化为黑白图片
		img.save(os.path.join('result', file[:-4] + '_grey.png'))   # 存储图片