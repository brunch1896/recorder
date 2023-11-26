import pyaudio
import wave
import keyboard
import requests


# print(pyaudio)
# exit()
# 设置参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "output.wav"

# 打开音频设备
audio = pyaudio.PyAudio()

# 打开流
stream = audio.open(format=FORMAT, channels=CHANNELS,
             rate=RATE, input=True,
             frames_per_buffer=CHUNK)

print("wwwwwww")

frames = []
recording = False
pause = False


# if keyboard.is_pressed('s'):
#       print("又开始了")

# 开始录制
while True:
 if keyboard.is_pressed('s'):
   if not recording:
     print("开始录制，按 'q' 键停止，按 'p' 键暂停")
     recording = True
#    break
 if recording:
   print("22222")
   data = stream.read(CHUNK)
   frames.append(data)
 if keyboard.is_pressed('q'):
   print("33333")
   break
 if keyboard.is_pressed('p'):
   pause = not pause
   if pause:
       print("暂停录制，按 'p' 键继续")
   else:
       print("恢复录制，按 'p' 键暂停")

# 停止录制
stream.stop_stream()
audio.terminate()

# 保存音频文件
with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(audio.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))

print(f"已录制并保存为 {WAVE_OUTPUT_FILENAME}")


API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("output.wav")
print(output)