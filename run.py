import datetime
from application import app

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = '53a7f856-9cf0-41d0-9b7b-b10891d36b4f'
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=5)

    app.run(debug=True)