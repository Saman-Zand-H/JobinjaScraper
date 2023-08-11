from collections import Counter
from twisted.internet import threads

from demand.models import DemandTechnology


class JobinjaPipeline:
    def open_spider(self, spider):
        self.items = []
        
    def process_item(self, item, spider):
        if item.get("name") is not None:
            self.items.append(item["name"])
            
    def close_spider(self, spider):
        # doing this helps us avoid thread related conflicts
        threads.deferToThread(self.perform_bulk_create)
    
    def perform_bulk_create(self):
        name_count = Counter(self.items)
        data = DemandTechnology.objects.bulk_create(
            [
                DemandTechnology(name=name, count=count)
                for name, count in name_count.items()
            ],
            update_conflicts=True,
            update_fields=["count"]
        )
