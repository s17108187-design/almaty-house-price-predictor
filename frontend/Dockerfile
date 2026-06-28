FROM python:3.14-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit","run","frontend/frontend.py","--host","0.0.0.0","8501"]