from django.db import models

class Profession(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    def __repr__(self):
        return f"{self.title} - {self.price:.0f}"
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
