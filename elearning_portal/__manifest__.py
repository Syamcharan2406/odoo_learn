{
    "name": "My eLearning Portal Component",
    "author": "OdooErpCloud",
    "website": "https://campuscleverit.es",
    "version": "19.0.0.1.0",
    "summary": "Shows subscribed eLearning courses in the portal using OWL",
    "category": "Syam",
    "depends": [
        "portal",
        "website_slides",  # Dependencia clave para elearning app
        "web",
    ],
    "data": [
        "views/portal_template.xml",  # El XML que hereda del portal
    ],
    "assets": {
        "web.assets_frontend": [
            "elearning_portal/static/src/components/*.js",
            "elearning_portal/static/src/components/*.xml",
        ],
        # "web.assets_backend": [
        #     "elearning_portal/static/src/components/*.js",
        #     "elearning_portal/static/src/components/*.xml",
        # ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}