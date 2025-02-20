FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install pytest flake8 mypy pytest-cov
CMD ["python", "prime.py"]
