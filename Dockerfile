FROM python:3.9.21-bullseye

WORKDIR /app

RUN pip install elasticsearch openai fastapi uvicorn requests google-genai

COPY ./src /app

EXPOSE 8000

# Set the default command to run the FastAPI app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]