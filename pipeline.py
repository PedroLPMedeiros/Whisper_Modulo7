import argparse
from pathlib import Path
import requests
import whisper

SUPPORTED_EXTENSIONS = {".wav", ".mp3", ".ogg"}
OLLAMA_URL = "http://localhost:11434/api/generate"


def transcrever_audio(caminho_audio: str, tamanho_modelo: str = "base") -> str:
    """Transcreve um arquivo .wav ou .mp3 usando o modelo Whisper."""
    arquivo = Path(caminho_audio)

    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    if arquivo.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Formato '{arquivo.suffix}' inválido. Envie um arquivo .wav, .mp3 ou .ogg."
        )

    modelo = whisper.load_model(tamanho_modelo)
    resultado = modelo.transcribe(str(arquivo))
    return resultado.get("text", "").strip()


def resumir_com_ollama(texto: str, modelo_ollama: str = "llama3.2") -> str:
    """Envia o texto transcrito ao Ollama e retorna os pontos-chave."""
    prompt = (
        "Extraia os principais pontos-chave do texto a seguir em tópicos objetivos "
        "e fiéis ao conteúdo:\n\n"
        f"{texto}"
    )

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": modelo_ollama,
            "prompt": prompt,
            "stream": False,
        },
        timeout=180,
    )
    resposta.raise_for_status()
    return resposta.json().get("response", "").strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pipeline de transcrição (.wav/.mp3) com Whisper e resumo com Ollama."
    )
    parser.add_argument("audio", help="Caminho para o arquivo .wav ou .mp3")
    parser.add_argument(
        "--whisper-model",
        default="small",
        help="Modelo do Whisper (ex.: tiny, base, small, medium, large)",
    )
    parser.add_argument(
        "--ollama-model",
        default="llama3.2",
        help="Modelo instalado no Ollama (ex.: llama3.2, qwen2.5)",
    )
    args = parser.parse_args()

    transcricao = transcrever_audio(args.audio, args.whisper_model)
    pontos_chave = resumir_com_ollama(transcricao, args.ollama_model)

    print("\n--- TRANSCRIÇÃO ---")
    print(transcricao)
    print("\n--- PONTOS-CHAVE ---")
    print(pontos_chave)


if __name__ == "__main__":
    main()