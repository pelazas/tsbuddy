FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

COPY . .

EXPOSE 5000

CMD [ "python", "main.py" ]