import subprocess
from datetime import datetime
import threading
import time
import sys

def record_hour(filename, ext):
    #ffmpeg -i "https://d2od87akyl46nm.cloudfront.net/live/omroepgelderland/kijkradio/index.m3u8" -c:a copy -filter:v scale=420:-1 -crf 35 -t 00:00:05 file.mp4
    cmd_video = [
        'ffmpeg',
        '-y',
        '-i', 
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8',
        '-c:a',
        'copy',
        '-filter:v',
        'scale=420:-1',
        '-crf',
        '25',
        '-t',
        '00:01:00',
        filename + '.' + ext
    ]

    cmd_audio = [
        'ffmpeg',
        '-y',
        '-i', 
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8',
        '-c:a',
        'copy',
        '-t',
        '00:01:00',
        filename + '.' + ext
    ]

    if ext == 'mp3':
        cmd = cmd_audio
    elif ext == 'mp4':
        cmd = cmd_video
    else:
        print("!!!ERROR!!! UNKNOWN extension!")
        sys.exit(1)

    subprocess.run(cmd)


if __name__ == '__main__':

    while True:
        hourly_dt = datetime.utcnow()
        print(hourly_dt)
        if hourly_dt.strftime("%S") == '00':
            dt_string = hourly_dt.strftime("%Y%m%d%H%M%S")
            print(dt_string)

            try:
                #_thread.start_new_thread(record_hour, 'magic.mp4')
                x = threading.Thread(target=record_hour, args=(dt_string, 'mp4'))
                x.start()
            except:
                print ("Error: unable to start thread")
            
            time.sleep(2)

        time.sleep(0.1)


