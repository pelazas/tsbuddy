FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

COPY . .

EXPOSE 8001

CMD [ "python", "main.py" ]