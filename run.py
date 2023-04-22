import uvicorn


def start():
    uvicorn.run("app.main.config.server:app", host="0.0.0.0", port=9000, reload=True)


if __name__ == "__main__":
    start()
