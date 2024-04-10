from gtts import gTTS
from playsound import playsound
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

# 나의 텍스트 경로로 바인딩 한다.
file_path = '나의텍스트.txt'

# vkdlfdmf ㄹ의 이름으로 오픈합니다. 한글로 작성된 파일을 열기 때문에 'rt', encoding='UTF8'형식으로 열어 글자가 깨지지 않게 하였습니다.
with open(file_path, 'rt', encoding='UTF8') as f :
  read_file = f.read() # 파일 전체 재용을 읽어 read_file 변수에 바인딩 합니다.

# with는 파일을 열고 종료되면 자동으로 파일을 닫습니다. 파일을 열 때 with를 사용하면 코드가 간결해 집니다.

tts = gTTS(text=read_file, lang='ko')
tts.save("myText.mp3")
playsound('myText.mp3')

# Linux(Ubuntu)에서 실행시
# sudo apt-get update
# sudo apt install python3-pip
# pip install gtts
# pip install playsound==1.2.2
