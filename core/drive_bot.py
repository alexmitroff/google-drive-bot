from mimetypes import MimeTypes

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


class DriveBot:
    def __init__(self, auth_token):
        credentials = Credentials(token=auth_token)
        self.service = build('drive', 'v3', credentials=credentials)

    @staticmethod
    def get_filename(filepath):
        return filepath.split('/')[-1]

    @staticmethod
    def get_basic_metadata(filename):
        return {'name': filename}

    def get_files_list(self, q=None, page_token=None):
        list_params = {
            'spaces': 'drive',
            'fields': 'nextPageToken, files(id, name)',
            'pageToken': page_token,
        }
        if q is not None:
            list_params['q'] = q
        response = self.service.files().list(**list_params).execute()
        return response.get('files', [])

    def get_existing_file_id(self, filepath):
        filename = self.get_filename(filepath)
        files = self.get_files_list(q=filename)
        for file in files:
            if filename == file['name']:
                return file['id']

    @staticmethod
    def get_mime(filepath):
        mime = MimeTypes()
        return mime.guess_type(filepath)

    def get_media_body(self, filepath):
        return MediaFileUpload(filepath, mimetype=self.get_mime(filepath))

    def send(self, filepath, folder_id=None):
        filename = self.get_filename(filepath)
        file_metadata = self.get_basic_metadata(filename)
        if folder_id is not None or folder_id != "":
            file_metadata['parents'] = [{'id': folder_id}]

        create_params = {
            'body': file_metadata,
            'media_body': self.get_media_body(filepath),
            'fields': 'id',
        }

        response = self.service.files().create(**create_params).execute()
        print('File ID: %s' % response.get('id'))

    def update(self, filepath, file_id):
        media_body = self.get_media_body(filepath)

        update_params = {
            'fileId': file_id,
            'media_body': media_body,
        }

        response = self.service.files().update(**update_params).execute()
        print('Updated file: %s' % response.get('id'))

    def send_or_update(self, filepath, folder_id=None):
        file_id = self.get_existing_file_id(filepath)
        if file_id is None:
            self.send(filepath, folder_id)
        else:
            self.update(filepath, file_id)
