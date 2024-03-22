import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from clientes.models import Cliente
from faker import Faker
from validate_docbr import CPF
import random

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome=fake.name()
        email='{}@{}'.format(nome, fake.free_email_domain())
        email = email.replace(' ', '').replace('.', '').lower()
        cpf=cpf.generate()
        rg='{}{}{}{}'.format(random.randint(10, 99), random.randint(100, 999), random.randint(100, 999), random.randint(0, 9))
        celular='{} 9{}-{}'.format(random.randint(10, 99), random.randint(10000, 99999), random.randint(1000, 9999))
        ativo=random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
        p.save()

criando_pessoas(50)
print('50 pessoas criadas com sucesso!')
