# Laços Cifrados

**Laços Cifrados** é um jogo 2D de mistério, exploração e resolução de enigmas, desenvolvido inteiramente em Python utilizando a biblioteca [Pygame](https://www.pygame.org/). Este projeto foi criado como um trabalho acadêmico para a disciplina de Lógica de Programação.

---

## 📖 História
Camila, Gabi e Millena finalmente conseguiram um tempo livre para relaxar e fazer um acampamento juntas na floresta. Tudo parecia perfeito ao redor da fogueira, até que um estrondo alto ecoou de trás das árvores. 

Camila e Gabi decidem ir investigar... e de repente, um grito corta o silêncio. Elas desapareceram. Agora, cabe a você explorar o local, desvendar pistas e resolver o mistério para encontrá-las antes que seja tarde demais.


## 🎮 Controles
O jogo possui controles simples e intuitivos para movimentação e interação:

| Tecla | Ação |
| :---: | :--- |
| **W** | Mover para cima |
| **A** | Mover para a esquerda |
| **S** | Mover para baixo |
| **D** | Mover para a direita |
| **ESPAÇO** | Pular |
| **E** | Interagir (Avançar cutscenes, ler papéis, interagir com celas) |
| **ESC** | Sair / Voltar / Fechar interface |
| **ENTER** | Iniciar o jogo / Confirmar enigma |

## ⚙️ Funcionalidades e Mecânicas
- **Movimentação 2D:** Explore o cenário para encontrar respostas.
- **Interação:** Colete papéis e dicas espalhados pelo mapa apertando a tecla `E`.
- **Inimigos e Armadilhas:** Tome cuidado com Aranhas e Armadilhas pelo caminho. Você possui uma vida limitada!
- **Sistema de Enigma:** Use as dicas encontradas para decifrar a senha no final do jogo e resgatar suas amigas.
- **Finais Múltiplos:** O jogo possui um *Good Ending* (se você resolver o enigma) e um *Bad Ending* (se você perder toda sua vida).

---

## 🚀 Como Executar o Jogo

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) (versão 3.x) instalado em sua máquina.

### Instalação

1. Clone ou baixe este repositório para o seu computador.

```bash
    git clone https://github.com/Justi-Camila/lacos-cifrados-jogo.git
```

2. Abra o terminal na pasta raiz do projeto.
3. (Opcional, mas recomendado) Crie e ative um ambiente virtual (`.venv`).
```bash
    python -m venv .venv
```

```bash
    # No Windows:
    .venv\Scripts\activate
```

4. Instale as dependências necessárias através do arquivo `requirements.txt`:
```bash
    pip install -r requirements.txt
```

### Iniciando
Após a instalação das dependências, basta executar o arquivo `main.py` para iniciar o jogo:
```bash
    python main.py
```

---

## 📦 Como Gerar o Executável (.exe)

Se você deseja compilar o jogo em um arquivo executável para rodar no Windows sem precisar do Python instalado, siga os passos abaixo:

### 1. Instale o PyInstaller
No seu terminal (com o ambiente virtual ativo, se estiver usando), instale o PyInstaller:
```bash
    pip install pyinstaller
```

### 2. Gere o arquivo .exe
Execute o comando abaixo para compilar o projeto:
```bash
    python -m PyInstaller --onefile --noconsole main.py
```

```
Nota: A flag --noconsole impede que a janela preta do terminal/prompt de comando abra junto com o jogo.
```

### 3. Organize as pastas do jogo
Após a compilação, o PyInstaller criará uma pasta chamada dist/. Dentro dela estará o seu arquivo main.exe.

Importante: Copie a pasta assets/ para dentro da pasta dist/ (ao lado do arquivo main.exe), para que o jogo consiga carregar as imagens, sons e fontes corretamente.

Agora é só dar dois cliques no main.exe e jogar! 🎮

---

## 📁 Estrutura do Projeto
- `main.py`: Arquivo principal responsável por iniciar a execução do jogo.
- `requirements.txt`: Lista de dependências (Pygame).
- `assets/`: Pasta contendo os recursos visuais e sonoros do jogo (imagens, fontes, áudios).
- `scripts/`: Pasta que contém todo o código-fonte do jogo dividido em módulos orientados a objetos (Game, Level, Player, Entidades, Menus, Constantes, etc.).

## 📝 Créditos e Recursos Utilizados
Conforme os agradecimentos no final do jogo:
- **Imagens e Sprites:** Feitas no aplicativo Pixel Studio.
- **Áudios e Efeitos Sonoros:** Retirados do [Freesound.org](https://freesound.org/).
- **Fonte:** Utilizada a fonte do [dafont.com.br](https://www.dafont.com/pt/).
