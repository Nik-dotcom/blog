from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    '''
    Данные записи
    '''
    title = models.CharField('Заголовок записи', max_length=100)
    img = models.ImageField('Изображение', upload_to='image/%Y', blank=True)
    content = models.TextField('Содержимое записи')
    author =  models.ForeignKey(User, verbose_name='Автор',on_delete=models.CASCADE)
    publicationDate = models.DateTimeField('Дата публикации', default=timezone.now)

    
    def __str__(self) -> str:
        return f'{self.title}, {self.author}'
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь',on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, null=True)
    
    def __str__(self) -> str:
        return f'{self.user}, {self.post}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'