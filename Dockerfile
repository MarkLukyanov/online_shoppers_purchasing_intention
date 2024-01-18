FROM python:3.10

RUN pip install dill
RUN pip install explainerdashboard

COPY dashboard.py ./
COPY app.py ./

RUN python dashboard.py

EXPOSE 9050
CMD ["python", "./app.py"]