#! pip install win10toast pypiwin32 setuptools

from win10toast import ToastNotifier

toaster = ToastNotifier()


def notification(title, message, duration=5, icon=None):
    if icon:
        toaster.show_toast(
            title, message, duration=duration, threaded=True, icon_path=icon
        )
    else:
        toaster.show_toast(title, message, duration=duration, threaded=True)


notification("Hey", "Model Trained")
