BASE_URL = 'https://instagram.com/'
USER_URL = BASE_URL + '{0}'
MEDIA_URL = BASE_URL + '{0}/media'

CHECK_INTERVAL = 10 # in minutes

NOTIFICATION_TITLE = 'Instagram Stalker'
NOTIFICATION_SUCCESS_SOUND_NAME = 'Purr'
NOTIFICATION_FAILURE_SOUND_NAME = 'Basso'

MESSAGE_ACCOUNT_UNAVAILABLE = "{0}: @{1} account doesn't exist or an error occurred while retrivieng it's content. Please verify the given username and internet connection"
MESSAGE_ACCOUNT_PRIVATE = "{0}: @{1} account is still private or doesn't have any public photos"
MESSAGE_ACCOUNT_PUBLIC = "{0}: @{1} made his account public"
