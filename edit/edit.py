from moviepy.editor import *
from moviepy.video.fx.resize import resize

import numpy as np
from moviepy.config import change_settings

movie = "../youtubedl/movie/けす記憶チャレンジ「わっきゃいの小腸」.mp4"

c = VideoFileClip(movie)
wide = c.w
hight = c.h

total = wide + hight
rate = 16 + 9

shortSize = (720,405)
shortBaseSize = (1280,720,3)
normalSize = (1280,720)
#creat_H = (total / rate ) * 16

baseImage = np.full(shortBaseSize,[0,0,0])
baseClip = ImageClip(baseImage).set_duration(20)

creat_W = (total / rate ) * 9
creat_H = (creat_W / 16 ) * 9




print("wide",wide)
print("hight",hight)
print("total ",total)
print("creat_H",creat_H)
print("creat_W",creat_W)

clip1 = VideoFileClip(movie).subclip(0, 10).resize(shortSize).set_pos(('center','center'))
clip2 = VideoFileClip(movie).subclip(20 ,30 ).resize(shortSize).set_pos(('center','center'))

TEXT = 'テスト'
#TEXT = 'test'
textSize = 70
textColor = 'blue'
# textPosition = (shortSize[1] / 2,shortSize[0] - (shortSize[0] /2)  )
#textPosition = (shortBaseSize[0] - 70,shortBaseSize[1]- 70)
#textPosition = ('left', 'bottom')
#textPosition = ('center', 'bottom')
textPosition = (720 / 2 - textSize,1280 / 3 + 405 + textSize)
textDuration = 10
#textFont = 'Xolonium-Bold'
textFont ='/usr/share/fonts/truetype/fonts-japanese-mincho.ttf' #sudo apt install -y fonts-ipafont #fc-list
#change_settings({"IMAGEMAGICK_BINARY": r"/etc/ImageMagick-6/policy.xml"})
txt_clip =TextClip(TEXT,fontsize=textSize,color=textColor,font=textFont).set_position(textPosition).set_duration(textDuration)

# txt_clip = (TextClip("TEST", fontsize=70, color='blue')
#             .set_position('center')
#             .set_duration(10))

print("resuze")



#clip1 = resize(clip1 ,(creat_W,creat_H ))
#clip2 = resize(clip2 ,(creat_W,creat_H ))

#clip1 = resize(clip1 ,(total * (9 / 25) ,total * (16 / 25) ))
#clip2 = resize(clip2 ,(total * (9 / 25) ,total * (16 / 25) ))

print("concatenatevideoclips")

#final_clip = concatenate_videoclips([baseClip,clip1, clip2])
final_clip = CompositeVideoClip([baseClip,clip1, clip2,txt_clip])

print("write_videofile")

final_clip.write_videofile("chaplin.mp4", fps=25)  # 編集した結果を保存する