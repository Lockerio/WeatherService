from datetime import datetime, timedelta, timezone

from icecream import ic


class TimeHelper:
    @staticmethod
    def get_local_time(offset_seconds: int) -> str:
        gmt_time = datetime.now(timezone.utc)
        offset = timedelta(seconds=offset_seconds)
        local_time = gmt_time + offset
        rounded_local_time = local_time.replace(minute=0, second=0, microsecond=0)
        formatted_time = rounded_local_time.strftime('%Y-%m-%dT%H:%M')
        return formatted_time
