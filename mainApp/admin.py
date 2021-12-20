from django.contrib import admin
from . import models
admin.site.site_header ="Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Your Admin Dashboard"





class SolutionDetailParagraphConten(admin.TabularInline):
    model = models.SolutionDetailParagraph
    extra=1

class SolutionDetailAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading',"intro_content",'hover_icon','main_icon',"number"]})]
    inlines=[SolutionDetailParagraphConten]





admin.site.register(models.SolutionDetail,SolutionDetailAdmin)
admin.site.register(models.Contact)
admin.site.register(models.ParthershipNetwork)
admin.site.register(models.WorkWithus)

admin.site.register(models.countryAddress)
admin.site.register(models.CountryLocation)

admin.site.register(models.ContinentLocation)