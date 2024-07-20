from datetime import datetime, timedelta, timezone


class TimeHelper:
    @staticmethod
    def get_local_time(offset_str: str):
        gmt_time = datetime.now(timezone.utc)
        offset_hours = int(offset_str)
        offset = timedelta(hours=offset_hours)

        local_time = gmt_time + offset
        formatted_time = local_time.strftime('%Y-%m-%dT%H:%M')
        return formatted_time
