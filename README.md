# DialogAI

Esse é um projeto pessoal que desenvolvi para criar um chatbot interativo usando LangChain com Azure OpenAI e Streamlit para fornecer interface gráfica. O assistente se chama **DialogAI** e foi desenvolvido para responder de forma clara, objetiva e com um toque mais humano, adaptando o tom da conversa de acordo com a energia da mensagem do usuário.

---

## Funcionalidades

- Responde perguntas de forma clara e objetiva
- Mantém o histórico da conversa
- Resume textos em até 5 linhas
- Adapta o tom da resposta com base na emoção da mensagem
- Escolhe automaticamente entre resposta ou resumo, dependendo da intenção

---
## Configurações Necessárias


Todas as dependências necessárias para rodar o projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```bash
pip install -r requirements.txt
```

Este projeto utiliza variáveis de ambiente para armazenar informações sensíveis, como chaves de API e endpoints. Por segurança, o arquivo `.env` não está incluído no repositório.

Para executar o chatbot corretamente, você deve criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_DEPLOYMENT=your_deployment_name_here
AZURE_OPENAI_API_VERSION=version_here
```

## Como rodar o projeto

### Usando Git (recomendado)

Com o Git instalado, clone o repositório com:

```bash
git clone https://github.com/giocarreira/ChatBot_Gigi_Carreira.git
cd ChatBot_Gigi_Carreira
streamlit run main.py

