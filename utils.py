TASKS_SUPPORTED = [
    # "audio-classification",
    "automatic-speech-recognition",
    # "conversational",
    # "depth-estimation",
    "document-question-answering",
    "feature-extraction",
    "fill-mask",
    "image-classification",
    # "image-segmentation",
    "image-to-text",
    # "mask-generation",
    # "object-detection",
    "question-answering",
    "summarization",
    # "table-question-answering",
    "text2text-generation",
    "text-classification",
    "text-generation",
    # "token-classification",
    "translation",
    # "translation_xx_to_yy",
    # "video-classification",
    "visual-question-answering",
    "zero-shot-classification",
    # "zero-shot-image-classification",
    # "zero-shot-audio-classification",
    # "zero-shot-object-detection",
]

from huggingface_hub import HfApi, ModelFilter
def validate_models(task: str, model: str):
    # api = HfApi()
    # models = api.list_models(
    #         filter = ModelFilter(
    #         task = task,
    #         model_name = model
    #     )
    # )
    # return len(models) != 0
    return True

VALIDATE_MODELS = validate_models