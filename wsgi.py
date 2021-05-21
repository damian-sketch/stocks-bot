from app import bot

app = Flask(__name__)

if __name__ == '__main__':
   app.run(threaded=True)