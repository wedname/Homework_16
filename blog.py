from datetime import date


class Post:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.current_date = date.today()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('name must be a string')

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self._description = value
        else:
            raise ValueError('description must be a string')

    def get_short_description(self):
        data = self._description
        if len(data) > 150:
            return data[:148] + ".."
        else:
            return data


class Blog:

    def __init__(self, posts_list: list):
        self.posts_list = posts_list

    @property
    def posts_list(self):
        return self._posts_list

    @posts_list.setter
    def posts_list(self, value):
        if isinstance(value, list):
            self._posts_list = value
        else:
            raise ValueError('posts_list must be a list')

    def add_post(self, value_name: str, value_description: str):
        return self._posts_list.append(Post(value_name, value_description))

    def edit_post(self, value, value_name: str, value_description: str) -> list:
        for i in range(0, len(self._posts_list)):
            if self._posts_list[i] == value:
                self._posts_list[i].name(value_name)
                self._posts_list[i].description(value_description)
                self._posts_list[i].current_date = date.today()
            return self._posts_list[i]
        else:
            ValueError("No such item!")

    def delete_post(self, value):
        for i in range(0, len(self._posts_list)):
            if self._posts_list[i] == value:
                self._posts_list.pop(i)
            return self._posts_list
        else:
            ValueError("No such item!")

    def get_post(self, value):
        for i in range(0, len(self._posts_list)):
            if self._posts_list[i] == value:
                return self._posts_list[i]
        else:
            ValueError("No such item!")
