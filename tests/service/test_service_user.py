import unittest

from src.service import service_user
from src.service.service_user import ServiceUser


class ServiceUserTest(unittest.TestCase):
    add_successful_message = "Usuário adicionado"
    add_existing_user_error_message = "Usuário já existe"
    add_invalid_user_error_message = "Usuário deve ser do tipo string"
    update_job_successful_message = "Job alterado com sucesso"
    remove_user_successful_message = "Usuário removido com sucesso"
    remove_user_nonexistent_message = "Usuário inexistente"

    def test_add_user_success(self):
        service_user = ServiceUser()
        message = service_user.add_user("Ana", "Arquiteta")
        self.assertEqual(message, self.add_successful_message)

    def test_add_existing_user(self):
        service_user = ServiceUser()
        service_user.add_user("Ana", "Arquiteta")
        message = service_user.add_user("Ana", "Arquiteta")
        self.assertEqual(message, self.add_existing_user_error_message)

    def test_add_user_name_none(self):
        service_user = ServiceUser()
        message = service_user.add_user(None, "Engenheiro")
        self.assertEqual(message, self.add_invalid_user_error_message)

    def test_add_user_invalid_name_string(self):
        service_user = ServiceUser()
        message = service_user.add_user(12, "Professor")
        self.assertEqual(message, self.add_invalid_user_error_message)

    def test_add_user_job_none(self):
        service_user = ServiceUser()
        message = service_user.add_user("Ana", None)
        self.assertEqual(message, self.add_invalid_user_error_message)

    def test_add_user_invalid_job_string(self):
        service_user = ServiceUser()
        message = service_user.add_user("Fabio", 1234)
        self.assertEqual(message, self.add_invalid_user_error_message)

    def test_remove_user_success(self):
        service_user = ServiceUser()
        service_user.add_user("Alana", "Arquiteta")
        message = service_user.remove_user("Alana")
        self.assertEqual(message, self.remove_user_successful_message)

    def test_remove_user_nonexistent(self):
        service_user = ServiceUser()
        message = service_user.remove_user("Alana")
        self.assertEqual(message, self.remove_user_nonexistent_message)

    def test_remove_user_value_none(self):
        service_user = ServiceUser()
        message = service_user.remove_user(None)
        self.assertEqual(message, self.add_invalid_user_error_message)

    def test_update_job_success(self):
        service_user = ServiceUser()
        service_user.add_user("Jonas", "Eletricista")
        message = service_user.update_user("Jonas", "Professor")
        self.assertEqual(message, self.update_job_successful_message)

    def test_update_job_user_nonexistent(self):
        service_user = ServiceUser()
        message = service_user.update_user("Paulo", "Professor")
        self.assertEqual(message, self.remove_user_nonexistent_message)

    def test_update_job_user_invalid(self):
        service_user = ServiceUser()
        message = service_user.update_user(123, 345)
        self.assertEqual(message, self.add_invalid_user_error_message)

    def test_get_user_name_successful(self):
        service_user = ServiceUser()
        name = "Jonas"
        job = "Eletricista"
        service_user.add_user(name, job)
        message = service_user.get_user_by_name("Jonas")
        self.assertEqual(message, name + " - " + job)

    def test_get_user_name_nonexistent(self):
        service_user = ServiceUser()
        message = service_user.get_user_by_name("Pedro")
        self.assertEqual(message, self.remove_user_nonexistent_message)

    def test_get_user_name_invalid_string(self):
        service_user = ServiceUser()
        message = service_user.get_user_by_name(None)
        self.assertEqual(message, self.add_invalid_user_error_message)