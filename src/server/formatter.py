from humanize import naturaltime


class Formatter:
    @staticmethod
    def created(data):
        created = data.get('created')
        if not created:
            return "<unknown>"

        # dateformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        # created_date = datetime.strptime(created, dateformat)
        # return naturaltime(datetime.now() - created_date)
        return created.strftime("%x %X")

    @staticmethod
    def elapsed(data):
        elapsed = data.get('elapsed')
        if not elapsed:
            return "AberMUD has yet to ever start!!!"
        return "Game time elapsed: {}".format(
            humanize.naturaltime(elapsed)
        )
