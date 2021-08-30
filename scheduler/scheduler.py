from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

try:
    from server import app
    from data_processing import file_summary
except:
    from .server import app
    from .data_processing import file_summary


executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}


sched = BackgroundScheduler()
sched.configure(executors=executors, job_defaults=job_defaults, timezone=utc)

@sched.scheduled_job('cron', id='process_data_summary')
def process_data_summary_schedule():
    """ Job to summarize data """
    with app.app_context():
        print('\n\nrunning cron job')
        file_summary('data/messages.1.data')
        print('finished cron job\n\n')

    sched.shutdown(wait=False)
