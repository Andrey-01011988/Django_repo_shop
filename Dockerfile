FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip "poetry==2.1.3" 
RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY mysite .

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
