import json
from collections import Counter
from itemadapter import ItemAdapter


class JobinjaPipeline:
    def open_spider(self, spider):
        self.data = []
        
    def process_item(self, item, spider):
        name = item.get("name")
        if name is not None:
            self.data.append(name)
            
    def close_spider(self, spider):
        if len(self.data):
            name_count = Counter(self.data)
            with open("technologies.json", "w") as f:
                json.dump(dict(name_count), f, indent=4, ensure_ascii=False)
