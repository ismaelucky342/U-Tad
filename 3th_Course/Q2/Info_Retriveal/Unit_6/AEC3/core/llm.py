"""LLM interaction module: local inference and API fallbacks."""

import os
import torch
import requests
from pathlib import Path


class LLMHandler:
    """Handles local LLM inference and API fallbacks."""

    @staticmethod
    def chat_local_llm(prompt: str = None, 
                       model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                       max_new_tokens: int = 512,
                       temperature: float = 0.7) -> None:
        """
        Run a pretrained LLM locally for interactive chat.
        
        If a prompt is provided, generates a response and continues conversation.
        Default model (TinyLlama-1.1B) runs on CPU or low-VRAM GPUs (~4GB).
        
        Args:
            prompt: Initial message (optional)
            model_name: HuggingFace model ID
            max_new_tokens: Max tokens per response
            temperature: Sampling temperature (0=deterministic, 1=random)
            
        Raises:
            ImportError: If transformers/torch not installed
        """
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
        except ImportError:
            raise ImportError(
                "transformers and torch required.\n"
                "Install: pip install transformers torch accelerate"
            )

        print(f"\n[LLM] Loading model '{model_name}' …")
        print("      (first run downloads and caches weights)\n")

        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.float16 if device == "cuda" else torch.float32

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            device_map="auto" if device == "cuda" else None,
            low_cpu_mem_usage=True,
        )
        if device == "cpu":
            model = model.to(device)

        model.eval()
        print(f"[LLM] Model loaded on {device.upper()}.\n")

        # Chat history
        history = []

        def _generate(user_message: str) -> str:
            """Generate response given current history."""
            history.append({"role": "user", "content": user_message})

            # Format for TinyLlama/Llama-style models
            chat_prompt = ""
            for turn in history:
                role = turn["role"]
                content = turn["content"]
                if role == "user":
                    chat_prompt += f"<s>[INST] {content} [/INST] "
                else:
                    chat_prompt += f"{content}</s> "

            inputs = tokenizer(chat_prompt, return_tensors="pt").to(device)
            with torch.no_grad():
                output_ids = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    do_sample=temperature > 0,
                    pad_token_id=tokenizer.eos_token_id,
                )

            new_ids = output_ids[0][inputs["input_ids"].shape[1]:]
            response = tokenizer.decode(new_ids, skip_special_tokens=True).strip()
            history.append({"role": "assistant", "content": response})
            return response

        # Initial prompt
        if prompt:
            print("=" * 60)
            print("  INITIAL PROMPT (from network analysis)")
            print("=" * 60)
            print(prompt)
            print("\n[LLM] Generating response…\n")
            response = _generate(prompt)
            print("[LLM RESPONSE]")
            print("-" * 60)
            print(response)
            print("-" * 60 + "\n")

        # Interactive chat
        print("  Interactive chat started. Type 'exit' to quit.\n")
        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n[LLM] Session ended.")
                break

            if user_input.lower() in ('exit', 'quit', 'q', 'salir'):
                print("[LLM] Session ended.")
                break
            if not user_input:
                continue

            response = _generate(user_input)
            print(f"\nModel: {response}\n")

    @staticmethod
    def chat_api_llm(prompt: str, 
                     model: str = "gemini-1.5-flash",
                     api_key_env: str = "GEMINI_API_KEY") -> str:
        """
        Fallback: use Gemini API (Google AI Studio) when no GPU available.
        Free tier: 15 requests/min, 1M token context.
        
        Args:
            prompt: Prompt to send
            model: Gemini model variant
            api_key_env: Env var with API key
            
        Returns:
            Model response text
            
        Raises:
            EnvironmentError: If API key not found
            ValueError: If unexpected response format
        """
        api_key = os.environ.get(api_key_env, "")
        if not api_key:
            raise EnvironmentError(
                f"Set '{api_key_env}' env var with your Google AI Studio key.\n"
                "Free key at: https://aistudio.google.com/app/apikey"
            )

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        headers = {"Content-Type": "application/json"}
        params = {"key": api_key}

        resp = requests.post(url, json=payload, headers=headers, params=params, timeout=30)
        resp.raise_for_status()

        data = resp.json()
        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as e:
            raise ValueError(f"Unexpected Gemini response: {e}\n{data}")

        print("[Gemini API Response]")
        print("-" * 60)
        print(text)
        print("-" * 60)
        return text

    @staticmethod
    def save_chat_log(conversation: list, output_path: str = "outputs/llm_chat.txt"):
        """
        Save conversation to file.
        
        Args:
            conversation: List of {"role": ..., "content": ...} dicts
            output_path: Where to save
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        lines = ["=== LLM Chat Log ===\n"]
        for turn in conversation:
            role = turn["role"].upper()
            content = turn["content"]
            lines.append(f"{role}:\n{content}\n\n")
        
        Path(output_path).write_text("".join(lines), encoding="utf-8")
        print(f"[LLM] Chat log saved to '{output_path}'")
