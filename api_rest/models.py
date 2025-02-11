from django.db import models

# define classe e modelo será mapeado para uma tabela no banco de dados
class User(models.Model):
	# define os campos do banco de dados (tipo, maximo tamanho, default e primary key)
	user_nickname = models.CharField(primary_key=True, max_length=100, default='')
	user_name = models.CharField(max_length=150, default='')
	user_email = models.EmailField(default='')
	user_age = models.IntegerField(default=0)

	# define como o objeto será exibido quando convertido em texto
	def __str__(self):
			return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'

class UserTasks (models.Model):
  user_nickname= models.CharField(max_length=100, default="")
  user_task= models.CharField(max_length=255, default="")