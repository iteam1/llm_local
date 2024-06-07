# llm_local

 run llm model on local system

# guide llamafile

1. Download [llava-v1.5-7b-q4.llamafile](https://huggingface.co/Mozilla/llava-v1.5-7b-llamafile/resolve/main/llava-v1.5-7b-q4.llamafile?download=true) (4.29 GB)

2. Grant permission for your computer to execute this new file (If you're on Windows, rename the file by adding ".exe" on the end):

        chmod +x llava-v1.5-7b-q4.llamafile

3. Run the llamafile (On your browser http://localhost:8080/) 

        ./llava-v1.5-7b-q4.llamafile

        ./llava-v1.5-7b-q4.llamafile --server --nobrowser (server mode)

        CUDA_VISIBLE_DEVICES=0 ./Meta-Llama-3-8B-Instruct.Q4_1.llamafile --gpu nvidia (for specific GPU)

4. Kill process `sudo kill <PID>`

# json API Quickstart

- Curl API Client Example:

        curl http://localhost:8080/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer no-key" \
        -d '{
        "model": "LLaMA_CPP",
        "messages": [
        {
                "role": "system",
                "content": "You are LLAMAfile, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."
        },
        {
                "role": "user",
                "content": "Write a limerick about python exceptions"
        }
        ]
        }' | python3 -c '
        import json
        import sys
        json.dump(json.load(sys.stdin), sys.stdout, indent=2)
        print()
        '

- Python API Client example:

        #!/usr/bin/env python3
        from openai import OpenAI
        client = OpenAI(
        base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
        api_key = "sk-no-key-required"
        )
        completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=[
                {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
                {"role": "user", "content": "Write a limerick about python exceptions"}
        ]
        )
        print(completion.choices[0].message)

# shout down for

[llamafile](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file)

[llama.cpp](https://github.com/ggerganov/llama.cpp)

[llama-cpp-python](https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file)

[6 Ways For Running A Local LLM](https://semaphoreci.com/blog/local-llm)
