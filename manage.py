import os
import logging

from flask_script import Manager, Server, prompt_bool, Shell
from flask_migrate import MigrateCommand
from logging.handlers import RotatingFileHandler
from sqlalchemy.exc import SQLAlchemyError

try:
    from server import create_flask_app
    from data_processing import file_summary
except ImportError:
    from .server import create_flask_app
    from .data_processing import file_summary

environment = os.getenv("FLASK_CONFIG")
app = create_flask_app(environment)

app.secret_key = os.getenv("APP_SECRET")

port = int(os.environ.get('PORT', 5000))
server = Server(host="0.0.0.0", port=port)


# initialize flask script
manager = Manager(app)

# enable migration commands
manager.add_command("runserver", server)


@manager.command
def script_cleanup_data(prompt=True):
    """Script to summarizes Customerio event data file
    """
    if environment == "production":
        print("\n\n\tNot happening! Aborting...\n\n Aborted\n\n")
        return

    if environment in ["testing", "development"]:
        try:
            file_summary('data/messages.1.data') # summarize the data/messages.1.data file
            message = "\n\n\tSuccess in cleanup\n\n\n"
        except SQLAlchemyError as error:
            message = "\n\n\tThe error below occured when trying to summarize data file\n\n\n" + str(error) + "\n\n"

        print(message)
    else:
        print("\n\n\tAborting... Invalid environment '{}'.\n\n"
              .format(environment))


# initialize the log handler
handler = RotatingFileHandler('errors.log', maxBytes=10000000, backupCount=5)
formatter = logging.Formatter("%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
# set the log handler level
handler.setLevel(logging.INFO)
# set the app logger level
app.logger.setLevel(logging.INFO)
werkzeug_handler = logging.getLogger('werkzeug')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.addHandler(werkzeug_handler)

manager.run()
