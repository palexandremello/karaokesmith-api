# Karaokesmith

Karaokesmith é um backend robusto que gera amostras de música e transforma música em karaokê usando inteligência artificial. Foi construído seguindo os princípios da Arquitetura Limpa (Clean Architecture) para garantir a separação de preocupações e a escalabilidade do projeto.

## Sobre

Este projeto pode aceitar uma música do YouTube ou um arquivo MP3, cortá-lo em N segmentos, ou pegar uma música inteira e transformá-la em uma faixa de karaokê. O tratamento de áudio é feito por uma inteligência artificial que pode separar a música dos vocais, permitindo que uma faixa instrumental limpa seja criada.

## Estrutura do Projeto

A estrutura de pastas e arquivos do projeto é a seguinte:

```bash
├── app
│   ├── application
│   │   ├── adapters
│   │   │   └── request_adapter_interface.py
│   │   ├── controllers
│   │   │   ├── create_karaoke
│   │   │   │   └── create_karaoke_controller.py
│   │   │   ├── create_sample
│   │   │   │   └── create_sample_controller.py
│   │   │   └── interface
│   │   │       └── controller_interface.py
│   │   └── helpers
│   │       └── http
│   │           ├── request.py
│   │           └── response.py
│   ├── domain
│   │   ├── entities
│   │   │   ├── audio_media.py
│   │   │   ├── __init__.py
│   │   │   ├── karaoke_file.py
│   │   │   ├── mp3_file.py
│   │   │   ├── sample.py
│   │   │   ├── video_metadata.py
│   │   │   ├── video_source.py
│   │   │   └── youtube_audio.py
│   │   ├── __init__.py
│   │   ├── repositories
│   │   │   ├── sample_repository_impl.py
│   │   │   └── sample_repository_interface.py
│   │   ├── services
│   │   │   ├── create_sample_service
│   │   │   │   ├── create_sample_service_interface.py
│   │   │   │   ├── create_sample_service.py
│   │   │   │   └── sampler_interface.py
│   │   │   ├── mp3_file
│   │   │   │   ├── mp3_file_service_interface.py
│   │   │   │   ├── mp3_file_service.py
│   │   │   │   └── mp3_file_validator_interface.py
│   │   │   ├── sample_saver
│   │   │   │   ├── sample_saver_interface.py
│   │   │   │   ├── sample_saver.py
│   │   │   │   └── save_method_interface.py
│   │   │   ├── video_converter
│   │   │   │   ├── converter_interface.py
│   │   │   │   ├── video_converter_service_interface.py
│   │   │   │   └── video_converter_service.py
│   │   │   └── youtube_video
│   │   │       ├── youtube_video_downloader_interface.py
│   │   │       ├── youtube_video_service_interface.py
│   │   │       └── youtube_video_service.py
│   │   ├── usecases
│   │   │   ├── create_karaoke_from_youtube
│   │   │   │   ├── create_karaoke_from_youtube_interface.py
│   │   │   │   └── create_karaoke_youtube_impl.py
│   │   │   ├── create_karaoke_music
│   │   │   │   ├── create_karaoke_impl.py
│   │   │   │   └── create_karaoke_interface.py
│   │   │   ├── create_sample_from_mp3
│   │   │   │   ├── create_sample_from_mp3_impl.py
│   │   │   │   └── create_sample_from_mp3_interface.py
│   │   │   ├── create_sample_from_youtube
│   │   │   │   ├── create_sample_from_youtube_impl.py
│   │   │   │   └── create_sample_from_youtube_interface.py
│   │   │   ├── get_youtube_video
│   │   │   │   ├── get_youtube_video_impl.py
│   │   │   │   └── get_youtube_video_interface.py
│   │   │   ├── mp3_file
│   │   │   │   ├── mp3_file_impl.py
│   │   │   │   └── mp3_file_interface.py
│   │   │   ├── sample
│   │   │   │   ├── sample_impl.py
│   │   │   │   └── sample_interface.py
│   │   │   ├── save_karaoke
│   │   │   │   ├── save_karaoke_impl.py
│   │   │   │   └── save_karaoke_interface.py
│   │   │   ├── save_sample
│   │   │   │   ├── save_sample_impl.py
│   │   │   │   └── save_sample_interface.py
│   │   │   ├── video_to_audio_converter
│   │   │   │   ├── video_to_audio_converter_impl.py
│   │   │   │   └── video_to_audio_converter_interface.py
│   │   │   └── youtube_audio
│   │   │       ├── youtube_audio_impl.py
│   │   │       └── youtube_audio_interface.py
│   │   └── validators
│   │       ├── audio_validators
│   │       │   ├── mp3_validator_impl.py
│   │       │   └── mp3_validator_interface.py
│   │       └── video_validators
│   │           ├── youtube_validator_impl.py
│   │           └── youtube_validator_interface.py
│   ├── errors
│   │   ├── http_errors.py
│   │   └── service_errors.py
│   ├── infra
│   │   ├── gateways
│   │   │   ├── youtube_dl
│   │   │   │   ├── youtube_dl_gateway.py
│   │   │   │   └── youtube_dl_gateway_interface.py
│   │   │   └── ffmpeg
│   │   │       ├── ffmpeg_gateway.py
│   │   │       └── ffmpeg_gateway_interface.py
│   │   ├── repositories
│   │   │   └── sample_repository.py
│   │   └── validators
│   │       ├── audio_validators
│   │       │   └── mp3_validator.py
│   │       └── video_validators
│   │           └── youtube_validator.py
│   └── main
│       ├── config.py
│       ├── routers
│       │   ├── create_karaoke_router.py
│       │   ├── create_sample_router.py
│       │   └── router.py
│       └── server.py
└── tests

```

## Como usar

1. Clone este repositório.
2. Instale as dependências necessárias.
3. Execute o servidor backend.
4. Use a API para enviar solicitações HTTP para gerar amostras de músicas ou transformá-las em faixas de karaokê.

## Requisitos

- Python 3.7 ou superior
- FFmpeg
- youtube-dl
- Outras dependências do Python que estão no arquivo `requirements.txt`.

## Instalação

```bash
git clone https://github.com/palexandremello/karaokesmith.git
cd karaokesmith
pip install -r requirements.txt
