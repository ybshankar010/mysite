from django.contrib.auth.models import User


def project_context(context):

    context = {"me": User.objects.first()}

    return context
