import argparse
import subprocess
from datetime import datetime, timedelta
import threading
import time
import sys

def record_hour(filename, ext, stream_url, record_duration):
    # Example:
    # $ ffmpeg -i "https://d2od87akyl46nm.cloudfront.net/live/omroepgelderland/kijkradio/index.m3u8" -c:a copy -filter:v scale=420:-1 -crf 35 -t 00:00:05 file.mp4
    cmd_video = [
        'ffmpeg',
        '-y',
        '-i', 
        stream_url,
        '-c:a',
        'copy',
        '-filter:v',
        'scale=420:-1',
        '-crf',
        '25',
        '-t',
        record_duration,
        filename + '.' + ext
    ]

    cmd_audio = [
        'ffmpeg',
        '-y',
        '-i', 
        stream_url,
        '-c:a',
        'copy',
        '-t',
        record_duration,
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", choices=['minutely', 'hourly'], required=True)
    args = parser.parse_args()

    stream_url = 'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8'

    while True:
        current_dt = datetime.utcnow()
        print(current_dt)

        if args.mode == 'minutely':
            checker = "%S"
            wait_time = 2
            period = timedelta(minutes=1)
            record_duration = '00:01:00'

            dt_start_string = current_dt.strftime("%Y%m%d%H%M00")
            dt_next = current_dt + period
            dt_next_string = dt_next.strftime("%Y%m%d%H%M00")
        elif args.mode == 'hourly':
            checker = "%M"
            wait_time = 120
            period = timedelta(hours=1)
            record_duration = '01:00:00'

            dt_start_string = current_dt.strftime("%Y%m%d%H0000")
            dt_next = current_dt + period
            dt_next_string = dt_next.strftime("%Y%m%d%H0000")
        else:
            print("Invalid mode chosen.")
            sys.exit(1)

        if current_dt.strftime(checker) == '00':
            
            filename = 'DET024SkySportNews_gcp_la4_' + dt_start_string + '_' + dt_next_string

            try:
                x = threading.Thread(target=record_hour, args=(filename, 'mp4', stream_url, record_duration))
                x.start()
            except Exception as e:
                print(e)
                print("!!!Error!!! Unable to start thread.")
            
            print("Recording : ", filename)
            time.sleep(wait_time)

        time.sleep(0.1)


