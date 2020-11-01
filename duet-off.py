import requests

TASMOTA_OFF = 'cm?cmnd=Power%20off'
DUET_STATUS = 'rr_status'
TEMPERATURE_OFF = 45

# list of tuples, address of duet, addres of switch (tasmota)
CONFIG = [
    ('http://genius.local', 'http://genius-sw.local'),
]


def switch_off(switch_url):
    if switch_url.endswith('/'):
        switch_url = switch_url[0:-1]

    url = '{}/{}'.format(switch_url, TASMOTA_OFF)

    requests.get(url)


def can_be_off(duet_url):
    if duet_url.endswith('/'):
        duet_url = duet_url[0:-1]

    url = '{}/{}'.format(duet_url, DUET_STATUS)

    r = requests.get(url)
    data = r.json()

    if data['status'] != 'I':
        return False

    active = data['active']
    heaters = data['heaters']

    if not -1 in active:
        return False

    for a, h in zip(active, heaters):
        if a == -1 and h > TEMPERATURE_OFF:
            return False

    return True


def process(duet_url, switch_url):
    if can_be_off(duet_url):
        switch_off(switch_url)

def process_all():
    for duet, switch in CONFIG:
        try:
            process(duet, switch)
        except Exception as e:
            pass


if __name__ == "__main__":
    process_all()