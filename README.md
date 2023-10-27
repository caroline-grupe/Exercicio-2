# Exercicio-2
Segundo trabalho da aula de Técnicas de Desenvolvimento de Software Livre: criar uma classe para controle de usuário usando hash em pyhton

### Parte 1

Foi importado algoritmo SHA256 da biblioteca hashlib para que fosse possível aramzenar o hash da senha do usuário, garantindo uma segurança maior do banco de dados de senhas (hashs).

Foi criada uma classe chamada "Usuário" para caracterizar usuários com um nome, uma senha e um nível (moderador, administrador ou funcionário).
Dentro dessa classe, foi feita uma função para transformar a senha respectiva do usuário em um hash (função "hash_senha") e uma outra função para fazer a verificação da senha (função "verificacao_senha"), ou seja, confirmar se o hash da senha escrita pelo usuário é idêntica ao hash da senha cadastrada para esse usuário.

### Parte 2

Foram definidos quatro objetos da classe como usuários que já haviam sido cadastrados no site da empresa.

### Parte 3

Foi feito um input para nome e senha para poder coletar esses dados e utilizar o controle de usuário criado.

Para isso, após a coleta de nome e senha, foi feito um teste para cada nome de usuário cadastrado (verificando qual usuário que fez login). Em cada teste, foi criado o hash da senha colocada no momento do login (usando a função da classe "hash_senha") e depois foi testada se o hash da senha no momento de login é igual ao hash da senha armazenado na hora do cadastro (usando a função da classe "verificacao_senha"). Se os hashs eram idênticos, o código imprime que a senha está correta e qual o nível do usuário que acabou de fazer login. Caso contrário, o código impreme que a senha está incorreta e o procedimento deve se iniciar novamente.


