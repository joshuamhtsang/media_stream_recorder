FROM python:3.7
RUN apt update
RUN apt install -y ffmpeg
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY record_stream.py /app
CMD python3 -u record_stream.py --mode minutely