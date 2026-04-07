# SmokeWatch AI

This repository contains the source code for **SmokeWatch AI**, a proof‑of‑concept system for detecting smoking in videos using a pretrained YOLOv8 model.

## Backend

The `backend` directory hosts a FastAPI application that accepts video uploads, runs YOLOv8 object detection, and returns processed videos. To run the backend locally:

```bash
cd backend
bash start.sh
```

## Frontend

The `frontend` directory contains a simple HTML page that lets you upload a video to the backend and view the response.

## Deployment

A `render.yaml` file defines the configuration for deploying the backend to Render. The frontend can be deployed to Netlify or any static hosting service.

Feel free to customize the model, add features like timeline markers and bounding boxes, or replace the pretrained YOLO model with your own `smoking.pt` to improve detection accuracy.
