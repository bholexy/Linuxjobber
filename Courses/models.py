import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/uploads')

LAB_SUBMISSION= (
        (1, 'submit by uploading document'),
        (2, 'submit by machine ID'),
        (3, 'submit from repo')
    )

class Course(models.Model):
    course_title = models.CharField(max_length = 200)
    lab_submission_type = models.IntegerField(default=1, choices=LAB_SUBMISSION)
    
    class Meta:
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return self.course_title


class CourseTopic(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='topics',related_query_name='topic')
    topic_number = models.IntegerField(default=0)
    topic =  models.CharField(max_length = 200)
    lab_name = models.CharField(max_length = 50)
    video = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Course Topics'
    
    def __str__(self):
        return self.topic
#         return self.lab_name+" - "+self.topic


class LabTask(models.Model):
    lab = models.ForeignKey(CourseTopic, on_delete = models.CASCADE, related_name='tasks',related_query_name='task')
    task_number = models.IntegerField()
    comment = models.TextField()
    note = models.TextField(null = True, blank = True)
    task = models.TextField()
    xpected = models.TextField(default="Nil")
    hint = models.TextField(null = True, blank = True)
    instruction = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Lab Tasks'
        ordering = ('lab_id', 'task_number')
        
    def __str__(self):
        return self.task
    
    
class GradesReport(models.Model):
    date = models.DateTimeField(default=timezone.now, null=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course_topic = models.ForeignKey(CourseTopic, on_delete = models.CASCADE, related_name='grades',related_query_name='grade')
    #task_no = models.IntegerField()
    score = models.IntegerField()
    grade = models.CharField(default='not graded', max_length=20)
    
    class Meta:
        verbose_name_plural = 'Grades Reports'
    
    def __str__(self):
        return self.user_id, self.lab, self.grade, self.date, self.score


def content_file_name(instance, filename):
    # Need to rework this method, as it is identifying topics by topic_number. it should recognized them by something else.
    ext = ''
    if instance.course_topic.topic_number == 4:
        ext = 'py'
    elif instance.course_topic.topic_number > 4 and instance.course_topic.topic_number < 7 :
        ext = 'sql'
    else:
        if filename.endswith('.zip'):
            ext = 'zip'
        elif filename.endswith('tar'):
            ext = 'tar'
        else:
            ext = 'gz'
    filename = "%s_%s.%s" % (instance.user.last_name, instance.course_topic.topic_number, ext)
    return os.path.join('uploads', filename)


class Document(models.Model):
    course_topic = models.ForeignKey(CourseTopic, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    document = models.FileField(upload_to = content_file_name )
    uploaded_at = models.DateTimeField(auto_now_add = True)


class MainModel(models.Model):
    title = models.CharField(max_length = 42)
    document = models.ForeignKey(Document, on_delete = models.CASCADE)

