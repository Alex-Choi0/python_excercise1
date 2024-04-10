#Project04 QR코드 생성기

# pip install qrcode

import qrcode

import os

# file_path = r'chapter3/project4/qr코드모음.txt'

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = r'qr코드모음.txt'
print("file_path : ", file_path)
with open(file_path, 'rt', encoding='UTF8') as f :
  read_lines = f.readlines()

  for line in read_lines:
    line = line.strip()
    print(line)
    qr_data = line
    qr_img = qrcode.make(qr_data)
    save_path = qr_data + '.png'
    qr_img.save(save_path)

# qr_data = 'www.naver.com'
# qr_img = qrcode.make(qr_data)

# save_path = qr_data + '.png'
# qr_img.save(save_path)
