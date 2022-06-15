# -*- coding: euc-kr -*-

'''
import wave
import os
import numpy as np 
import json
import array

local_list = ['Chungcheong']

def split_wav(local):
  file_list = os.listdir(r'C:\\Users\\capstone_02\\Downloads\\' + local + '\\Training\\')

  cnt = 0
  for index, x in enumerate(file_list): 
    w = wave.open(os.path.join(os.getcwd(), "noises", "sample",r'C:\\Users\\capstone_02\\Downloads\\' + local + "/Training/"+ x), "r")
    wavLen = w.getnframes() / w.getframerate()
    buffer = w.readframes(w.getnframes())
    amplitude = (np.frombuffer(buffer, dtype="int16"))

    with open('C:\\Users\\capstone_02\\Downloads\\' + local + '/label/' + os.path.splitext(x)[0] + ".json", encoding='utf-8-sig') as f:
        json_object = json.load(f)

    if os.path.isdir('C:\\Users\\capstone_02\\Downloads\\' + local + "\\cut\\"):
        pass
    else:
        os.mkdir('C:\\Users\\capstone_02\\Downloads\\' + local + "\\cut\\")


    for i in range(0, len(json_object['speaker'])):
        if check_birthplace(json_object, i, local) == True and check_length(json_object, i) == True:
            for i in range(len(json_object["utterance"])):

                s_amp = amplitude[int(json_object["utterance"][i]['start'] * w.getframerate() * w.getnchannels()):int(json_object["utterance"][i]['end'] * w.getframerate() * w.getnchannels())]
                save_wave = wave.Wave_write(os.path.join('C:\\Users\\capstone_02\\Downloads\\' + local + "\\cut\\" + str(cnt) + ".wav"))
                cnt += 1
                
                save_wave.setparams(w.getparams())
                save_wave.writeframes(array.array('h', s_amp).tobytes())
                save_wave.close()
                print(local + "의 " + str(cnt) + " 번째 오디오 분리 완료")



def check_birthplace(json_object, i, local):
    if (local == "Jeju" and (json_object["speaker"][i]["birthplace"] == '제주'))  or \
    (local == "Gangwon" and (json_object["speaker"][i]["birthplace"] == '강원')) or \
    (local == "Gyeongsang" and ((json_object["speaker"][i]["birthplace"] == '경상') or (json_object["speaker"][i]["birthplace"] == '부산') or (json_object["speaker"][i]["birthplace"] == '경남'))) or \
    (local == "Jeolla" and ((json_object["speaker"][i]["birthplace"] == '전라')) or  (json_object["speaker"][i]["birthplace"] == '전남')  or  (json_object["speaker"][i]["birthplace"] == '전북'))  or \
    (local == "Chungcheong" and (json_object["speaker"][i]["birthplace"] == '충청')): 
        return True
    else:
        return False

def check_length(json_object, i): 
    if abs(int(json_object["utterance"][i]['start']) - int(json_object["utterance"][i]['end'])) > 2:
        print(abs(int(json_object["utterance"][i]['start']) - int(json_object["utterance"][i]['end'])) > 2)
        return True
    else:
        return False

for local in local_list:
  split_wav(local)


import os
 
def changeName(path, cName):
    i = 1
    for filename in os.listdir(path):
        print(path+filename, '=>', path+str(cName)+str(i)+'.wav')
        os.rename(path+filename, path+str(cName)+str(i)+'.wav')
        i += 1

local_list = ['Jeju', 'Gangwon', 'Jeolla', 'Gyeongsang', 'Chungcheong']

for local in local_list:
    changeName('C:\\Users\\capstone_02\\Downloads\\' + local   + '\\cut\\',local + '_')



import os
import csv

f = open('DialectDataset.csv','a', newline='')
wr = csv.writer(f)


wav_list =  os.listdir("C:\\Users\\capstone_02\\Downloads\\dataset")


wr.writerow(['filename', 'label', 'local'])

cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for wav in wav_list: 
    if "Jeju" in wav and cnt_0 < 30000:
        wr.writerow([wav, 0, "Jeju"])
        cnt_0 += 1
    if "Gangwon" in wav and cnt_1 < 30000:
        wr.writerow([wav, 1, "Gangwon"])
        cnt_1 += 1
    if "Jeolla" in wav and cnt_2 < 30000:
        wr.writerow([wav, 2, "Jeolla"])
        cnt_2 += 1
    if "Gyeongsang" in wav and cnt_3 < 30000:
        wr.writerow([wav, 3, "Gyeongsang"])
        cnt_3 += 1
    if "Chungcheong" in wav and cnt_4 < 30000:
        wr.writerow([wav, 4, "Chungcheong"])
        cnt_4 += 1
f.close()



''' 
import shutil
import os


local_list = ['Jeju', 'Gangwon', 'Jeolla', 'Gyeongsang', 'Chungcheong']

cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for local in local_list:

    file_source = 'C:\\Users\\capstone_02\\Downloads\\dataset\\'

    if os.path.isdir('C:\\Users\\capstone_02\\Downloads\\dataset\\' + local):
        pass
    else:
        os.mkdir('C:\\Users\\capstone_02\\Downloads\\dataset\\' + local)

    file_destination = 'C:\\Users\\capstone_02\\Downloads\\dataset\\' + local

    get_files = os.listdir(file_source)
 
    for g in get_files:
        if "Jeju" in g and cnt_0 < 30000:
            shutil.move(file_source + g, file_destination)
            cnt_0 += 1
        if "Gangwon" in g and cnt_1 < 30000:
            shutil.move(file_source + g, file_destination)
            cnt_1 += 1
        if "Jeolla" in g and cnt_2 < 30000:
            shutil.move(file_source + g, file_destination)
            cnt_2 += 1
        if "Gyeongsang" in g and cnt_3 < 30000:
            shutil.move(file_source + g, file_destination)
            cnt_3 += 1
        if "Chungcheong" in g and cnt_4 < 30000:
            shutil.move(file_source + g, file_destination)
            cnt_4 += 1

        print(local + " 완료")



