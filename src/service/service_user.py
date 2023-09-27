from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def is_string(self, attribute):
        return isinstance(attribute, str)

    def find_user(self, name):
        for u in self.store.bd:
            if u.name == name:
                return u
        return None

    def get_user_by_name(self, name):
        if name is not None:
            if self.is_string(name):
                user = self.find_user(name)
                if user is not None:
                    return name + " - " + user.job
                else:
                    return "Usuário inexistente"
        return "Usuário deve ser do tipo string"

    def update_user(self, name, job):
        if name is not None and job is not None:
            if (self.is_string(name) and self.is_string(job)):
                user = self.find_user(name)
                if user is not None:
                    user.job = job
                    return "Job alterado com sucesso"
                else:
                    return "Usuário inexistente"
        return "Usuário deve ser do tipo string"

    def add_user(self, name, job):
        if name is not None and job is not None:
            if (self.is_string(name) and self.is_string(job)):
                if self.find_user(name) is not None:
                    return "Usuário já existe"
                else:
                    user = User(name=name, job=job)
                    self.store.bd.append(user)
                    return "Usuário adicionado"
        return "Usuário deve ser do tipo string"

    def remove_user(self, name):
        if name is not None and self.is_string(name):
            user = self.find_user(name)
            if user is not None:
                self.store.bd.remove(user)
                return "Usuário removido com sucesso"
            else:
                return "Usuário inexistente"
        return "Usuário deve ser do tipo string"
