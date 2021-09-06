import argparse

ARGUMENT_INPUT = 'input'
ARGUMENT_TOKEN = 'token'
ARGUMENT_PARENT = 'parent'


def get_arguments():
    parser = argparse.ArgumentParser(description='Sends file to Google Drive')
    parser.add_argument('-i', f'--{ARGUMENT_INPUT}', required=True, help='A file')
    parser.add_argument('-t', f'--{ARGUMENT_TOKEN}', required=True, help='Auth token')
    parser.add_argument('-p', f'--{ARGUMENT_PARENT}', required=True, help='Folder ID')
    return parser.parse_args()


def get_input(args):
    return getattr(args, ARGUMENT_INPUT)


def get_auth_token(args):
    return getattr(args, ARGUMENT_TOKEN)


def get_folder_id(args):
    return getattr(args, ARGUMENT_PARENT)
