FROM python:3.7
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY record_stream.py /app
CMD python3 record_stream.py --mode minutely