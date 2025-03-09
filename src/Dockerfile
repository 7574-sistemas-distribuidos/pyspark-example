FROM eclipse-temurin:21.0.6_7-jre
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install -yq python3.12-full
RUN apt install -yq python3-pip

WORKDIR /src
COPY requirements.txt /src
RUN pip install --break-system-packages -r requirements.txt
COPY main.py /src
CMD ["python3", "main.py"]
