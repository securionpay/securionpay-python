from pathlib import Path

from .testcase import TestCase


def create_test_file(tmpdir):
    file = tmpdir.join("test_file.pdf")
    file.write_text("Any text", "UTF-8")
    return file


class TestCredits(TestCase):
    def test_upload_by_filename(self, tmpdir, api):
        # given
        file = create_test_file(tmpdir)
        file_name = Path(file).resolve().__str__()
        # when / then
        api.file_uploads.upload(file_name, {"purpose": "dispute_evidence"})

    def test_upload_by_opened_file(self, tmpdir, api):
        # given
        file = create_test_file(tmpdir)
        # when / then
        api.file_uploads.upload(open(file, "rb"), {"purpose": "dispute_evidence"})

    def test_get(self, tmpdir, api):
        # given
        file = create_test_file(tmpdir)
        uploaded = api.file_uploads.upload(
            open(file, "rb"), {"purpose": "dispute_evidence"}
        )
        # when
        response = api.file_uploads.get(uploaded["id"])
        #
        assert uploaded["id"] == response["id"]

    def test_list(self, tmpdir, api):
        # given
        file = create_test_file(tmpdir)
        uploaded = api.file_uploads.upload(
            open(file, "rb"), {"purpose": "dispute_evidence"}
        )
        # when
        response = api.file_uploads.list({"limit": 100})
        #
        self.assertListResponseContainsInAnyOrderById(response, [uploaded])
