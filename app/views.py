from app import app

@app.route('/')
@app.route('/index')
def index():
    return "What are you doing here?"
