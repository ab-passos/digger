
from datetime import date
import pytest

import querygithub

class TestFileChanges:

    def test_convert_to_str(self):
        today = date.today()
        fileData = querygithub.FileData('commit1', 'author1', today)
        fileChanges = querygithub.FileChanges()
        fileChanges.add_change('file1', fileData)
        assert str(fileChanges) == 'filename is : file1 and file data is: Commit commit1 from user: author1 on date: {}'.format(today)