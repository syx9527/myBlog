from .models import *

# Create your tests here.

user = UserInfo.objects.filter(username='syx').first()
if user:

    print(user.blog.site_name)
else:
    print(2)
