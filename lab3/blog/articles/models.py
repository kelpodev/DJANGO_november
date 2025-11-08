from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Одна статья в блоге.
    Django сам создаст из этого таблицу articles_article
    """

    # Заголовок — строка до 200 символов
    title = models.CharField(max_length=200)

    # Автор — ссылка на пользователя.
    # CASCADE = если удалить юзера → удалятся его статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Полный текст статьи (без ограничения длины)
    text = models.TextField()

    # Дата создания — ставится автоматически при первом сохранении
    created_date = models.DateField(auto_now_add=True)

    # Как статья будет выглядеть в админке и в print()
    # В Python 3 используем __str__, а не старый __unicode__
    def __str__(self):
        return f"{self.author.username}: {self.title}"

    # Краткий отрывок для списка статей
    def get_excerpt(self):
        if len(self.text) > 140:
            return self.text[:140] + "..."   # обрезаем + троеточие
        return self.text                     # короткий текст — как есть
