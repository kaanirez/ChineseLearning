DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kagan12LINA@localhost:5432/app'
SQLALCHEMY_DATABASE_URI = 'postgres://sspmowzdlxwkpd:eff1274bb20690017128b28f15d89c693efc85e89e22586a2eb5dc892c45055f@ec2-54-158-26-89.compute-1.amazonaws.com:5432/dd3nloo7u99q67'


SQLALCHEMY_TRACK_MODIFICATIONS= False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"