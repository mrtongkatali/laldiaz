from django.shortcuts import render

def index(request):
    urls = {
        "cv": "https://s3-ap-southeast-1.amazonaws.com/laldiaz.me/LeoDiaz-Resume-2021-v1.pdf",
        "gitlab": "https://gitlab.com/mrtongkatali",
        "linkedin": "https://www.linkedin.com/in/mrtongkatali/",
        "github": "https://github.com/mrtongkatali",
        "email": "leo@crazyapp.cloud",
        "mailto_href": "mailto:leo@crazyapp.cloud",
        "cookery_api": "http://api-dev-cookery.crazyapp.cloud/api/swagger",
        "mcl": "https://mcl.edu.ph/"

    }

    return render(request, 'landing_v1/index.html', urls)
