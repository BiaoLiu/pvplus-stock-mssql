from django.db import models

# Create your models here.

response_retcode = {'success': 10000, 'error': '10001'}

response_message = {'recode': response_retcode['success'], 'errmsg': '', 'data': ''}
