class Storage:
    def __init__(self):
        self.categories = []
        self.topic = []
        self.documents = []

    def __repr__(self):
        return f"{self.categories} , {self.topic},  {self.documents}"


    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topic:
            self.topic.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topic if t.id == topic_id][0]
        topic.edit(new_topic)

    def edit_document(self, document_id, new_file_name):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.edit(new_file_name)

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        category.remove(category_id)

    def delete_topic(self, topic_id):
        del_topic = [d for d in self.topic if d.id == topic_id][0]
        del_topic.remove(topic_id)

    def delete_document(self, document_id):
        del_doc = [d for d in self.documents if d.id == document_id][0]
        del_doc.remove(document_id)

    def get_document(self, document_id):
        get_doc = [d for d in self.documents if d.id == document_id][0]
        return get_doc
