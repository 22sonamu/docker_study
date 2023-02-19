FROM python:3.11.2

# ADD 는 COPY 보다 강한 명령어이다.
# 압축 파일이나 네트워크 상의 파일을 사용하는게 아니라면 COPY
COPY backend.py backend.py
COPY requirements.txt requirements.txt

#FLASK 설치 위함
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "backend.py"]