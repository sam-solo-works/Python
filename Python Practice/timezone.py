from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
utc.zone

eastern = pytz.timezone('US/Eastern')
eastern.zone

amsterdam = pytz.timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
print(loc_dt.strftime(fmt))

# Claytontz = -14400
# Clayton = pytz.timezone(datetime.datetime.now())
# print(datetime.timedelta(0, Claytontz))

#datetime.datetime.now(pytz.timezone('Asia/Jerusalem')).strftime('%z')
