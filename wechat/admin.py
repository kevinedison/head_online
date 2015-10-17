from django.contrib import admin
from wechat.models import UserProfile, AcademyInfo, ClassInfo, SyllabusInfo, TestInfo, GradeInfo, TestAnsInfo,BBS,Category,BBS_user
from django.db import models 
# Register your models here.

class AcademyInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyName', 'academyPre', 'academyIntro', 'slug', 'academyImage')
	prepopulated_fields = {'slug':('academyName',)}
	
class ClassInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyID', 'className', 'classBegDate', 'classCharge')
	prepopulated_fields = {'slug':('className',)}
	
class SyllabusInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyID', 'lessonName', 'lessonContent', 'timeOut')
	
class TestInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'syllaID', 'topic')
	
class TestAnsInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'testInfoId', 'option', 'rightOption')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('nickName', 'id', 'fromUser', 'stuSex', 'stuName', 'inClass', 'tel', 'createTime', 'lastTime')
	
class GradeInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'stuID', 'syllaID', 'grade')
#BBS
class BBS_admin(admin.ModelAdmin):
        list_display=('title','summary','author','signature','view_count','created_at')
        list_filter=('created_at',)
        search_fields=('title','author_user_username')
        def signature(self,obj):
            return obj.author.signature
        signature.short_description='hah'

admin.site.register(AcademyInfo, AcademyInfoAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(SyllabusInfo, SyllabusInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(GradeInfo, GradeInfoAdmin)
admin.site.register(TestAnsInfo, TestAnsInfoAdmin)

admin.site.register(BBS,BBS_admin)
admin.site.register(Category)
admin.site.register(BBS_user)
