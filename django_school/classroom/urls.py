from django.urls import include, path

from .views import classroom, students, teachers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('submit_details', students.StudentDetailsView.as_view(),
             name='submit_details'),
        path('student_info', students.student_attendance_detail,
             name='submit_details'),
        path('<str:name>', students.student_attendance_detail2,
             name='submit_details2')
     ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('',
             TemplateView.as_view(
              template_name='classroom/teachers/dashboard.html'),
             name='dashboard'),
        path('attendance', teachers.AttendanceView.as_view(),
             name='attendance'),
        path('download_attendance', teachers.download_attendance,
             name='download_csv'),
        path('students_list', teachers.students_list, name='students_list')
     ], 'classroom'), namespace='teachers')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
