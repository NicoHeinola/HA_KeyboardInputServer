# Keyboard Input Server

A FastAPI server for controlling keyboard input remotely.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file:

```
HOST=127.0.0.1
PORT=8000
```

3. Run the server:

```bash
python main.py
```

## API Endpoints

- `POST /press` - Press and release a key
  - Parameters: `key` (string), `duration_seconds` (float, default: 0.1)
- `POST /hold` - Hold down a key
  - Parameters: `key` (string)
- `POST /release` - Release a held key
  - Parameters: `key` (string)
- `GET /` - Health check

## Example Usage

```bash
# Press a key for 0.1 seconds
curl -X POST http://localhost:8000/press -H "Content-Type: application/json" -d '{"key":"a"}'

# Hold a key
curl -X POST http://localhost:8000/hold -H "Content-Type: application/json" -d '{"key":"shift"}'

# Release a key
curl -X POST http://localhost:8000/release -H "Content-Type: application/json" -d '{"key":"shift"}'
```
