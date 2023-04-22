class HttpErrors:
    @staticmethod
    def error_400(message="Bad Request"):
        return {"status_code": 400, "body": {"error": message}}

    @staticmethod
    def error_401(message="Unauthorized"):
        return {"status_code": 401, "body": {"error": message}}

    @staticmethod
    def error_403(message="Forbidden"):
        return {"status_code": 403, "body": {"error": message}}

    @staticmethod
    def error_404(message="Not Found"):
        return {"status_code": 404, "body": {"error": message}}

    @staticmethod
    def error_409(message="Conflict"):
        return {"status_code": 409, "body": {"error": message}}

    @staticmethod
    def error_500(message="Internal Server Error"):
        return {"status_code": 500, "body": {"error": message}}
