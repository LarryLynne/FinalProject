from abc import abstractmethod, ABC

class UserInterface(ABC):
    @abstractmethod
    def separation(self):
        pass

    @abstractmethod
    def show_user_info(self):
        pass


class View(UserInterface):
    def __init__(self, name="", phone="", birth="", email="", status="", note=""):
        self.name = name
        self.phone = phone
        self.birth = birth
        self.email = email
        self.status = status
        self.note = note

    def separation(self):
        return '-' * 50
    def show_user_info(self):
        pattern = "Name: {:<20} \n*  Phones: {:<20} \n*  Birthday: {:<20} \n*  Email: {:<20} \n*  Status: {:<20} \n*  Note: {:<20}"
        return pattern.format(self.name, self.phone, self.birth, self.email, self.status, self.note)

class HelpUser(UserInterface):
    def separation(self):
        return '- -' * 7
    def show_user_info(self):
        return "|{:^20}|"