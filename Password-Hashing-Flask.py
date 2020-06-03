#! pip install flask-bcrypt

from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
bcrypt.generate_password_hash('p@ssword').decode('utf-8')


bcrypt.check_password_hash(hashed_password, 'p@ssword')