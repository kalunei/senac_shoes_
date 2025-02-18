## PASSO A  PASSO PARA UTILIZAÇÃO BÁSICA DO GIT\GITHUB


# 1. 
Ir no github e criar repositório do projeto;

# 2. 
Abrir o diretório do projeto no VScode;

# 3. 
Abrir tela do terminal do VScode (CTRl + J);

# 4. git init -->
Cria o repositório local do projeto na pasta onde ele está armazenado;

# 5. 
Informar as credenciais do git, isso é realizado uma única vez no computador;
<!-- 
    git config --global user.name "Seu Nome"
    git config --global user.email "artur" 
-->

# 6. git status -> 
verifica quais arquivos/pastas foram enviados para o repositório local;

# 7. git add . ->
Inclui todos os arquivos/pastas no repositório local;

# 8. git branch -M main -> 
Altera o nome da branch atual para main;

# 9. git commit -m "--O comentário fica aqui--" ->
Realiza um novo commit no repositório local;

# 10. git remote add origin endereço_do_repositório_remoto ->
Comando p. realizar a sincronização do repositório local com o remoto;

# 11. git push -u origin main -> 
Envia o repositório local para o remoto;