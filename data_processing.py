from llama_index.llms.nvidia import NVIDIA
from llama_index.core.llms import ChatMessage, MessageRole

llm = NVIDIA(model="meta/llama3-70b-instruct",nvidia_api_key="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")
messages = [
    ChatMessage(
        role=MessageRole.SYSTEM, content=("You are a helpful assistant.")
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=("Did girl cum like man"),
    ),
]

res = llm.chat(messages)
print(res)
'''
Hybrid Optimization
A hybrid approach could further optimize cost and accuracy:

Pre-analyze the PDF: Use tools like PyMuPDF to classify pages as text-based or image-based.
For text-based pages: Extract text with PyMuPDF directly.
For image-based pages: Use OCR for simple images or multimodal LLMs for complex image data.
Adaptive Processing: Implement logic to switch between processing methods based on page content type.
This minimizes costs while maintaining high accuracy for diverse PDF content.
'''