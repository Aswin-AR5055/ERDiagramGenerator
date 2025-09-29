FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000", "erdiagramgenerator.wsgi:application"]