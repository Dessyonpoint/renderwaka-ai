from flask import Flask

app = Flaskapp = FastAPI(
    title="Waka AI App",
    version="1.0.0",
    docs_url="/docs",        # Optional: explicitly enables /docs
    redoc_url="/redoc",      # Optional: enables /redoc
)

@app.route('/')
def home():
    return "✅ Hello, this is my AI app on Hugging Face!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
