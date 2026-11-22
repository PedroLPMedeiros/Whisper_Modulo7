# Transcrição de Áudio com Whisper e Extração de Pontos-Chave com Ollama

Pipeline em Python que recebe um arquivo de áudio (`.wav`, `.ogg` `.mp3`), realiza a transcrição local com **OpenAI Whisper** e extrai os principais pontos-chave utilizando um modelo local via **Ollama**.

## Requisitos e Instalação

1. Instale o **FFmpeg** no sistema operacional e garanta que ele esteja no `PATH`.
2. Instale o **Ollama** e baixe um modelo (ex.: `llama3.2`):
   ```bash
   ollama pull llama3.2

Vamos estruturar o pipeline completo em Python para **transcrever áudios (`.wav` ou `.mp3`) com o Whisper** e **extrair os pontos-chave com o Ollama**, pronto para rodar no seu ambiente local (VS Code + `.venv` + Ollama).

---


## Como Executar

Com o serviço do Ollama ativo, execute:

```bash
python pipeline.py amostras/audio_exemplo.mp3

```

### Exemplos de Uso

* Especificar o tamanho do modelo Whisper e o modelo do Ollama:
```bash
python pipeline.py amostras/reuniao.wav --whisper-model small --ollama-model llama3.2

```


## Link para o vídeo: https://www.loom.com/share/2f0b67de529e410cbef29b1729f6a51f