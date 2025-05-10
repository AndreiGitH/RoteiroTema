import streamlit as st
from google import genai

# App Streamlit para gerar roteiros de vídeos no YouTube baseado em tema e tamanho desejado

def main():
    # Configuração da página com ícone
    st.set_page_config(page_title="Roteiro YouTube AI", page_icon="📜", layout="wide")

    st.title("Gerador de Roteiro para Vídeos")
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
                prompt_script = f"Crie um roteiro pronto para narração TTS (semmarcações) para um vídeo do YouTube com aproximadamente {num_palavras} palavras, focado no público cristão, sobre o tema bíblico: \"{tema}\".\n\n" + \
                "**I. INTRODUÇÃO E GANCHO (Aproximadamente 10-15% do roteiro):**\n\n" + \
                "1.  **Gancho Forte e Variado:**\n" + \
                "    *   Comece com uma pergunta retórica impactante, uma breve e vívida vinheta/história hipotética que o espectador possa se identificar, uma citação bíblica poderosa e menos conhecida, ou uma estatística surpreendente (se aplicável e verdadeira) relacionada ao tema.\n" + \
                "    *   **Exemplo de Variação:** \"[Comece com uma imagem mental forte: 'Imagine [personagem bíblico/situação] enfrentando [desafio relacionado ao tema]... Essa luta antiga ecoa em nossos corações hoje quando lidamos com [aspecto moderno do tema]...']\"\n\n" + \
                "2.  **Conexão Imediata:** Relacione o gancho diretamente às dores, dúvidas, anseios ou curiosidades do público sobre o [TEMA BÍBLICO ESPECÍFICO].\n\n" + \
                "3.  **Promessa de Valor Clara:**\n" + \
                "    *   Declare explicitamente o que o espectador vai aprender ou descobrir (ex: \"Nos próximos minutos, você vai descobrir [NÚMERO] chaves/sinais/princípios sobre [TEMA BÍBLICO ESPECÍFICO]\", \"Vamos desvendar juntos como [aspecto do tema] pode transformar sua vida espiritual.\").\n" + \
                "    *   Mencione que o conteúdo é baseado em ensinamentos bíblicos profundos.\n\n" + \
                "4.  **Chamada para Engajamento Inicial (Opcional, mas recomendado):**\n" + \
                "    *   Convide a comentar uma frase específica de fé/código espiritual (ex: \"Paz em Cristo\", \"Fé na Palavra\") para criar senso de comunidade.\n" + \
                "    *   Peça para curtir e se inscrever, explicando brevemente o impacto disso para o ministério/canal e para alcançar outras pessoas.\n" + \
                "    *   **Nota de Melhoria:** \"[Seja breve e direto nesta chamada inicial para não perder retenção logo no começo. Pode ser melhor posicionar uma chamada mais elaborada para inscrição um pouco mais adiante ou no final.]\"\n\n" + \
                "**II. DESENVOLVIMENTO DO CONTEÚDO (Aproximadamente 60-70% do roteiro):**\n\n" + \
                "1.  **Estrutura de Lista Clara:**\n" + \
                "    *   Divida o conteúdo principal em [NÚMERO ESPECÍFICO, ex: 5-8] pontos, sinais, princípios, ou passos claramente definidos. Use frases de transição curtas e diretas entre eles. Abra loops entre as partes.\n\n" + \
                "2.  **Para cada Ponto/Sinal/Princípio:**\n" + \
                "    *   **Apresentação:** Introduza o ponto de forma concisa.\n" + \
                "    *   **Exemplo Bíblico Central:** Utilize uma história, personagem ou passagem bíblica relevante para ilustrar e fundamentar o ponto. Narre de forma envolvente, destacando os aspectos cruciais.\n" + \
                "    *   **Aplicação Contemporânea:** Conecte o ensinamento bíblico às experiências, emoções e desafios atuais do espectador. Use linguagem que gere identificação.\n" + \
                "    *   **Aprofundamento e Insight:** Ofereça uma perspectiva espiritual, um \"segredo\" ou uma interpretação menos óbvia sobre o ponto, mostrando o \"porquê\" divino por trás dele.\n" + \
                "    *   **Reflexão/Pergunta Intercalada (Opcional):** \"[Faça uma pergunta direta ao espectador relacionada ao ponto recém-explicado para estimular reflexão interna. Ex: 'Você já vivenciou [situação do ponto]? Como isso impactou sua fé?']\"\n\n" + \
                ""3.  **\"Gatilho de Curiosidade\" Estratégico:**\n" + \
                "    *   Se o roteiro for dividido em múltiplos pontos, mencione que um dos pontos vindouros (ex: \"o penúltimo\", \"o terceiro\") contém uma revelação/chave particularmente importante ou transformadora. \"[Entregue essa promessa com impacto, talvez com um tom ligeiramente diferente ou maior profundidade.]\"\n\n" + \
                ""4.  **Linguagem Emocional e Encorajadora:**\n" + \
                "    *   Use palavras que toquem o coração e transmitam esperança, consolo, e a natureza amorosa e sábia de Deus, mesmo ao abordar temas difíceis.\n\n" + \
                ""5.  **Notas de Produção (Implícitas no Estilo):**\n" + \
                "    *   \"[O texto deve naturalmente sugerir pausas, mudanças de inflexão e momentos de maior intensidade. Pense em como seria a narração ideal ao escrever.]\"\n" + \
                "    *   \"[Considere momentos onde um texto-chave na tela poderia reforçar o ponto principal sendo discutido.]\"\n\n" + \
                ""**III. CONCLUSÃO E CHAMADAS FINAIS (Aproximadamente 15-20% do roteiro):**\n\n" + \
                "1.  **Recapitulação Breve (Opcional):** Reforce a mensagem central ou os principais aprendizados de forma concisa.\n\n" + \
                "2.  **Mensagem de Encorajamento e Esperança:** Conecte o [TEMA BÍBLICO ESPECÍFICO] com a ação de Deus na vida do espectador.\n\n" + \
                "3.  **Chamada para Compromisso/Ação Espiritual:**\n" + \
                "    *   Peça para o espectador comentar uma frase específica que demonstre seu entendimento ou compromisso com a mensagem (ex: \"Eu escolho confiar no plano de Deus\", \"Senhor, guia meus passos\").\n" + \
                "    *   Explique o significado espiritual dessa declaração.\n\n" + \
                "4.  **Chamada para Inscrição e Compartilhamento (Mais Elaborada):**\n" + \
                "    *   Reforce a importância de se inscrever para continuar recebendo conteúdo que edifica a fé.\n" + \
                "    *   Motive o compartilhamento, explicando como isso pode abençoar outras vidas. \"[Seja específico: 'Compartilhe este vídeo com [NÚMERO] pessoas que você sente que precisam desta palavra hoje.']\"\n\n" + \
                "5.  **Oração/Momento de Reflexão Final (Característica Forte):**\n" + \
                "    *   Sugira um momento de silêncio, oração ou reflexão, acompanhado por música (mencione o tipo de música).\n" + \
                "    *   Encoraje o espectador a permanecer até o fim para absorver a mensagem e sentir a presença de Deus.\n\n" + \
                "6.  **Bênção Final:** Termine com uma bênção ou palavras de paz.\n\n" + \
                ""**Considerações Adicionais para o Prompt:**\n" + \
                "*   **Tom:** \"[Mantenha um tom pastoral, empático, mas também com autoridade espiritual, baseado na Palavra.]\"\n" + \
                "*   **Linguagem:** \"[Use linguagem acessível, mas com profundidade bíblica. Evite jargões teológicos excessivos sem explicação  Evite abreviaturas. O texto já deve estar pronto para narração TTS. Caso queira uma pausa maior na narração, use '...'.]\"\n" + \
                "*   **Foco na Aplicação Prática:** \"[Embora profundamente bíblico, o roteiro deve sempre buscar responder à pergunta 'Como isso se aplica à minha vida hoje?']\""
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
