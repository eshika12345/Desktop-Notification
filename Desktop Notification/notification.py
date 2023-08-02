from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is vital for mental health",
            app_icon="C:/Users/ESHIKA/Downloads/pointer_pin_dropbox_logo_icon_255279.ico",
            timeout=5)
        time.sleep(10)