# YOLOv8 Deployment with FastAPI

This repo contains a simple FastAPI service for image inference using YOLOv8.

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoint

- `POST /predict/` with form-data: `file=<image>`
