class Storage:
    def __init__(self):
        self.categories = []
        self.topic = []
        self.documents = []

    def __repr__(self):
        pass

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
        pass

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        pass

    def edit_document(self, document_id, new_file_name):
        pass

    def delete_category(self, category_id):
        pass

    def delete_topic(self, topic_id):
        pass

    def delete_document(self, document_id):
        pass

    def get_document(self, document_id):
        pass
