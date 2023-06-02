from django.contrib.auth.decorators import user_passes_test
from accounts.models import User

def is_admin(User):
    return User.is_authenticated and User.tipo_de_usuario == User.ADMIN
    
def is_worker(User):
    return User.is_authenticated and User.tipo_de_usuario == User.TRABAJADOR
    
def is_client(User):
    return User.is_authenticated and User.tipo_de_usuario == User.CLIENTE

admin_required = user_passes_test(lambda u: is_admin(u), login_url='login')
worker_required = user_passes_test(lambda u: is_worker(u), login_url='login')
client_required = user_passes_test(lambda u: is_client(u), login_url='login')
