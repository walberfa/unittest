import unittest
import login


class TestLogin(unittest.TestCase):

    def test_admin_login(self):
        # Testando a tupla do admin
        self.assertTupleEqual(login.usuarios[0], ('admin', 'admin123'))

    def test_list_usuarios(self):
        # cria lista
        users = []
        # captura os nomes dos usuarios
        for value in login.usuarios:
            users.append(value[0])
        # Testa se a lista de usuarios atual é igual ao armazenado
        self.assertEqual(users, ['admin', 'pedrosilva1235', 'brunolaje12', 'teste223', 'dioguinho123', 'walber42'])


if __name__ == '__main__':
    unittest.main()
