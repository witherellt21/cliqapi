from time import strftime
import concurrent_log_handler


class DatetimeNamedConcurrentRotatingFileHandler(
    concurrent_log_handler.ConcurrentRotatingFileHandler
):
    def namer(self, default_name):
        try:
            head, tail = self.baseFilename.split(".")
        except:
            head, tail = (self.baseFilename, "")
        return f"{head}_{strftime('%m-%d-%Y_%H-%M-%S')}.{tail}"
