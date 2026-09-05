import os
import webview


class FileApi:
    def saveContent(self, content):
        # 1. Capture the tuple returned by the dialog box
        filename_tuple = webview.windows[0].create_file_dialog(
            webview.SAVE_DIALOG, save_filename=".txt"
        )

        # 2. Check if the user cancelled the dialog (returns None)
        if not filename_tuple:
            return

        # 3. Extract the first string element out of the tuple
        actual_filename = filename_tuple[0]

        # 4. Save your content using the clean string path
        with open(actual_filename, "w") as f:
            f.write(content)

    def ls(self):
        return os.listdir(".")
