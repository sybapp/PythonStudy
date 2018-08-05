
# 调用所需要的库
import PIL
from PIL import ImageFont, Image, ImageDraw

# 设置字体
font = ImageFont.truetype("arial.ttf",50)

# 打开要处理的文件
img = Image.open('img.jpg')

# 开始处理文件
draw = ImageDraw.Draw(img)

# 获取图片的宽高
width, height = img.size

# 设置处理的参数
draw.text((0, 0), '中文', font=font)

# 保存文件
img.save('out.jpg')


