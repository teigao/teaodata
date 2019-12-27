import os
import webbrowser


_current_path = os.path.dirname(__file__)
_project_root_folder = _current_path+"/_config/"


html_path = _project_root_folder + 'sample.html'

webbrowser.open_new_tab(html_path)
