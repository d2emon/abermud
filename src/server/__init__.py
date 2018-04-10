from user.models import User


def check_host(host):
    '''
    Check we are running on the correct host
    see the notes about the use of flock();
    and the affects of lockf();
    '''
    assert User.host() == host, "AberMUD is only available on {}, not on {}".format(host, User.host())
