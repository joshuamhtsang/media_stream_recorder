import subprocess
from datetime import datetime


if __name__ == '__main__':
    hourly_dt = datetime.utcnow()
    print(hourly_dt.strftime("%Y%m%d%H%M%S"))

    cmd = [
        'ffmpeg',
        '-y',
        '-i', 
        'https://d2od87akyl46nm.cloudfront.net/live/omroepgelderland/kijkradio/index.m3u8',
        '-c:a',
        'copy',
        '-filter:v',
        'scale=420:-1',
        '-crf',
        '25',
        '-t',
        '00:00:10',
        'file.mp4'
    ]
    subprocess.run(cmd)
    #ffmpeg -i "https://d2od87akyl46nm.cloudfront.net/live/omroepgelderland/kijkradio/index.m3u8" -c:a copy -filter:v scale=420:-1 -crf 35 -t 00:00:05 file.mp4






