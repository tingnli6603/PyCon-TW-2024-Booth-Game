import os
import random
import pouchy
from home import your_puzzle

def newbie_task():
    if pouchy.download_Opass():
        return 'pass'
    else:
        return 'fail'

def graffiti_task():

    with open('graffiti_wall.txt', 'w') as f:
        message = 'Anything you want to say about PyCon TW.'
        f.write(message)

    with open('graffiti_wall.txt', 'r') as f:
        photo = f.read()

    with open('social_media.txt', 'w') as f:
        f.write(photo)
        f.write("@pycon.tw")

    if os.path.isfile('social_media.txt'):
        return 'pass'
    else:
        return 'fail'

def team_task(your_puzzle):
    members = ['PY', 'TH', 'ON']
    your_teammates = [m for m in members if m != your_puzzle]
    photo_content = {}
    if len([your_puzzle] + your_teammates) == 3:
        photo_content['puzzle_image'] = ''.join(members)
        photo_content['people']       = len(members)
        photo_content['background']   = 'graffiti_wall'

    for key, value in photo_content.items():
        if value is None:
            return 'fail'

    return 'pass'

def booth_task():
    sponsor_booths    = ['PSF', 'E.SUN Bank', 'Reuven Lerner']
    community_booths  = ['D', 'E', 'F']
    unfinished_booths = sponsor_booths + community_booths

    while len(unfinished_booths) > 0:
        booth = random.choice(unfinished_booths)
        if pouchy.visit(booth):
            unfinished_booths.remove(booth)

    if len(unfinished_booths) == 0:
        return 'pass'
    else:
        return 'fail'

def task():
    newbie_task_status   = newbie_task()
    graffiti_task_status = graffiti_task()
    team_task_status     = team_task(your_puzzle)
    booth_task_status    = booth_task()


if __name__ == "_main_":
    task()