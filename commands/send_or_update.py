from core.actions import get_arguments, get_input, get_auth_token
from core.drive_bot import DriveBot
from core.validators import does_file_exist


def send_or_update():
    args = get_arguments()
    file_path = get_input(args)
    does_file_exist(file_path)
    drive_bot = DriveBot(auth_token=get_auth_token(args))
    return drive_bot.send_or_update(file_path)


if __name__ == '__main__':
    send_or_update()
