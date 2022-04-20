import securionpay as api
from securionpay.resource import Resource


class FileUploads(Resource):
    def upload(self, file, params):
        if isinstance(file, str):
            opened = open(file, "rb")
            file_tuple = (opened.name, opened, "application/octet-stream")
        else:
            file_tuple = file

        return self._multipart(
            "/files",
            params=params,
            files={"file": file_tuple},
            url=api.uploads_url.rstrip("/"),
        )

    def get(self, file_upload_id):
        return self._get("/files/%s" % file_upload_id, url=api.uploads_url.rstrip("/"))

    def list(self, params):
        return self._get("/files", params, url=api.uploads_url.rstrip("/"))
