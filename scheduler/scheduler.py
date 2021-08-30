from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

try:
    from server import app
except:
    from .server import app


executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


sched = BackgroundScheduler()
sched.configure(executors=executors, job_defaults=job_defaults, timezone=utc)

@sched.scheduled_job('cron', id='sample_id', day='*', hour=0, minute=15, second=0) ## run at 12.15am
def sample_cron_schedule():
    with app.app_context():
        print('running cron job')
