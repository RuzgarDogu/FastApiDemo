class Docsettings(object):
    title="FastAPI Test Project"
    description="This is a very simple FastAPI project, with auto docs for the API and everything. This Api is created for testing purposes only. Feel free to use. DISCLAIMER -- I do not take responsibility for any kind of misuse. This is not tested thoroughly and must be used with caution."
    version="0.2.0"
    openapi_tags = [
        {
            "name": "Users",
            "description": "Operations with users. The **login** logic is also here.",
        },
        {
            "name": "Blogs",
            "description": "Create, Delete, Update and Read Blogs.",
            "externalDocs": {
                "description": "Powered by FastAPI. For more info > ",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ]
    # docs_url="/tryout"
    # redoc_url="/documentation"
    docs_url="/docs"
    redoc_url="/redoc"

docsettings = Docsettings()
