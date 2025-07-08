from llama_cpp import Llama
llm = Llama(model_path="models/mistral-7b.Q4_K_M.gguf", n_ctx=2048)

def ask_llm(prompt):
     output = llm(prompt, max_tokens=512, stop=["</s>"])
     return output['choices'][0]['text'].strip()
