from subprocess import Popen, PIPE, STDOUT


# ffprobe -i northernlights.mp4 -show_entries format=duration -v quiet
def get_duration(input_file):
    cmd2 = ['ffprobe', '-i', input_file, '-show_entries', 'format=duration', '-v', 'quiet']
    p = Popen(cmd2, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)

    duration = stdout.decode('ascii').split('\n')[1].split('=')[1]
    print(duration)


if __name__ == '__main__':
    get_duration('northernlights.mp4')
