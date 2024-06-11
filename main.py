import base64
import requests


url = "xxx"
headers = {
    'api-key': 'your api key',
    "Content-Type": "application/json; charset=utf-8",
    "Encoding": "utf-8"
}

data = {
    "temperature": 0.5,
    "max_tokens": 2048
}


def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        base64_datas = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/png;base64,{base64_datas}"


def generate_from_gpt4o(system, question, image_file=None, example_question=None, example_image_file=None, example_assistant=None):
    messages = []
    system_message = {"role": "system", "content": system}
    messages.append(system_message)

    if image_file:
        if example_question and example_image_file and example_assistant:
            example_image_url = image_to_base64(example_image_file)
            example_content_text = {"type":"text", "text":example_question}
            example_content_url = {"type":"image_url", "image_url":{"url":example_image_url, "detail":"auto"}}
            example_content = []
            example_content.append(example_content_text)
            example_content.append(example_content_url)
            example_user_message = {"role":"user", "content":example_content}
            example_assistant_message = {"role":"assistant", "content":example_assistant}
            messages.append(example_user_message)
            messages.append(example_assistant_message)

        image_url = image_to_base64(image_file)
        content_text = {"type":"text", "text":question}
        content_url = {"type":"image_url", "image_url":{"url":image_url, "detail":"auto"}}
        content = []
        content.append(content_text)
        content.append(content_url)
        user_message = {"role":"user", "content":content}

    else:
        if example_question and example_assistant:
            example_user_message = {"role":"user", "content":example_question}
            example_assistant_message = {"role":"assistant", "content":example_assistant}
            messages.append(example_user_message)
            messages.append(example_assistant_message)

        user_message = {"role":"user", "content":question}
    
    messages.append(user_message)
    data["messages"] = messages
    response = requests.post(url, headers=headers, json=data)
    output = response.json()
    if "error" not in output:
        return output
    else:
        return None


def load_prompts(path):
    with open(path, "r", encoding="utf8") as f:
        return "".join(f.readlines())



if __name__ == "__main__":

    # Get image description
    system_prompt = "you are a helpful visual assistant"
    image_file = "xxx"  # local path
    question_prompt = "Please provide a summary of the image and generate underlying data table for the chart"
    image_description = generate_from_gpt4o(system_prompt, question_prompt, image_file)


    CoTAR_system_prompt_dir = "/mnt/cfs/zhudan/a800_bak/zhudan/codes/StatsChartMWP/prompts/solution_augmentation.md"
    CoTAR_system_prompt = load_prompts(CoTAR_system_prompt_dir)
    
    question = "下面是一幅扇形统计图，请根据图中信息回答下列问题。\n白菜占总数的____%"
    question_prompt = "Question: {}\n Textual Description: {}".format(question, image_description)
    solution = generate_from_gpt4o(CoTAR_system_prompt, question_prompt)
    
