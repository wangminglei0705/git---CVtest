import cv2

# 1. 读取彩色图像
img = cv2.imread("dog.jpg")  # 替换成你的图片路径

# 2. 转换为灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 显示灰度图
cv2.imshow("灰度图", gray_img)
cv2.waitKey(0)  # 按任意键关闭窗口
cv2.destroyAllWindows()

# 4. 保存灰度图
cv2.imwrite("gray_output.jpg", gray_img)