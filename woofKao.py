import random
import pouchy
from home import puzzle

def newbie_task():
    if pouchy.download_Opass():
        return 'pass'

def personal_task():

    if pouchy.visit('Graffiti Wall'):
        message = 'Anything you want to say about PyCon TW.'
        f = open('social_media.txt', 'w')
        f.write(message)
        f.write("@pycon.tw")
        f.close()
        return 'pass'

def team_task(puzzle):
    participants = [("Member1", "PY"), ("Member2", "TH"), ("Member3", "ON")]
    team = [p for p in participants if p[1] in {"PY", "TH", "ON"}]

    team_has_three_members = len(team) == 3

    unique_codes = set(p[1] for p in team)
    codes_are_unique = len(unique_codes) == 3

    if team_has_three_members and codes_are_unique:
        print(f"Team {', '.join(p[0] for p in team)} passed the challenge!")
        print("Team takes a group photo.")
    else:
        print("Not enough participants for a complete team.")

    game_master = "information desk"

    if team_has_three_members and codes_are_unique:
        print(f"Photo taken with: {', '.join(p[0] for p in team)}")
        print(f"Go find the game master {game_master}. Challenge passed!")
    else:
        print("Not enough participants for a complete team.")


def booth_task(unfinished_booths):

    while len(unfinished_booths) > 0:
        booth = random.choice(unfinished_booths)
        if pouchy.visit(booth):
            unfinished_booths.remove(booth)

    if len(unfinished_booths) == 0:
        return 'pass'

def task():

    # 歡迎來到 PyCon TW 2024，這裡是大地遊戲
    # 請閱讀程式碼並依據程式碼內容完成任務
    # 如完成 newbie_task、personal_task 與 team_task，請前往大地遊戲櫃台給工作人員確認並蓋 pass 章
    # 如果是 booth_task，則由各攤位的工作人員替您蓋章

    newbie_task_status   = newbie_task()
    personal_task_status = personal_task()
    team_task_status     = team_task(puzzle)

    sponsor_booths    = ['PSF', 'E.SUN Bank', 'Reuven Lerner']
    community_booths  = ['A', 'B', 'C']
    booth_task_status    = booth_task(sponsor_booths + community_booths)

    if newbie_task_status == personal_task_status == team_task_status == booth_task_status=='pass':
        print('Congratulations on passing all tasks, you are already qualified to draw the final prize.')
    else:
        print('There are still some tasks yet to be completed.')


if __name__ == "__main__":
    task()