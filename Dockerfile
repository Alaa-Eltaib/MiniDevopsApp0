FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r req.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]