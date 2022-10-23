import os
import time


exe_path = r"exeFile\stream.exe"
model_path = r"models\stream"
wav_path = r"speech_lmq.wav"
result = os.popen(" ".join([exe_path, model_path, wav_path]))
while True:
    nowResult = result.buffer.readline().decode("utf8")
    if nowResult == '':
        break
    elif "当前识别结果" in nowResult:
        print('\r', nowResult.replace("\r\n", "").replace("当前识别结果:  ", "").replace('"', "")[:-1], end='', flush=True)
    elif "最终结果" in nowResult:
        print("\n")
        final = nowResult
print("\n", final.replace('最终结果为: "', "")[:-4])