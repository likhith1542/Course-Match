from django.contrib import admin
from .models import Poll
# Register your models here.

class accounts(admin.ModelAdmin):
    list_display=(
        'question',
        'option_one',
        'option_two',
        'option_three',
        'option_four',
        'option_five',
        'option_six',
        'option_seven',
        'option_eight',
        'option_nine',
        'option_ten'
    )

admin.site.register(Poll,accounts)
