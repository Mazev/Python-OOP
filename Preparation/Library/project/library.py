from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.book_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)


    def remove_user(self, user: User):
        if user  in self.user_records:
            self.user_records.remove(user)
            if user.username in self.rented_books:
                del self.rented_books[user]

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        filtred_user = [u for u in self.user_records if u.user_id == user_id]
        if filtred_user:
            user = filtred_user[0]
            if not user.username == new_username:
                old_username = user.username
                user.username = new_username
                if old_username in self.rented_books:
                    books_for_user = self.rented_books[old_username]
                    del self.rented_books[old_username]
                    self.rented_books[old_username] = books_for_user
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            else:
                return f"Please check again the provided username - it should be different than the username used so far!"
        else:
            return f"There is no user with id = {user_id}!"



user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))