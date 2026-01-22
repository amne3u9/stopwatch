from datetime import date


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def add_session(self, duration):
        today = date.today().strftime('%Y-%m-%d')
        if today in self.sessions:
            self.sessions[today].append(duration)
        else:
            duration_data = [duration]
            self.sessions[today] = duration_data

    def get_sessions_by_date(self, date_) -> list:
        return self.sessions[date_]

    def get_total_by_date(self, date_) -> float:
        return sum(self.get_sessions_by_date(date_))
