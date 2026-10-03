from datetime import datetime
from zoneinfo import ZoneInfo

# list zone info
"""
import zoneinfo
zone = zoneinfo.available_timezones()
for i in zone: print(i) # ex: "Asia/Jakarta"
"""


def f(zone_info: str = "Asia/Jakarta", default: bool = False) -> datetime:
    tz_server = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tz_info = datetime.now(ZoneInfo(zone_info)).strftime("%Y-%m-%d %H:%M:%S")
    # print(f"tz_server: {tz_server} || tz_info: {tz_info}")
    if tz_server == tz_info:
        # print("masuk if")
        return datetime.now()
    if default:
        return datetime.now()
    # print("tidak masuk if")
    # print(f">>> {datetime.now(ZoneInfo(zone_info)).replace(tzinfo=None)}")
    return datetime.now(ZoneInfo(zone_info)).replace(tzinfo=None)
