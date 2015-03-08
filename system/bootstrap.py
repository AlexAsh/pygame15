"""Bootstrap application"""
import os
import shutil


def bootstrap():
    """Bootstrap application"""
    settings = "system/settings.py"
    sample = "system/settings_sample.py"

    if not os.path.exists(settings):
        if os.path.exists(sample):
            shutil.copy(sample, settings)
        else:
            return False

    from system.settings import settings
    return settings
