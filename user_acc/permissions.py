from rest_framework.permissions import BasePermission
from datetime import datetime

class WorkingHoursPermission(BasePermission):
    message = "Detail va Lits faqat Dushanbadan Jumagacha ishlaydi"

    def has_permission(self, request, view):
        now = datetime.now().time()
        start = datetime.strptime("09:00", "%H:%M").time()
        end = datetime.strptime("18:00", "%H:%M").time()


        return start <= now <= end

