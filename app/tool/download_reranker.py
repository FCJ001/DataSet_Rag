from modelscope.hub.snapshot_download import snapshot_download

# 下载到项目 models/rerank 目录
local_dir = "./models/rerank"

model_dir = snapshot_download(
    model_id="BAAI/bge-reranker-large",
    cache_dir=local_dir,
)

print("下载完成，模型目录：", model_dir)
