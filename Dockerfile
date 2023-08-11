# 
FROM python:3.9

# 
WORKDIR /ModelApp

# 
COPY ./requirements.txt /ModelApp/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /ModelApp/requirements.txt

# 
COPY ./app /ModelApp/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]