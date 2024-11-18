# comando para refazer a senha (troca o admin pelo nome colocado):
# python manage.py changepassword admin

# comando para iniciar o projeto :
# python manage.py runserver

# comando para criar um usuario admin:
# python manage.py createsuperuser 
# ex: lorddoug - projetodoug

# comando para criar um usuario comum:
# python manage.py createsuperuser --username=nome --email=email --password=senha

# comando para criar um app :
# python manage.py startapp nome_do_app

# comando  para criar um o caminho do meus models:
# python manage.py makemigrations

#  comando para criar o banco de dados:
# python manage.py migrate
# sempre usar para atualizar os models no banco de dados





# criando a pasta mde midia 
# em settings.py adicionar o caminho da pasta midia
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# adicionar o caminho da pasta midia nas urls.py de todos os apps que precise
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


