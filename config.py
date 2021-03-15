class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres://nkwbokdiefieok' \
                              ':93621b7d45dd634f364cb886b5a29e07a63ab845f5da574371847359b854629f@ec2-54-216-185-51.eu' \
                              '-west-1.compute.amazonaws.com:5432/d606d18vn5g2dq'
    SECRET_KEY = 'secret_key'
    SECURITY_PASSWORD_SALT = 'SALT'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
