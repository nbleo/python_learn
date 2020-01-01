#! /usr/local/bin/python3

import cv2

# 获取头像和logo， 是BGR 格式数据格式在 0-255
img_head = cv2.imread("/Users/leo/Desktop/Python/python_learn/add_flag_to_photo/head.jpg")
img_logo = cv2.imread("/Users/leo/Desktop/Python/python_learn/add_flag_to_photo/logo.jpg")

# 获取头像和logo的宽度
# shape 读取图像的具体形状
w_head, h_head = img_head.shape[:2]
w_logo, h_logo = img_logo.shape[:2]

# 计算图案缩放比例
scale = w_head / w_logo / 4

# 缩放图像
img_flag = cv2.resize(img_logo, (0, 0), fx=scale, fy=scale)

# 获取缩放图像的新宽度
w_flag, h_flag = img_flag.shape[:2]

# 按3个通道合并图片
for c in range(0, 3):
    img_head[w_head - w_flag:, h_head - h_flag:, c] = img_flag[:, :, c]

# 保存
cv2.imwrite("/Users/leo/Desktop/Python/python_learn/add_flag_to_photo/new_head.jpg", img_head)
