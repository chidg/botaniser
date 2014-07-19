import os

def get_settings_module():
    if os.environ['USER'] == 'ubuntu':
        import botaniser.settings.prod as settings
        return settings
    else:
        import botaniser.settings.dev as settings
        return settings
