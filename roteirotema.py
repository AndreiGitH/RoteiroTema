import streamlit as st
from google import genai

# App Streamlit para gerar roteiros de vídeos no YouTube baseado em tema e tamanho desejado

def main():
    # Configuração da página com ícone
    st.set_page_config(page_title="Roteiro YouTube AI", page_icon="📜", layout="wide")

    st.title("Gerador de Roteiro para Vídeos Cristãos")
    st.markdown("Escolha o tema bíblico e o tamanho do roteiro em palavras para criar conteúdo focado no público cristão.")

    # Configuração da API key (não exposta)
    api_key = st.secrets.get("google_api_key", "")
    client = genai.Client(api_key=api_key)

    # Sidebar para escolha de modelo
    st.sidebar.header("Configurações do Modelo")
    default_model = st.secrets.get("default_model", "gemini-2.5-pro-exp-03-25")
    model_name = st.sidebar.text_input("Modelo GenAI", value=default_model)

    # Inputs principais
    tema = st.text_input("Tema Bíblico Específico:", "")
    num_palavras = st.number_input("Número aproximado de palavras:", min_value=100, max_value=10000, value=1000, step=50)

    # Geração do roteiro
    if st.button("Gerar Roteiro", key="btn_gen_script"):
        if not tema.strip():
            st.error("Por favor, preencha o tema bíblico.")
        else:
            with st.spinner("Gerando roteiro..."):
                prompt_script = (
                    f"Crie um roteiro para um vídeo do YouTube com aproximadamente {num_palavras} palavras, focado no público cristão, "
                    f"sobre o tema bíblico: \"{tema}\".\n\n"
                    "O objetivo é gerar grande interesse e alta retenção. Incorpore os seguintes elementos e estrutura, "
                    "modelados a partir de roteiros de sucesso anteriores e sugestões de melhoria:\n\n"
                    "I. INTRODUÇÃO E GANCHO (10-15%): Gancho forte, conexão com o público, promessa de valor clara e chamada breve para engajamento inicial.\n"
                    "II. DESENVOLVIMENTO (60-70%): Divida em pontos claros com exemplo bíblico, aplicação contemporânea, gatilho de curiosidade e linguagem emocional.\n"
                    "III. CONCLUSÃO E CHAMADAS FINAIS (15-20%): Recapitulação breve, encorajamento, compromisso espiritual, inscrição, compartilhamento, oração e bênção final.\n\n"
                    "Use tom pastoral, empático e com autoridade espiritual. O texto já deve estar pronto para narração TTS.\n"
                )
                roteiro = call_genai(client, model_name, prompt_script)
                st.session_state.roteiro = roteiro

    # Exibição sempre visível do roteiro gerado
    roteiro = st.session_state.get("roteiro", "")
    st.subheader("Roteiro Gerado")
    st.text_area("", roteiro, height=300, key="script_box", disabled=True)
    if roteiro:
        st.download_button(
            label="Baixar Roteiro (.txt)",
            data=roteiro,
            file_name="roteiro_youtube.txt",
            mime="text/plain"
        )

    # Geração de descrição, hashtags, tags e sugestão de thumb
    if st.button("Gerar Descrição e Metadados", key="btn_gen_meta"):
        if not st.session_state.get("roteiro"):
            st.error("Gere primeiro o roteiro antes de criar metadados.")
        else:
            with st.spinner("Gerando descrição, hashtags, tags e thumb..."):
                prompt_meta = (
                    f"Com base no roteiro acima, crie: 1) descrição de vídeo de até 1000 caracteres; "
                    "2) hashtags entre vírgulas; 3) tags separadas por vírgulas; 4) descrição em texto para thumbnail que gere curiosidade, benefício e urgência.\n\n"
                    + st.session_state.roteiro
                )
                meta = call_genai(client, model_name, prompt_meta)
                st.session_state.meta = meta

    # Exibição sempre visível dos metadados
    meta = st.session_state.get("meta", "")
    st.subheader("Descrição, Hashtags, Tags e Thumb")
    st.text_area("", meta, height=300, key="meta_box", disabled=True)
    if meta:
        st.download_button(
            label="Baixar Metadados (.txt)",
            data=meta,
            file_name="meta_youtube.txt",
            mime="text/plain"
        )


def call_genai(client, model: str, prompt: str) -> str:
    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    return response.text.strip()


if __name__ == "__main__":
    main()
