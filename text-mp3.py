from gtts import gTTS
# 需要在翻墙的环境下运行
text = """
            hello
        """
print('开始转换')
tts = gTTS(text=text, lang='zh-tw')
# text：音频内容
# lang: 音频语言
tts.save("yinpin.mp3")
print("转换完成")

