from fastapi import FastAPI
from threading import Thread
import mqqt

app = FastAPI()

def mqtt_thread():
    mqqt.start_listening()

@app.on_event("startup")
def startup_event():
    thread = Thread(target=mqtt_thread)
    thread.daemon = True
    thread.start()

@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI y MQTT en ejecución"}
