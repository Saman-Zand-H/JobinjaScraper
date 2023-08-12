import json
from django.views import View
from django.db.models import Sum, Avg
from django.shortcuts import render

from .models import DemandTechnology


class HomeView(View):
    template_name = "demands/index.html"
    
    def get(self, *args):
        tech_data = (
            DemandTechnology
            .objects
            .all()
            .order_by("-count")[:20]
            .values("name", "count")
        )
        others_count = 0
        if DemandTechnology.objects.count() > 20:
            others_count = (
                DemandTechnology
                .objects
                .all()[20:]
                .aggregate(s=Sum("count"))["s"]
            )
            
        chart_data = {
            i["name"]: i["count"] for i in tech_data.iterator()
        } | {"others": others_count}
        
        avg_count = DemandTechnology.objects.aggregate(a=Avg("count"))["a"]
        
        context = {
            "chart_data": chart_data,
            "data": (
                DemandTechnology
                .objects
                .filter(count__gt=avg_count)
                .order_by("-count")
                .values("name", "count")
            )
        }
        return render(self.request, self.template_name, context)
