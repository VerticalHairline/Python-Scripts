import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from letterGenerator import api_message as api_message

CLIENT_FILE = 'GradAccount.json'
SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/drive']
creds = None

def token():


    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('GradAccount.json', SCOPES)
            creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

token()

def doc_id(title):

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    drive_service = build('drive', 'v3', credentials=creds)

    folder_id = '170pwBc9Ogflpf-4b5lRox8Qj37RgheEa'

    doc_title = title

    doc_metadata = {
        'name': doc_title,
        'parents': [folder_id],
        'mimeType': 'application/vnd.google-apps.document'
    }
    drive_service = build('drive', 'v3', credentials=creds)
    doc = drive_service.files().create(body = doc_metadata).execute()

    id = doc['id']

    return id

id = doc_id('thank you')

def doc_content(message, id, pageBreak = False):
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    docs_service = build('docs', 'v1', credentials=creds)

    requests = [
    {
        'insertText': {
            'location': {
                'index': 1
            },
            'text': f"{message}"
        },
    }
    ]

    result = docs_service.documents().batchUpdate(documentId = id, body={'requests': requests}).execute()

def doc_pagebreak(id):
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    docs_service = build('docs', 'v1', credentials=creds)

    requests = [
    {
        'insertPageBreak':{
            'location':{
                'index': 1,
                'segmentId': ''
            }
        }
    }
    ]

    result = docs_service.documents().batchUpdate(documentId = id, body={'requests': requests}).execute()

increment = 0
for message in api_message:
    increment += 1
    doc_content(message, id)
    if increment > 3:
        increment = 0
        doc_pagebreak(id)