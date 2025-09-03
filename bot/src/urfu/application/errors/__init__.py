class AppError(Exception):
    message: str = "Internal Server Error"
    status_code: int = 500

    def __init__(
        self,
        message: str | None = None,
        status_code: int | None = None,
        *args: object,
    ) -> None:
        self.message = message or self.message
        self.status_code = status_code or self.status_code
        super().__init__(self.message, *args)
