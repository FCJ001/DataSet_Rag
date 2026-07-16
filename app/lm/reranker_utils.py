import os
# 必须在导入 FlagEmbedding / transformers 之前设置，禁止加载 TensorFlow
os.environ["USE_TF"] = "0"

from FlagEmbedding import FlagReranker
from app.conf.reranker_config import reranker_config
from app.utils.path_util import PROJECT_ROOT

_reranker_model = None


def get_reranker_model():
    global _reranker_model
    if _reranker_model is None:
        model_path = reranker_config.bge_reranker_large
        # 相对路径 → 基于 PROJECT_ROOT 转为绝对路径，不依赖 CWD
        if model_path and not os.path.isabs(model_path) and os.path.exists(os.path.join(PROJECT_ROOT, model_path)):
            model_path = os.path.join(PROJECT_ROOT, model_path)
        _reranker_model= FlagReranker(
            model_name_or_path=model_path,
            device=reranker_config.bge_reranker_device,
            use_fp16=reranker_config.bge_reranker_fp16
        )
    return _reranker_model