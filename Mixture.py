import streamlit as st
import asyncio
import os
from together import AsyncTogether, Together

# Page configuration
st.set_page_config(
    page_title="🧠 LLM Fusion Hub",
    page_icon="🧪",
    layout="centered"
)

# Gradient title using Markdown
st.markdown(
    """
    <h1 style='text-align: center; color: #4A90E2;'>🧪 Mixture-of-Agents LLM App 🎯</h1>
    <p style='text-align: center;'>🤖 A delightful fusion of multiple AI minds – like an Avengers team, but for your questions!</p>
    """,
    unsafe_allow_html=True
)

# Get API key
together_api_key = st.text_input("🔐 Enter your Together API Key:", type="password")

if together_api_key:
    os.environ["TOGETHER_API_KEY"] = together_api_key
    client = Together(api_key=together_api_key)
    async_client = AsyncTogether(api_key=together_api_key)

    # Define reference models (your superhero squad!)
    reference_models = [
        "Qwen/Qwen2-72B-Instruct",
        "meta-llama/Llama-Vision-Free",
        "mistralai/Mixtral-8x22B-Instruct-v0.1",
        "meta-llama/Llama-Vision-Free",
    ]
    aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"

    aggregator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability. Responses from models:"""

    # User question input
    user_prompt = st.text_input("🗣️ What's your question for the AI Superteam?")

    async def run_llm(model):
        try:
            response = await async_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0.7,
                max_tokens=512,
            )
            return model, response.choices[0].message.content
        except Exception as e:
            return model, f"❌ Error from `{model}`: {e}"

    async def main():
        st.info("🧠 Assembling expert AI opinions... This may take a moment ⏳")
        results = await asyncio.gather(*[run_llm(model) for model in reference_models])

        # Show each model's response
        st.subheader("🧩 Individual Model Responses")
        for model, response in results:
            with st.expander(f"📦 Response from `{model}`"):
                st.markdown(f"```\n{response}\n```")

        # Aggregate time!
        st.subheader("🌟 Aggregated Wisdom from the AI Alliance")
        try:
            finalStream = client.chat.completions.create(
                model=aggregator_model,
                messages=[
                    {"role": "system", "content": aggregator_system_prompt},
                    {"role": "user", "content": ",".join(response for _, response in results)},
                ],
                stream=True,
            )

            # Display streamed aggregated response
            response_container = st.empty()
            full_response = ""
            for chunk in finalStream:
                if not hasattr(chunk, "choices") or not chunk.choices:
                    continue
                delta = chunk.choices[0].delta
                if not hasattr(delta, "content") or delta.content is None:
                    continue
                full_response += delta.content
                response_container.markdown(full_response + "▌")
            response_container.markdown(full_response)
        except Exception as e:
            st.error(f"💥 Aggregation failed: {e}")

    if st.button("🚀 Get Answer"):
        if user_prompt:
            asyncio.run(main())
        else:
            st.warning("🧐 Hey! Don’t forget to type your question.")
else:
    st.warning("🔑 Please enter your Together API key to activate the LLM squad.")

# Sidebar info with humor
st.sidebar.title("📘 About the App")
st.sidebar.markdown(
    """
    Ever wanted multiple AI brains to argue and agree for you? 🤯  
    This app sends your question to a team of powerful open-source LLMs and then combines their answers into a master reply.

    ### 💡 How it works:
    1. 🧠 Each LLM gives their answer
    2. 🧙 A magical aggregator combines the responses
    3. 🎁 You get a unified, smart reply — no assembly required

    Models used:
    - Qwen/Qwen2-72B-Instruct
    - Meta LLaMA Vision-Free
    - Mixtral-8x22B-Instruct
    - DBRX Instruct

    Made with ❤️ by AI and Streamlit fans.
    """
)
